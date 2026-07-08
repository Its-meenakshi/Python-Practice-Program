def movgen(graph,node):
  return graph[node]
def dfs(graph,start,goal):
  OPEN=[]
  CLOSED=[]
  OPEN.append(start)
  while OPEN:
    current = OPEN.pop(0)
  print("Exploring nodes",current)
  if current == goal:
    print("Goal found",goal)
    print("closed list",CLOSED)
    CLOSED.append(current)
    children = movgen(current,graph)
    for child in reversed(children):
      if child not in OPEN and child not in CLOSED:
        OPEN.insert(0,child)
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
        dfs(graph,start,goal)
    
  






      