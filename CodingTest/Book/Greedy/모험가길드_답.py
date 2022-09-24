n = int(input())
data = list(map(int,input().split()))
data.sort()

result = 0 #총 그룹의 수
cnt = 0 # 현재 그룹에 포함된 모험가의 수

for i in data:
    cnt += 1 # 공포도를 낮은 것부터 하나씩 확인하며
    # 현재 그룹에 해당 모험가를 포함시킨다.
    if cnt >= i: #현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면
        # 그룹을 결성
        result += 1
        cnt = 0
print(result)
