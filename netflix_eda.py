import pandas as pd
df = pd.read_csv("netflix_titles.csv")
head= df.head(5)
dtypes= df.dtypes
null_counts= df.isnull().sum()
shape= df.shape
print(head)
print(dtypes)
print(null_counts)
print(shape)

country_null_percentage = len(df[df["country"].isnull()]) / len(df)*100 #finding percentage of null values in country column, len(df[df["country"].isnull()]) gives the number of rows where country is null,the outer df filters the rows where isnull os True andgives that number of rows, len(df) gives the total number of rows in the dataframe, dividing these two gives the percentage of null values in country column
print(f"Percentage of null values in 'country' column: {country_null_percentage:.2f}%")

director_null_percentage = len(df[df["director"].isnull()]) / len(df)*100 #finding percentage of null values in director column, len(df[df["director"].isnull()]) gives the number of rows where director is null,the outer df filters the rows where isnull os True andgives that number of rows, len(df) gives the total number of rows in the dataframe, dividing these two gives the percentage of null values in director column
print(f'Percentage of director null values: {director_null_percentage: .2f}%')

value_counts = (df["country"]).value_counts()
print(value_counts)

df["date_added"]= pd.to_datetime(df["date_added"], format='mixed') #converting date_added column to datetime format
print(df["date_added"].dt.year.value_counts()) #counting number of movies added in each year, df.year gives the year of the date_added column, value_counts() counts the number of occurrences of each year

print(df.columns) #printing all the columns in the dataframe
print(df["type"].value_counts())
df["year_added"]= df["date_added"].dt.year
ratio_over_time = df.groupby(["year_added", "type"]).size() #size tells us the number of rows
print(ratio_over_time)