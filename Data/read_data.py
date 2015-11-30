import numpy as np
import xlrd
import os

def read(file):

    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, file)
    book = xlrd.open_workbook(file_path)
    worksheet = book.sheet_by_index(0)
    data=np.zeros((worksheet.nrows-1,2))
    for i in range (worksheet.nrows-1):
        for j in range (2):
            data[i][j]=worksheet.cell(i+1,j+1).value
    return (data)

