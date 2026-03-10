import numpy as np
import random

pc=12
members=24
# def random_seating_arrangement(pc):
col1 = []

for num_pc in range(1, pc+1):
    col1.append([num_pc])


col1 = np.array(col1)
member_ids = list(range(1, members+1))
random.shuffle(member_ids)



col2 = []
col3 = []

for num_pc in range(pc):
    col2.append([member_ids[num_pc]])
    col3.append([member_ids[num_pc+pc]])

col2 = np.array(col2)
col3 = np.array(col3)



result = []

for num_pc in range(pc):
    row = [
        col1[num_pc][0],
        col2[num_pc][0],
        col3[num_pc][0],
    ]
    result.append(row)
result = np.array(result)

print("Номера рабочих мест:", result[:, 0])
print("Ученик 1:           ", result[:, 1])
print("Ученик 2:           ", result[:, 2])
