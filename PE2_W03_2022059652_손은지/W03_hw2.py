# 2022059652 손은지
import numpy as np # numpy를 사용하겠다.

# 좌변 A
A = np.array([[11, 7, 8, -4, -2],
              [9, -8, 5, 11, -4],
              [1, 13, -10, 2, 1],
              [-3, 1, 1, -1, 2],
              [21, -7, -5, 1, 7]])

# 우변 B
B = np.array([23, 32, 10, 8, 31])

# 연립방정식(A,B)의 해를 계산
X = np.linalg.solve(A, B)

# 답 출력
for index, value in enumerate(X): # index 0, value 1.0000000000000004
    print(f"x{index+1} =", value)