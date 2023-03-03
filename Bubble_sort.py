# Bubble_sort

import sys

with open(sys.argv[1], 'r') as f:

    num_list = [int(x) for x in f.read().split(',')]

//Bubble Sort Algorithm

for i in range(len(num_list)):

    for j in range(i+1, len(num_list)):
    
        if num_list[i] > num_list[j]:
            num_list[i], num_list[j] = num_list[j], num_list[i]

print(num_list)
