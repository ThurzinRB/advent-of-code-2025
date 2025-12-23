import copy

class Point():
    def __init__(self, x:int, y: int):
        self.x = x
        self.y = y
    def __str__(self):
        return 'x: '+str(self.x) + '\ty: '+ str(self.y)
        

class Edge():
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
    def __str__(self):
        return 'START: ' + str(self.start) + '\tEND: ' + str(self.end)
        

class Polygon():
    def __init__(self, vertices):
        self.vertices = []
        for vertice in vertices:
            point = Point(vertice[0], vertice[1])
            self.vertices.append(point)
    def get_edges(self):
        edges = []
        edge = Edge(self.vertices[-1], self.vertices[0])
        edges.append(edge)
        for i in range(len(self.vertices)-1):
            edge = Edge(self.vertices[i], self.vertices[i+1])
            edges.append(edge)
        return edges
    def __str__(self):
        mstring = ''
        mstring += 'vertices: \n'
        mstring+= '\n'.join(list(map(str, self.vertices)))

        mstring+= '\nedges: \n'
        mstring+= '\n'.join(list(map(str, self.get_edges())))
        return mstring

class Square(Polygon):
    def __init__(self, diag_vertices):
        vertices = [
            [diag_vertices[0][0], diag_vertices[0][1]],
            [diag_vertices[0][0], diag_vertices[1][1]],
            [diag_vertices[1][0], diag_vertices[1][1]],
            [diag_vertices[1][0], diag_vertices[0][1]],
            ]         
        super().__init__(vertices)
    def get_area(self):
        A = self.vertices[0]
        B = self.vertices[2]
        dx = abs(A[0] - B[0])+1
        dy = abs(A[1] - B[1]) + 1
        return dx*dy



data = []
with open('day9/input/basic.txt') as mfile:
    for line in mfile:
        strip_line = line.rstrip()
        data.append(list(map(int,strip_line.split(','))))

# print(data)

polygon = Polygon(data)
print(polygon)
square = Square([data[0], data[3]])
print('---------')
print('SQUARE: ')
print(square)