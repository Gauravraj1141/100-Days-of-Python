# num = [2,3,4,3,4,2,4,5,4,5,26]
#
# for i in range(len(num)):
#     for k in range(i+1,len(num)):
#         if num[i] == num[k]:
#             print(num[i] , "is duplicate")
#             break


import bisect

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,77]

index = bisect.bisect_right(my_list,85)

print(index)
