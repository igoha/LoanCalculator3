import math

edge_lenght = int(input())
area = round(2 * math.sqrt(3) * math.pow(edge_lenght, 2), 2)
volume = round((1 / 3) * math.sqrt(2) * math.pow(edge_lenght, 3), 2)
print(area, "", volume)
