# 2022059652 손은지
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 2, 0.2) # 0에서 2까지 0.2 간격으로 숫자들을 생성하여 배열 x에 저장
plt.plot(x, x, 'r--', x, x**2, 'bo', x, x**3, 'g-.') # (x, y, 옵션) 을 나타냄
# red -- 스티치직선, blue o 원형선, green -. 실점선
plt.show()
