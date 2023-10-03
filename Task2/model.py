import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score

# =======================Import and prepare data=======================
df = pd.read_excel('task2_dataset.xlsx', sheet_name='Applications_Decided_On')

df_new_applications = pd.read_excel('task2_dataset.xlsx', sheet_name='New_Applications')
df_new_applications_first = pd.read_excel('task2_dataset.xlsx', sheet_name='New_Applications')

df['Obligations'] = df['Obligations'].replace({"YES": 1, "NO": 0})
df['Got_Approval'] = df['Got_Approval'].replace({"YES": 1, "NO": 0})

df_new_applications['Obligations'] = df_new_applications['Obligations'].replace({"YES": 1, "NO": 0})

df.drop('Client_No',axis=1,inplace=True)
df_new_applications.drop('Client_No',axis=1,inplace=True)


X = df[["Monthly_Income", "Years_Worked", "Obligations"]].values
y=df["Got_Approval"].values

def set_percentage_of_prob(value):
    if value == 1 :
        return "100%"
    elif value >= 0.9:
        return '90%'
    elif value >= 0.8:
        return '80%'
    elif value >= 0.7:
        return '70%'
    elif value >= 0.6:
        return '60%'
    elif value >= 0.5:
        return '50%'
    elif value >= 0.4:
        return '40%'
    elif value >= 0.3:
        return '30%'
    elif value >= 0.2:
        return '20%'
# =======================END=======================


# =======================Model train and Model selection=======================
xtrain, xtest,ytrain,ytest=train_test_split(X,y,test_size=0.2,random_state=0)

m1=LogisticRegression()
m1.fit(xtrain,ytrain)
yp1=m1.predict(xtest)

m2=DecisionTreeClassifier()
m2.fit(xtrain,ytrain)
yp2=m2.predict(xtest)

# Print scores for Decision Tree Classifier
print("Decision Tree Classifier :")
print(" accuracy is ",accuracy_score(ytest,yp2))
print(" precision score is ",precision_score(ytest,yp2))
print(" recall is ",recall_score(ytest,yp2))
print(" f1 score is ",f1_score(ytest,yp2))

# Print scores for Logistic Regression
print("Logistic Regression :")
print(" accuracy is ",accuracy_score(ytest,yp1))
print(" precision score is ",precision_score(ytest,yp1))
print(" recall is ",recall_score(ytest,yp1))
print(" f1 score is ",f1_score(ytest,yp1))
# =======================END=======================


# =======================Predict probability and export 500 approved clients=======================
prediction_probs = m1.predict_proba(df_new_applications)[:, 1]
Prediction_Probs = pd.Series(prediction_probs, name='Prediction_Probs')
# Assign the new Prediction_Probs as a new column in the DataFrame
df_new_applications_first['Prediction_Probs'] = Prediction_Probs
sorted_df = df_new_applications_first.sort_values(by='Prediction_Probs', ascending=False)
top_500_applications = sorted_df.head(500)
top_500_applications.to_excel("approved_500_clients.xlsx", index=False)
# =======================END=======================


# =======================Find the most important value for approval according coefficients of futures=======================
coefficients = m1.coef_[0]
feature_names = df_new_applications.columns.tolist()
# Create a DataFrame to store coefficients and feature names
coefficients_df = pd.DataFrame({'Feature': feature_names, 'Coefficient': coefficients})
# Sort the coefficients in descending order of absolute value
coefficients_df['Absolute_Coefficient'] = coefficients_df['Coefficient'].abs()
coefficients_df = coefficients_df.sort_values(by='Absolute_Coefficient', ascending=False)
#Display the sorted coefficients
print(coefficients_df)
# =======================END=======================