#Depth First Search (DFS) Traversal)
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# Build the graph
graph = {}
for _ in range(int(input("Enter number of edges: "))):
    u, v = input("Enter edge (u v): ").split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)

# Start DFS
start = input("Enter start node: ")
print("DFS traversal:")
dfs(graph, start)

------------------------------------------------------------------------------------------------------------------------------------------------

#Breadth First Search (BFS) Traversal
def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(n for n in graph[node] if n not in visited)

# Build the graph
graph = {}
for _ in range(int(input("Enter number of edges: "))):
    u, v = input("Enter edge (u v): ").split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)

# Start BFS
start = input("Enter start node: ")
print("BFS Traversal:")
bfs(graph, start)

------------------------------------------------------------------------------------------------------------------------------------------------
#Algorithm for 8 Puzzle Problem(A* algorithm)
import heapq

goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def manhattan(s):
    return sum(abs(i - val // 3) + abs(j - val % 3) for i, row in enumerate(s)
               for j, val in enumerate(row) if val)

def get_blank(s):
    for i in range(3):
        for j in range(3):
            if s[i][j] == 0:
                return i, j

def neighbors(s):
    x, y = get_blank(s)
    moves = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            ns = [r[:] for r in s]
            ns[x][y], ns[nx][ny] = ns[nx][ny], ns[x][y]
            moves.append(ns)
    return moves

def astar(start):
    heap = [(manhattan(start), 0, start, [])]
    visited = set()
    while heap:
        _, g, state, path = heapq.heappop(heap)
        st = tuple(tuple(r) for r in state)
        if state == goal:
            return path + [state]
        if st in visited:
            continue
        visited.add(st)
        for n in neighbors(state):
            heapq.heappush(heap, (g + 1 + manhattan(n), g + 1, n, path + [state]))
    return None

# Start A* Search
start = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
res = astar(start)
for step in res:
    for r in step:
        print(r)
    print("---")

------------------------------------------------------------------------------------------------------------------------------------------------
#Selection Sort (Greedy Algorithm)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# User input and sort
arr = list(map(int, input("Enter numbers separated by space: ").split()))
print("Original array:", arr)
selection_sort(arr)
print("Sorted array:", arr)

------------------------------------------------------------------------------------------------------------------------------------------------
# N-Queens Problem (Backtracking)
def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(n):
    def solve(board, row):
        if row == n:
            print_board(board, n)
            return True
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                if solve(board, row + 1):
                    return True
                board[row] = -1
        return False

    def print_board(board, n):
        for row in range(n):
            row_str = ""
            for col in range(n):
                row_str += "Q " if board[row] == col else ". "
            print(row_str)
        print()

    board = [-1] * n
    if not solve(board, 0):
        print("No solution")

# Run for 9 queens
solve_nqueens(9)

------------------------------------------------------------------------------------------------------------------------------------------------
#Customer Chatbot (Rule-based NLP)
import random

def chatbot_response(user_input):
    responses = {
        'hi': 'Hello! How can I assist you today?',
        'hello': 'Hi there! How can I help you?',
        'how are you': 'I am just a program, but I\'m doing great! How can I help you?',
        'bye': 'Goodbye! Have a great day!',
        'help': 'I can help with general queries. Just ask me anything!',
        'default': 'Sorry, I didn\'t quite understand that. Can you please rephrase?'
    }
    user_input = user_input.lower()
    return responses.get(user_input, responses['default'])

def start_chat():
    print("Welcome to the customer service chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

start_chat()

------------------------------------------------------------------------------------------------------------------------------------------------
#Expert System for Information Management
class ExpertSystem:
    def __init__(self):
        self.knowledge_base = {
            'database': 'You should use a relational database management system (RDBMS) like MySQL for structured data.',
            'data storage': 'Consider cloud storage solutions like AWS S3 or Google Cloud Storage for scalability.',
            'backup': 'Use automated backups with version control and store them off-site for security.',
            'security': 'Encrypt sensitive data and implement access controls and multi-factor authentication.'
        }

    def get_advice(self, query):
        query = query.lower()
        for key in self.knowledge_base:
            if key in query:
                return self.knowledge_base[key]
        return "Sorry, I don't have advice on that topic."

def run_expert_system():
    print("Welcome to the Information Management Expert System. Ask me for advice.")
    expert_system = ExpertSystem()
    while True:
        query = input("You: ")
        if query.lower() == 'exit':
            print("Goodbye!")
            break
        advice = expert_system.get_advice(query)
        print(f"Expert System: {advice}")

run_expert_system()



