import time

start = time.time()
N = int(input())
data = list(map(int,input().split()))
data.sort() #오름차순으로 정렬

cnt = 1 # 모험가 수 count
result = 0
for i in range(len(data)):
    if data[i] == cnt: #count한 값과 공포도가 같다면 그룹 결성
        # print(data[i], data[i+1], i)
        result += 1
        cnt = 1
    else: #count한 값과 공포도가 다르다면 모험가를 한명 더
        cnt += 1

print(result)
end = time.time()

print(end - start)