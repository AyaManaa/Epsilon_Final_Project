# Epsilon_Final_Project
This Project has two datasets. The first one is `prev_df` it has a history of previous loan applications and their status whether it's *Approved* or *Refused*.

The second one is `app_df` it's our main data set. It has the current clients that are applying for a loan, where we help the bank to decide whether to Approve or Refuse the loan. By analyzing the client's behavior and predicting whether the client will default or not.

After analyzing each data individually, I merged both data sets because they have a common ID column for clients who applied for a loan before and currently applying for another one.

After Analyzing the third data set *the merged one*, I preprocessed the data, applied information gain for feature selection, and used XGBClassifer for Model Selection with an accuracy of 95% 
