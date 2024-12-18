import itertools
import heapq

def build_graph_from_input(file_name : str):
    board = [['.']*71 for _ in range(71)]

    #READ INPUT AND CREATE BOARD REPRESENTATION
    with open(file_name, 'r') as file:
        for i,line in enumerate(file):
            x,y = map(int, line.strip().split(','))
            board[x][y] = '#'
            #EACH STATE CONSISTING OUT OF COORDINATE AND CURRENT ORIENTATION IS A NODE
            states = [
                [i for i in range(0, len(board[0]))],
                [i for i in range(0, len(board))]
            ]
            nodes = [element for element in itertools.product(*states)]
            edges = dict()
            print(board)
            for node in nodes:
                edges[node] = []
            for node in nodes:
                i,j = node
                if board[i][j] != '#':
                    if i >= 1 and board[i-1][j] != '#':
                        edges[node].append((i-1,j))
                    if j >= 1 and board[i][j-1] != '#':
                        edges[node].append((i,j-1))
                    if i < len(board)-1 and board[i+1][j] != '#':
                        edges[node].append((i+1,j))
                    if j < len(board[0])-1 and board[i][j+1] != '#':
                        edges[node].append((i,j+1))
            
            distances = run_dijkstra(nodes, edges)
            if distances[(70,70)] == float('inf'):
                print(x,y)
                break

def run_dijkstra(nodes, edges):
    queue = []
    heapq.heappush(queue, (0,(0, 0)))
    distances = {}
    for node in nodes:
        distances[node] = float('inf')
    distances[(0, 0)] = 0

    visited = set()
    i = 0
    while queue:
        dist,cur = heapq.heappop(queue)
        x,y = cur
        if cur in visited:
            continue
        visited.add(cur)
        for neighbor in edges[cur]:
            i,j = neighbor
            distances[neighbor] = min(1 + dist, distances[neighbor])
            heapq.heappush(queue, (distances[neighbor], neighbor))
    return distances

build_graph_from_input('input.txt')

