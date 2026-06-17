import pandas as pd

df = pd.read_csv(
    "data/processed/featured_credit_data.csv"
)
print(
    df["SeriousDlqin2yrs"]
    .value_counts()
)
print(
    df["SeriousDlqin2yrs"]
    .value_counts(normalize=True) * 100
)
import matplotlib.pyplot as plt

df["SeriousDlqin2yrs"] \
    .value_counts() \
    .plot(kind="bar")

plt.title("Target Distribution")

plt.show()