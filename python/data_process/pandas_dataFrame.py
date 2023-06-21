import pandas as pd

# 创建示例数据框
data = {'City': ['shanghai_chongqing_beijing'],'Country':"China"}
df = pd.DataFrame(data)

##  一列转多列

# 拆分"City"列为三列
df[['city1', 'city2', 'city3']] = df['City'].str.split('_', expand=True)

# 输出结果
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>一列转多列结果展示<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n",df)

## 多列转一列
df["合并列"] = df[['city1', 'city2', 'city3']].apply(lambda x: '_'.join(x.dropna().astype(str)), axis=1)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>一多列转一列<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n",df)
## 一行转多行