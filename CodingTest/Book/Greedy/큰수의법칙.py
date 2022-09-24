N = int(input('숫자 개수 : '))
M = int(input('총 몇번 더할 것인지 : '))
K = int(input('한 숫자를 몇번까지 더할 것인지 : '))

num_list = []
num_list =  list(map(int, input('숫자 배열 입력').split()))

num_list.sort(reverse=True)

bigger_iter = M // K
small_iter = M % K

result = 0

for i in range(bigger_iter * K):
    result += num_list[0]

for j in range(small_iter):
    result += num_list[1]


print(result)


# while N!=0:


# num_dict = dict()
# max_num = 0
# max_i =  0
# for i in range(N):
#     num_dict[i] = int(input())
#     if num_dict[i] >= max_num:
#         max_num = num_dict[i]
#         max_i = i
#
# result =  0
# while M != 0:
#     result += max_num
#     K -= 1
#     M -= 1