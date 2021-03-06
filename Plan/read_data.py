import numpy as np
import xlrd
import os

def ReadData(file):

    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, file)
    book = xlrd.open_workbook(file_path)
    worksheet = book.sheet_by_index(0)
    data=np.zeros((worksheet.nrows-1,worksheet.ncols-1))
    name=[]
    for i in range (worksheet.nrows-1):
        for j in range (13):
            data[i][j]=worksheet.cell(i+1,j).value
    return data


def ReadDurations(file):
    
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, file)
    book = xlrd.open_workbook(file_path)
    worksheet = book.sheet_by_index(0)
    durations=np.zeros((worksheet.nrows,worksheet.ncols))
    name=[]
    for i in range (worksheet.nrows):
        for j in range (worksheet.ncols):
            durations[i][j]=worksheet.cell(i,j).value
    return durations
