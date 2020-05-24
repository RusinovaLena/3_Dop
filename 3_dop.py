import numpy as np
import random as rand

P = np.array([[0.9, 0.08, 0.02],
              [0.4, 0.5, 0.1],
              [0, 0, 1]])


def modeling(current_state):
    count = 0
    work = 1
    broken = 2
    recycle = 3
    current = current_state
    while True:
        rnd = rand.uniform(0, 1)
        if current == work:
            if rnd > (P[0][1] + P[0][2]):
                current = work
            else:
                if rnd > P[0][2]:
                    current = broken
                else:
                    current = recycle
            count = count + 1
            continue

        if current == broken:
            if rnd > (P[1][0] + P[1][2]):
                current = broken
            else:
                if rnd > P[1][2]:
                    current = work
                else:
                    current = recycle
            count = count + 1
            continue

        else:
            return count


sum_work = 0
sum_broken = 0
N = 1000
work = 1
broken = 2
for i in range(N):
    sum_work = sum_work + modeling(work)
    sum_broken = sum_broken + modeling(broken)
print("Work: ")
print(float(sum_work/N))
print("Broken: ")
print(float(sum_broken/N))
t_0_2 = ((-1)*P[0][1] + P[1][1] - 1)/(P[0][0]*((-1)*P[1][1]) + P[0][0] + P[0][1]*P[1][0] + P[1][1] - 1)
t_1_2 = (P[0][0] - P[1][0] - 1)/(P[0][0]*(-P[1][1]) + P[0][0] + P[0][1]*P[1][0] + P[1][1] - 1)
print("Th_Work: ")
print(t_0_2)
print("Th_Broken: ")
print(t_1_2)

Work: 
33.028
Broken: 
26.62
Th_Work: 
32.2222222222222
Th_Broken: 
27.777777777777754
