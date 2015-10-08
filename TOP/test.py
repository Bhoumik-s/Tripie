from read_data import read
from Google_distance_API import duration_mat

file="Mumbai.xlsx"
data=read(file)
name=data[1]
points=data[0]
#distance_mat(points[0:-1,:2])
