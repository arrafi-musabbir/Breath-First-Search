
'''
 the following section opens a text file and read throw it and initializes our
 graph in a dictionary

'''

with open("Weighted graph(cities).txt", "r") as f:
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


def bfs(d, S, G):
    visited = dict()
    que = list()
    path = list()
    temp = S
    que.append(temp)
    while len(que) > 0:
        temp = que.pop(0)
        if temp not in visited.keys():
            if d[temp] is not None:
                for i in d[temp]:
                    que.append(d[temp][i])
                    print(i)
                visited[temp] = 1
            else:
                visited[temp] = 1
            path.append(temp)
        elif temp in visited.keys():
            visited[temp] = visited[temp] + 1
        if temp == G:
            break
    if temp == G:
        print("starting search-->", end=" ")
        for i in path:
            print(i, "-->", end=" ")
        print("reached GOAL")
    if len(que) == 0:
        print("No path exist")

    print(que)


bfs(d, "a", "g")
