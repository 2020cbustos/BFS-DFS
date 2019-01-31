import random
import pprint
def make_make(size, lvl, st):
    # make a matrix with random ints
    matrix = [[random.randint(0,10) for row in range(size)] for col in range(size)]
    # loop through the matrix
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            # if element is > lvl = a free space
            if matrix[row][col] > lvl:
                matrix[row][col] = '.' # . = free space
                # else element is a wall
            else:
                matrix[row][col] = '|'
    x,y = st
    matrix[x][y] = "S"
    return matrix
# call our function to make a maze
matrix = make_make(10, 2, [5,5])
pprint.pprint(matrix)
# find all edges for node N
def find_edges(matrix, node):
    x,y = node
    edges = []
    length = len(matrix)
    # add conditions for nw, sw, ne, se
    for x,y in (x, y+1), (x, y-1), (x+1, y), (x-1, y):
        if 0 <= x < length and 0 <= y < length:
            # check if matrix[x][y] is a free space
            if matrix[x][y] == '.':
                edges.append([x,y])
    return edges
print(find_edges(matrix,[2,9]))


#BREATH-FIRST SEARCH

def bfs(matrix,node):
  queue = [[node]] # create queue
  #while something in queue, keep looking
  explored = [] # create explored list
  goal = [len(matrix)-1, len(matrix)-1]
  while queue: # cycle until queue is empty
    #FIFO check nodes in queue y creating path variable which is a single node
    path = queue.pop(0) #  # "pop" takes from the end (first in first out)
    node = path[-1]
    if node not in explored: #if node not in explored
          explored.append(node)
          edges = find_edges(matrix, node)
          for edge in edges:
            new_path = list(path)
            new_path.append(edge)
            queue.append(new_path) #first in first out # add path to explored
            if edge == goal:
              for x,y in new_path:
                matrix[x][y] = 'X'
              return matrix
  return ('no path found')
pprint.pprint(bfs(matrix, (0,0)))
# #create queue
# #create explored list
# #cycle until queue is empty
# #FIFO - check nodes in queue by creating path variable, which is a single node
# #if path not in explored do the following
# #add path to explored
# #find all of path's edges
# #add all edges to queue if not explored
# #clear path variable
# #repeat steps until done
# #return explored


#DEPTH-FIRST SEARCH

def dfs(matrix,node):
  stack = [[node]] # stack
  explored = [] # create explored list
  goal = [len(matrix)-1, len(matrix)-1]
  while stack: # cycle until stack is empty
    path = stack.pop(-1)
    node = path[-1] #index value (-1)
    if node not in explored: #if node not in explored
          explored.append(node)
          edges = find_edges(matrix, node)
          for edge in edges:
            new_path = list(path)
            new_path.append(edge)
            stack.append(new_path)
            if edge == goal:
              for x,y in new_path:
                matrix[x][y] = 'X'
              return matrix
  return ('no path found')
pprint.pprint(dfs(matrix, (0,0)))
