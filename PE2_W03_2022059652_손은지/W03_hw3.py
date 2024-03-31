# 2022059652 손은지
import numpy as np

# 운동장 N개
N = int(input("운동장의 개수를 입력하세요: "))

# 운동장마다 학생 M명
M = np.array(list(map(int, input("각 운동장에 있는 학생의 수를 입력하세요: ").split())))

# 담임은 X 관리, 교생은 Y 관리 (각 운동장에 담임은 오직 1명, ex) 2 2면, 담임은 2 관리 교생은 2 관리)
X, Y = map(int, input("담임과 교생의 수를 입력하세요: ").split())

# 각 운동장마다 필요한 선생님 수 계산
t = np.sum(np.ceil((M - X) / Y)) + N # (M - X) / Y)) + N, 3 4 5의 경우 2 2 3의 t가 필요

# 최소 t
print("필요한 선생님 수의 최솟값:", t)
