# 2022059652 손은지
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 100) # -10에서 10 사이를 100개의 구간. 등간격으로 나누어 배열 x를 생성.
y = x ** 3 # 세제곱한 값을 y 배열에 저장
plt.plot(x, y) # 선 그래프 plot
plt.xscale('symlog') # x축의 스케일을 'symlog'로 변경
plt.show() # 화면에 표시
