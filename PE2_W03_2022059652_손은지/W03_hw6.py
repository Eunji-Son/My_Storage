# 2022059652 손은지
import pandas as pd

c = ['col1', 'col2', 'col3'] # c 리스트에 열 이름 저장
l = [[1, 2, 3], [11, 12, 13]] # l 리스트에 data frame의 행 저장

# DataFrame 생성. c와 l 전달
df_l = pd.DataFrame(l, columns=c)
# columns : 열, 열이름은 굳이 안 지어줘도 ok 안 지어주면 0 1 2 이런식으로 열의 이름이 자동 지정.
# index=index_names으로 행의 이름도 지어줄 수 있음.

print(df_l)
print(df_l.to_string()) # 문자열 표현 출력.