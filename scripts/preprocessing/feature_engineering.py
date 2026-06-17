import pandas as pd

df = pd.read_csv(
    "data/processed/cleaned_credit_data.csv"
)

print(df.shape)
df["TotalLatePayments"] = (
    df["NumberOfTime30-59DaysPastDueNotWorse"]
    +
    df["NumberOfTime60-89DaysPastDueNotWorse"]
    +
    df["NumberOfTimes90DaysLate"]
)
df["IncomePerCreditLine"] = (
    df["MonthlyIncome"]
    /
    (df["NumberOfOpenCreditLinesAndLoans"] + 1)
)
df["HighDebtFlag"] = (
    df["DebtRatio"] > 1
).astype(int)
df["AgeGroup"] = pd.cut(
    df["age"],
    bins=[18,30,50,float("inf")],
    labels=["Young","Middle","Senior"]
)
age_mapping = {
    "Young":0,
    "Middle":1,
    "Senior":2
}

df["AgeGroup"] = df["AgeGroup"].map(age_mapping)
df["AgeGroup"] = df["AgeGroup"].astype(int)
df.to_csv(
    "data/processed/featured_credit_data.csv",
    index=False
)
print(df.columns)

print(
    df[
        [
            "TotalLatePayments",
            "IncomePerCreditLine",
            "HighDebtFlag",
            "AgeGroup"
        ]
    ].head()
)