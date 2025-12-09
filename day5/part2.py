from typing import List

class Interval:
    def __init__(self, min, max):
        self.min = min
        self.max = max
    def __str__(self):
        return f'min: {self.min}, max: {self.max}'
    
class Graph:
    def __init__(self):
        self.nodes = {}
    def add_node(self, node):
        self.nodes[node] = []
    def add_nodes(self,nodes):
        for node in nodes:
            self.add_node(node)
    def connect(self, nodeA, nodeB):
        self.nodes[nodeA].append(nodeB)
        self.nodes[nodeB].append(nodeA)
    def isConnected(self, nodeA, nodeB):
        return nodeB in self.nodes[nodeA] and nodeA in self.nodes[nodeB]
    def adj(self, node):
        return self.nodes[node]
    def bfs(self,init_node):
        
        visited = []
        queue = []
        queue.append(init_node)
        visited.append(init_node)
        while queue:
            s = queue.pop(0)
            for i in self.adj(s):
                if not i in visited:
                    queue.append(i)
                    visited.append(i)
        return(visited)
    def traverse(self):
        visited = []
        not_visited = list(self.nodes)
        print("not_visited: ", not_visited)
        groups = []
        while len(visited)<len(self.nodes):
            visited_now = self.bfs(not_visited[0])
            print('visited_now: ', visited_now)
            for i in visited_now:
                not_visited.pop(i)
            visited = visited + visited_now
            groups.append(visited_now)
        
        return groups

    

def has_interception(intervalA: Interval, intervalB: Interval):
     low_a = intervalA.min
     up_a = intervalA.max

     low_b = intervalB.min
     up_b = intervalB.max
     return ((low_a>= low_b and low_a<=up_b) or (up_a>= low_b and up_a<=up_b)) or ((low_b>= low_a and low_b<=up_a) or (up_b>= low_a and up_b<=up_a))
     


def parse_input(file_path:str):
    with open(file_path, 'r') as mfile:
        intervals = {}
        for i, line in enumerate(mfile):
            line_content = line.rstrip()
            if len(line_content) == 0:
                break
            [low, up] = line_content.split('-')
            interval =Interval(int(low),int(up))
            intervals[i] = interval
        return intervals
    
def join(low_a, up_a, low_b, up_b):
    low_result = 0
    up_result = 0
    union = False
    if ((low_a>= low_b and low_a<=up_b) or (up_a>= low_b and up_a<=up_b)) or ((low_b>= low_a and low_b<=up_a) or (up_b>= low_a and up_b<=up_a)):
            union = True
            low_result = min(low_a, low_b)
            up_result = max(up_a, up_b)
    
    return [union, [low_result, up_result]]
   
# def group_intervals(intervals: List[Interval]):
#      grouped = []
#      for i, intervalA in enumerate(intervals):
#           for j in range(i, len(intervals)):
#                intervalB = intervals[j]
#                if has_interception(intervalA, intervalB):
                    
          

intervals = parse_input('day5/input/basic.txt')
for key, interval in intervals.items():
    print(f'key: {key}, interval: {interval}')


# init graph
mgraph = Graph()
mgraph.add_nodes(list(intervals))
print(mgraph.nodes)
print('--------')

# create connections
for i in range(0, len(intervals)):
    for j in range(i+1, len(intervals)):
        intervalA = intervals[i]
        intervalB = intervals[j]
        print(intervalA, '\t', intervalB, end='\t')
        if has_interception(intervalA, intervalB):
            print('Connect\t', end='')
            mgraph.connect(i,j)
        print(i, j)
        print()

print('---------')
print(mgraph.nodes)
mgraph.bfs(1)


print(mgraph.traverse())