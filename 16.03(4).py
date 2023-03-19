import random
import copy

list = []
for i in range(4):
    list.append(random.randint(0, 10))

print(f'list:{list}\t')

list1 = [[1, 2, 3, 4], [1, 2, 3, 5]]
list2 = copy.deepcopy(list1)
list2[0][3] = 100
print(f'list1:{list1}\t list2{list2}')