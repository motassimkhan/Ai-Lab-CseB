import pandas as pd

s1 = pd.Series(['bmw','toyota','tata','kia'])
print(s1)
s2 = pd.Series(['M0','corolla','harrier','carens'])
print(s2)
df = pd.DataFrame({'Make':s1,'name':s2})
print(df)

head = df.head(2)
print(head)
tail = df.tail(2)
print(tail)

shape = df.shape
print(shape)

ele = df.iloc[1]
print(ele)
ele = df.loc[1]
print(ele)

df.to_csv('df.csv',index=False)

csv = pd.read_csv('data.csv')
print(csv)