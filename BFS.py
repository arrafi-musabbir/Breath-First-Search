
'''
 the following section opens a text file and reads through it and initializes
 the graph in a dictionary
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
a graph of cities have been initialized in dictionary "d"'
the following commented out code can be used to display the elements of "d"
'''
# for i in d:
#     print(i, ":", d[i])


def bfs(dic, Start, Goal):
    que = list()   # to be used as a stack
    path = list()  # to keep track of the visited nodes
    temp = Start
    que.append(temp)
    while len(que) > 0:
        temp = que.pop(0)  # poping out the top element from stack

        if path.count(temp) < 1:  # ckecking if the node has been visited
            if dic[temp] is not None:   # checking if the node is a terminal
                for i in dic[temp]:
                    que.append(i)  # pushing in to the stack
            path.append(temp)  # enqueing the visited node to the path

        if temp == Goal:  # checking if recently visited is a GOAL
            break         # will break out if reached the GOAL node

    if temp == Goal:
        print("starting search-->", end=" ")
        for i in path:
            print(i, "-->", end=" ")
        print("reached GOAL")

    if len(que) == 0:
        print("starting search-->", end=" ")
        print("No path exist")


bfs(dic=d, Start="s", Goal="g")
