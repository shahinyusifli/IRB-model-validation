# IRB-model-validation
IRB model validation with statistical tests, distribution analyses, and comparisons. Also, there is a solution for selecting the top 500 approved clients based on previous approvals according to probability.

### Task 1
Create a report in English, based on the data in Excel below, using also a visual output (tables, figures), with your solutions in Word, Excel or combination of them.

The distributions of observations, defaults and exposure across Credit Conversion Factor (CCF) segments (use unique value Segment_ID) should be analysed on total portfolio and on model level and presented in the report. Significant concentrations should be highlighted. Comparison to model construction distribution shall also be made. 

In order to support qualitative conclusions, a supportive analysis should be performed using a suitable statistical test. For example, use the metric to measure how much population has shifted over time (between two samples in distribution).

### Task 2
There’s a small financial institution that provides home loans for residents of a town. Up to this point 2000 loan applications have been decided on and 915 town residents are now happy homeowners. 
Over the course of an expansion campaign 1000 new applicants applied for loans. Unfortunately, this number of applications is way the institution’s expectations, and the institution can issue a maximum of 500 loans. We need your help to figure out to whom should the loans be given. In the second attached excel file there are two spreadsheets: Applications_Decided_On  and New_Applications.

Both of these datasets contain client-specific information, such as:
-	Client_No – Unique identifier of applicant; 
-	Monthly_Income – Monthly income in euros; 
-	Years_Worked – The length of consecutive working years as of the time of application; 
-	Obligations – Reflects if applicant has any other obligations or not.


On the spreadsheet Applications_Decided_On there is also a column called Got_Approval which reflects if a loan was issued to given applicant. Using this information, we would like you to select 500 applicants that deserve the approval.


Please add your solution (along with the rationale/methodology) into the report in English, based on the data in the second Excel below, using also a visual output (tables, figures).
Additionally, please also give answers to the following questions: 
1. What’s the probability that client number 200 (Client_No=200) will fall under the category Got_Approval=YES? 
2. What’s the most important variable for approval? 

