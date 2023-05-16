class Point:
    color='red'
    circle=2

Point.color='black'

print(Point.__dict__)

a=Point()
a.color='oo'

print(a.__dict__)

b=Point()

print(b.color)
print(a.color)