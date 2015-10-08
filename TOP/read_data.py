import numpy as np
import xlrd
import os

def read(file):

    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, file)
    book = xlrd.open_workbook(file_path)
    worksheet = book.sheet_by_index(0)
    data=np.zeros((worksheet.nrows-1,worksheet.ncols-1))
    name=[]
    for i in range (worksheet.nrows-1):
        for j in range (worksheet.ncols-1):
            data[i][j]=worksheet.cell(i+1,j+1).value
        name.append(str(worksheet.cell(i+1,0).value))
    return (data,name)

def find_segments(points):
    distance=np.zeros((points.shape[0],points.shape[0]))
    for i in range(points.shape[0]):
        for j in range (i+1, points.shape[0]):
            distance[i][j]=pow(pow(points[i][0]-points[j][0],2)+pow(points[i][1]-points[j][1],2),0.5)
            distance[j][i]=distance[i][j]
    return distance

