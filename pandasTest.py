
import pandas as pd

# I can read in some csv data an specificy which columns of the csv I want to use
df = pd.read_csv("crypto-markets.csv", usecols=["date", "symbol", "open","close"],
index_col="date")
print(df.head())


# I can create a custom column with a calculation as such:
df["difference"] = df.open - df.close
print(df.head())

# I can use built in data frame methods to analyze my data
print(df["symbol"].value_counts())

# if I want to access specific columns
print(df[["symbol", "open"]])

# I can create tables with specific columns from other tables

df2 = df[["symbol", "open"]]

# I can filter my data table to create another datatable as such:
df3 = df[df.symbol == "BTC"]

print(df3[df3.difference > 1000])

# I can sort a given data table as such
print(df3.sort_values("difference", ascending=False))

# after manipulating my data I can write it to a new file:
df4 = df3[df3.difference > 1000]
df4.sort_values("difference", ascending=False).to_csv("worstDrawDowns.csv")
