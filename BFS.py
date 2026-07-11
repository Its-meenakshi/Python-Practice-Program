def movgen(node,graph):
  return graph[node]
def bfs(graph,start,goal):
  OPEN=[]
  CLOSED=[]
  parent={}
  OPEN.append(start)
  parent[start]=None

  while OPEN:
    current=OPEN.pop(0)
    print("exploring nodes",current)
    if current == goal:
      print("goal found",goal)
      path = []
      node = goal
      while node not in None:
        path.append(node)
        node=parent[node]
    path.reverse()
    print("final path",path)
    print("closed list",CLOSED)

    children = movgen(current,graph)
    for child in children:
      if child not in OPEN and child not in CLOSED:
        OPEN.append(child)
        parent(child)=current

        CLOSED.append
        print("open list",OPEN)
        print("CLOSED LIST",CLOSED)
        print("-------------------")
        print("goal not found")
        graph = {
          'A':['B','C'],
          'B':['D','E'],
          'C':[],
          'D':[],
          'E':['G'],
          'G':[]
        }
        start = 'A'
        goal = 'G'
        bfs(graph,start,goal)