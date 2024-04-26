import math

def cal_distances(point1, point2):
    distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2 + (point2[2] - point1[2])**2)
    return distance

def my_map(func, list1, list2):
    return [func(point1, point2) for point1, point2 in zip(list1, list2)]

points1 = [(1.0, 1.0, 1.0), (2.0, 2.0, 2.0), (3.0, 3.0, 3.0)]
points2 = [(4.0, 4.0, 4.0), (5.0, 5.0, 5.0), (5.0, 5.0, 5.0), (6.0, 6.0, 6.0)]

distances = my_map(cal_distances, points1, points2)

print(distances)
