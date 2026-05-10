from queue import PriorityQueue

graph={
    'A':[('B',1),('C',3)],
    'B':[('D',3),('E',6)],
    'C':[('F',5)],
    'D':[],
    'E':[('G',2)],
    'F':[('G',2)],
    'G':[]
}

heuristic={
    'A':7,
    'B':6,
    'C':4,
    'D':5,
    'E':2,
    'F':1,
    'G':0
}

def astar(start , goal):
    pq=PriorityQueue()
    pq.put((0,start))

    cost={start:0}
    parent={start:None}

    while not pq.empty():
        current=pq.get()[1]
        if current==goal:
            break
        for i,j in graph[current]:
            new_cost=cost[current]+j
            if i not in cost or new_cost < cost[i]:
                cost[i]=new_cost
                priority=new_cost+heuristic[i]
                pq.put((priority,i))
                parent[i]=current
    path=[]
    node=goal

    while node is not None:
        path.append(node)
        node=parent[node]
    path.reverse()

    print("shortest path:",path)
    print("Total cost",cost[goal])

astar('A','G')


