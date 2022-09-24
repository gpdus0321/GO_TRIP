import time

start = time.time()
N, K = map(int,input().split())
cnt = 0

while(N != 1): #N이 1일때까지 반복
    if(N%K == 0): #만약 K가 N의 배수라면
        N = N // K #N을 몫으로 바꾸고
        cnt += 1 #count 1 증가
    else: #만약 K가 N의 배수가 아니라면
        N -= 1 #1을 빼고 다시
        cnt += 1
end = time.time()

print(f'cnt : {cnt}')
print(f'time : {end - start}')





