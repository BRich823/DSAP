import sys
import matplotlib.pyplot as plt
import numpy as np
import triangle as tr
from shapely.geometry import Polygon

def read_polygon_vertices(file_name):
  file_object = open(file_name, "r")
  # Input the number of rows and columns
  n_of_vertices = int(file_object.readline())
  vertices = []
  # Input the matrix elements
  for i in range(n_of_vertices):
    point = list(map(int, file_object.readline().split()))
    vertices.append(point)

  return vertices,n_of_vertices


vertices,N = read_polygon_vertices(sys.argv[1])
polygon_points = np.array(vertices)

# segments
i = np.arange(N)
seg = np.stack([i, i + 1], axis=1) % N
A = dict(vertices=np.array((polygon_points)),segments=seg)
B = tr.triangulate(A,'p')
# print(B)
triangles = (B['triangles'])
print("The triangles for the polygon produced by the library:")
print(triangles)
tr.compare(plt, A, B)
plt.show()
# And then you can plot them separately
original_polygon = Polygon(polygon_points)
x,y = original_polygon.exterior.xy
plt.plot(x,y)
plt.show()
# And to plot the triangles
for t in triangles:
    triangle_points = Polygon(polygon_points[t])
    x,y = triangle_points.exterior.xy
    plt.plot(x,y)
fig = plt.gcf()
ax = fig.gca()
# Now highlight some vertices (the locations of the guards)

# Your code will go here.
# Your code will find a subset of vertices that covers the entire polygon
# Ideally it should be of minimum size
#
# The code below just shows how to higlight
# the vertices that are part of the solution
#
# gets the degree of each vertice
counts = []
for v in range(len(vertices)):
    deg = 0
    for t in triangles:
        if v in t:
            deg += 1
    counts.append(deg)
counts.sort(reverse=True)
# visit all vertices in desc order of degree
visited = set()
guards = []
p = set(range(len(polygon_points)))
v = 0
while visited != p:
    if v in visited:
        v += 1
        continue
    print(visited)
    bl = len(visited)
    counts.pop(0)
    print(visited, p)
    for t in triangles:
        print(t)
        if v not in t:
            continue
        for pt in t:     
            visited.add(pt)
    visited.add(v + 1)
    if v != 0:
        visited.add(v - 1)
    if len(visited) > bl + 1:
        guards.append(v)
    v += 1
    
for i in guards:
  circle = plt.Circle(polygon_points[i], 0.2, color='r')
  ax.add_patch(circle)
plt.show()