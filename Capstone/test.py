from Map import Map
import util


A = Map()
a = util.Queue()
a.push((A.StartState,[]))
print(a.pop())
# #print(A.map)
# print(A.StartState)
# print(A.getSuccessors((1,2)))