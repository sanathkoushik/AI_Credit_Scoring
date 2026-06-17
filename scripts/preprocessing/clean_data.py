import pandas as pd
df=pd.read_csv("C:/Users/sanat/OneDrive/Desktop/AI_Credit_Scoring/data/raw/cs-training.csv")
df.drop(columns=["Unnamed: 0"],inplace=True)
median_income=df["MonthlyIncome"].median()
df["MonthlyIncome"].fillna(median_income,inplace=True)
df.drop_duplicates(inplace=True)
df=df[df["age"]>=18]
df=df[df["DebtRatio"]<5]
df.to_csv("data/processed/cleaned_credit_data.csv",index=False)
 