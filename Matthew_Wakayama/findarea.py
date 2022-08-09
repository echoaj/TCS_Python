

# You have two squares and your goal is find the area of non-intersection area
# Square one
x1 = -10
y1 = 10
x2 = 6
y2 = 4

# Square two
a1 = -2
b1 = 8
a2 = 12
b2 = 0

inner_x1 = max(x1, a1)
inner_y1 = min(y1, b1)
inner_x2 = min(x2, a2)
inner_y2 = max(y2, b2)

print(inner_x1, inner_y1, inner_x2, inner_y2)

# Calculate the area
area = abs((inner_x2 - inner_x1) * (inner_y2 - inner_y1))
print(area)

