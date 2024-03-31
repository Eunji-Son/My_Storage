# 2022059652 손은지
import pandas as pd
cols = ['국어','수학', '영어', '과학','사회']
lists = [[83, 68, 92, 55, 85], [40, 95, 64, 87,77],[65,87,58,92,72]]
indexes = ['태현', '준수', '기준']
dfs = pd.DataFrame(lists, columns = cols, index = indexes)
print(dfs)

dfs.to_csv("./hw10_result.csv")
