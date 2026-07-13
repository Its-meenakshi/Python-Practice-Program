def movgen(node,graph):
  return graph[node]
def hill_climbing(graph,heuristic,start,goal):
  OPEN = []
  CLOSED = []
  OPEN.append(start)

  while OPEN:
    current = OPEN.pop()
    print("current node",current)
    print("heuristic value",heuristic[current])

    if current == goal:
      print("goal found", goal)
      return
    
    CLOSED.append(current)
    neighbors = movgen(current,graph)

    best = None
    best_value = float('inf')

    for node in neighbors:
      if node not in CLOSED:
        if heuristic[node]<best_value:
          best_value = heuristic[node]
          best = node

    if best is None or best_value >= heuristic[current]:
      print("no better neighbors found")
      print("hill climbing stopped")
      return
    
    print("Moving to",best)
    OPEN.append(best)
    print("goal not found")

graph = {
          'A':['B','C'],
          'B':['D','E'],
          'C':['F'],
          'D':[],
          'E':['G'],
          'F':[],
          'G':[]
        }
heuristic = {
   'A':6,
   'B':4,
   'C':5,
   'D':9,
   'E':2,
   'F':9,
   'G':0

}
hill_climbing(graph,heuristic,'A','G')
