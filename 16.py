import itertools
import heapq

def build_graph_from_input(file_name : str):
    board = []

    #READ INPUT AND CREATE BOARD REPRESENTATION
    with open(file_name, 'r') as file:
        for line in file:
            row = [char for char in line.strip()]  # Remove '\n'
            board.append(row)

    start_x, start_y = len(board)-2, 1
    goal_x,goal_y = 1,len(board[0])-2

    #EACH STATE CONSISTING OUT OF COORDINATE AND CURRENT ORIENTATION IS A NODE
    states = [
        [i for i in range(0, len(board[0]))],
        [i for i in range(0, len(board))], 
        ['UP', 'RIGHT', 'DOWN', 'LEFT']
    ]
    directions = {'UP':(-1, 0), 'RIGHT':(0,1), 'LEFT':(0,-1), 'DOWN':(1,0)}
    nodes = [element for element in itertools.product(*states)]
    
    edges = dict()
    for node in nodes:
        edges[node] = []
    for node in nodes:
        i,j,direction = node
        if board[i][j] != '#':
            if direction == 'UP' or direction == 'DOWN':
                edges[node].append((i,j,'LEFT'))
                edges[node].append((i,j,'RIGHT'))
            elif direction == 'RIGHT' or direction == 'LEFT': 
                edges[node].append((i,j,'DOWN'))
                edges[node].append((i,j,'UP'))
            x,y = directions[direction]
            i += x
            j += y
            if board[i][j] != '#':
                edges[node].append((i,j,direction))
    return start_x,start_y,goal_x,goal_y,nodes,edges


def run_dijkstra(nodes, edges):
    queue = []
    heapq.heappush(queue, (0,(start_x, start_y, 'RIGHT')))
    distances = {}
    for node in nodes:
        distances[node] = float('inf')
    distances[(start_x, start_y, 'RIGHT')] = 0

    visited = set()
    i = 0
    while queue:
        dist,cur = heapq.heappop(queue)
        x,y,direction = cur
        if cur in visited:
            continue
        visited.add(cur)
        for neighbor in edges[cur]:
            i,j,_ = neighbor
            if x == i and y == j:
                distances[neighbor] = min(1000 + dist, distances[neighbor])
            else:
                distances[neighbor] = min(1 + dist, distances[neighbor])
            heapq.heappush(queue, (distances[neighbor], neighbor))
        i += 1
    return distances



start_x,start_y,goal_x,goal_y,nodes,edges = build_graph_from_input('input.txt')
distances = run_dijkstra(nodes, edges)

print(min(
    distances[(goal_x, goal_y, 'UP')],
    distances[(goal_x, goal_y, 'DOWN')],
    distances[(goal_x, goal_y, 'LEFT')],
    distances[(goal_x, goal_y, 'RIGHT')]))