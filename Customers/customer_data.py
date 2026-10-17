import pandas as pd
df = pd.read_csv("/content/messy_customer_sales_data.csv")
display(df)
df.info()
df.isnull().sum()
df.isnull().sum()/len(df)*100
df.describe().round()
