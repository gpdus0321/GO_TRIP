import util
from Map import Map

def BFS(problem,StartState,Goal):
    root = StartState
    queue = util.Queue()
    queue.push((root,[]))

    path = []
    while not queue.isEmpty():
        node, edges = queue.pop()
        
        if node==Goal:
            return edges

        if not node in path: #goal state가 아니고, 지나온 node도 아니라면
            path.append(node)#node를 지나온 리스트를 저장하는 path에 저장
            for successor, action in problem.getSuccessors(node): #다음으로 갈 수 있는 node(sussessor)와 node를 가는 방법 
                if not successor in path: #만약에 다음으로갈 node가 지나온것이 아니라면 큐에 넣는다.
                    queue.push((successor,edges + [action]))



MapNum = int(input('map을 선택해주세요(1,2) : '))
problem = Map(MapNum)

table_dict = problem.table_dict


t1 = input('첫번째 테이블 번호 : ')
t2 = input('두번째 테이블 번호 : ')
t3 = input('세번째 테이블 번호 : ')

input_list = [t1,t2,t3]

table_coordi=[problem.StartState]
for i in input_list:
    table_coordi.append(table_dict[i])

table_coordi.append(problem.StartState)
# print(table_coordi)

result_list= []
for i in range(4):
    a=BFS(problem,table_coordi[i],table_coordi[i+1])
    result_list.append(a)
print(result_list)