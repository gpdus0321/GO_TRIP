import time

start = time.time()
num_list = input()
result = 0

for i in range(0,len(num_list)-1):
    a = int(num_list[i])
    b = int(num_list[i+1])
    if i == 0:
        if a == 0 or a == 1:
            result = a + b
        else:
            result = a * b
    else:
        if a == 0 or a == 1:
            result = result + b
        else:
            result = result * b

end = time.time()
print(result)
print(f'time : {end - start}')


