import math

class Junction_box:
    def __init__(self, input_str: str):
        self.key = input_str
        [self.x, self. y, self.z] = list(map(int,input_str.split(',')))
    def __str__(self):
        return 'x: ' + str(self.x) + '\ty: ' + str(self.y) + '\tz: ' + str(self.z)
    def dist2(self, junction_box):
        return (self.x - junction_box.x)*(self.x - junction_box.x) + (self.y - junction_box.y)*(self.y - junction_box.y) + (self.z - junction_box.z)*(self.z - junction_box.z)
    def get_closest(self, Junction_boxes: dict, mgraph):
        min_dist2 = math.inf
        min_key = ''
        adj_list = mgraph.adj(self.key)
        for key, junction_box in junction_boxes.items():
            if not key in adj_list:
                dist2 = junction_boxes[self.key].dist2(junction_box)
                if key != self.key and min_dist2>dist2:
                    # print('aaa')
                    min_dist2 = dist2
                    min_key = key
            # print(dist2)
        return [min_key, dist2]

class Graph:
    def __init__(self):
        self.nodes = {}
    def add_node(self, node):
        if not node in self.nodes:
            self.nodes[node] = []
    def connect(self, A, B):
        self.nodes[A].append(B)
        self.nodes[B].append(A)
    def adj(self, node):
        if not node in self.nodes: return []
        return self.nodes[node]


file_path = 'day8/input/basic.txt'
n = 10



with open(file_path, 'r') as mfile:
    data = list(map(lambda x: x.strip('\n'),mfile.readlines()))

junction_boxes = {}
for item in data:
    junction_boxes[item] = Junction_box(item)
print(*junction_boxes.values(), sep='\n')
mgraph = Graph()
print(junction_boxes['162,817,812'].get_closest(junction_boxes, mgraph))
print('-----------')
for i in range(n):
    min_dist = math.inf
    closest_pair = []
    for key, junction_box in junction_boxes.items():
        [local_closest, local_min_dist] = junction_box.get_closest(junction_boxes, mgraph)
        if min_dist != 0 and min_dist>local_min_dist:
            min_dist = local_min_dist
            closest_pair = [junction_box.key, local_closest]
    mgraph.add_node(closest_pair[0])
    mgraph.add_node(closest_pair[1])
    mgraph.connect(*closest_pair)
    print(closest_pair)

    