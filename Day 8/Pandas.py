import csv
import pandas as pd
# pd is the alice of Pandas, alice is an alternate name used to refer the same thing

# # pandas version
print(pd.__version__)

# # pandas series: a column in a table
# a=[1,2,3]
# s=pd.Series(a)
# print(s)

# # Labels are the index of series: here s[0]: 0 is the label
# print(s[0])
# # label creation:
# sl=pd.Series(a,index=['x','y','z'])
# print(sl)
# print(sl['y']) # Here y is the label


# # Dictinary as a series
# example={
#     'Day 1':420,
#     'Day 2':310,
#     'Day 3':357
# }
# ex=pd.Series(example)
# print(ex)

# # to select some specific values in series, mention their index number in index
# ex1=pd.Series(example,index=['Day 1','Day 2'])
# print(ex1)


# dataset={
#     'cars':['Tata','BMW','Mahindra','Volvo','Ford','Ferrari','Hyundai','Honda',None,'Suzuki'],
#     'ratings':[5,4.7,4.5,5,4,4,3,3.5,3.7,2.5]
# }

# # To convert into data frame
# # df=pandas.DataFrame(dataset)
# df=pd.DataFrame(dataset)
# # print(df)
# # print(df.loc[0]) # The result is pandas series
# print(df.loc[[0,1]]) # for more locations result will be DF

csv_df=pd.read_csv('./data.csv')
# print(csv_df) # gives first and last five rows of enntire data
# print(csv_df.to_string()) # to prit entire data Frame
# print(pd.options.display.max_rows) # 60 : if my dataframe has more than 60 records then it will print top 5 and bottom 5 rows only


# pd.options.display.max_rows=999 # We can change the max rows by this line

# print(csv_df.head(10))
# print(csv_df.tail(10))
print(csv_df.info())


# Data cleaning

# 1. Drop null values
# dropped_csv_df=csv_df.dropna() # By default it returns new Dataframe use 'inplace=True' to change original dataframe
# print(dropped_csv_df.info())

# 2. Replace the null values with new one
csv_df.fillna({'Calories':130},inplace=True) # If we do not mention col name then it will replace all the null values with mentioned one