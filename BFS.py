
'''
 the following section opens a text file and read throw it and initializes our
 graph in a dictionary

'''

with open("graph(cities).txt", "r") as f:
    l1 = list()
    d = dict()
    for i in f:
        l1 = i.split()
        for j in l1:
            if len(l1) == 1:
                d[l1[0]] = None
            else:
                d[l1[0]] = l1[1:]

'''
a graph of cities have been initialized in dictionary "d"

'''
print(d)


def bfs(dic, Start, Goal):
    visited = dict()
    que = list()
    path = list()
    temp = Start
    que.append(temp)
    while len(que) > 0:
        temp = que.pop(0)
        if temp not in visited.keys():
            if dic[temp] is not None:
                for i in dic[temp]:
                    que.append(i)
                    print(i)
                visited[temp] = 1
            else:
                visited[temp] = 1
            path.append(temp)
        elif temp in visited.keys():
            visited[temp] = visited[temp] + 1
        if temp == Goal:
            break
    if temp == Goal:
        print("starting search-->", end=" ")
        for i in path:
            print(i, "-->", end=" ")
        print("reached GOAL")
    if len(que) == 0:
        print("No path exist")

    #return que

bfs(dic=d, Start="a", Goal="t")
