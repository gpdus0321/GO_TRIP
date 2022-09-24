change = int(input('거스름돈 입력 : '))

change_list = [500,100,50,10]

cnt = 0
for i in change_list:
    tmp = change // i
    change = change % i
    cnt += tmp

print(cnt)


