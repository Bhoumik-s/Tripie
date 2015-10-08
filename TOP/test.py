from main import plan

x=plan("Mumbai",2,540,1440,500)

file="Mumbai.xlsx"
data=read(file)
name=data[1]
points=data[0]
#distance_mat(points[0:-1,:2])
