import pandas as pd
import numpy as np
dates=pd.date_range('20250101',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
# 选择数据
print(df)
print(df.A)
print(df[0:3])
print(df.loc['20250101'])
print(df.loc[:,['A','B']])
print(df.loc['20250101',['A','B']])
print(df.iloc[3:5,1:3])
print(df.iloc[[1,3,5],1:3])
print(df[df.A>8])
# 设置值
print(df)
df.iloc[2,2]=111
df.loc['20250103','A']=10
df.A[df.A>4]=0
print(df)
df['F']=np.nan
df['E']=pd.Series([1,2,3,4,5,6],index=pd.date_range('20250101',periods=6))
print(df)
# 处理丢失数据
df.iloc[0,1]=np.nan
df.iloc[1,2]=np.nan
print(df.dropna(axis=0,how='any'))
print(df.dropna(axis=1,how='any'))
print(df.fillna(value=0))
print(df.isnull())
print(np.any(df.isnull()) == True)
# 导入导出数据
data = pd.read_csv(r'C:\Users\王浩龙\Desktop\cs.csv')
print(data)
data.to_pickle('student.pkl')
# 合并
df1=pd.DataFrame(np.ones((3,4))*0,columns=['A','B','C','D'])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['A','B','C','D'])
df3=pd.DataFrame(np.ones((3,4))*2,columns=['A','B','C','D'])
print(df1)
print(df2)
print(df3)
res=pd.concat([df1,df2,df3],axis=0,ignore_index=True) 
print(res)  
df1=pd.DataFrame(np.ones((3,4))*0,columns=['A','B','C','D'],index=[1,2,3])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['B','C','D','E'],index=[2,3,4])
print(df1)
print(df2)
res = pd.concat([df1, df2])
res = pd.concat([df1, df2], join='inner', ignore_index=True)
df2=df2.reindex(df1.index)
res = pd.concat([df1, df2], axis=1, join='inner')
print(res)
left=pd.DataFrame({'key':['K0','K1','K2','K3'],
                   'A':['A0','A1','A2','A3'],
                     'B':['B0','B1','B2','B3']})
right=pd.DataFrame({'key':['K0','K1','K2','K3'],
                    'C':['C0','C1','C2','C3'],
                     'D':['D0','D1','D3','D4']})
print(left)
print(right)   
res = pd.merge(left,right,on='key')
print(res)
left=pd.DataFrame({'key1':['K0','K1','K0','K0'],
                   'key2':['K0','K0','K1','K1'],
                     'B':['B0','B1','B2','B3']})
right=pd.DataFrame({'key1':['K1','K0','K1','K1'],
                    'key2':['K0','K1','K1','K1'],
                     'D':['D0','D1','D3','D4']})
res = pd.merge(left, right, on=['key1', 'key2'], how='inner')
print(res)
res = pd.merge(left, right, on=['key1', 'key2'], how='outer')
print(res)
# how = 'left'/'right'/'inner'/'outer'
boys = pd.DataFrame({'k':['K0','K1','K2'],'age':[1,2,3]})
girls = pd.DataFrame({'k':['K0','K0','K3'],'age':[4,5,6]})
print(boys)
print(girls)
res = pd.merge(boys,girls,on='k',suffixes=['_男','_女'],how='outer')
print(res)



