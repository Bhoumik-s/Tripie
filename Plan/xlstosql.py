import numpy as np
import xlrd
import os
from .models import Mumbai_db

def makedb():
	module_dir = os.path.dirname(__file__)  # get current directory
	file_path = os.path.join(module_dir, 'Mumbai.xlsx')
	book = xlrd.open_workbook(file_path)
	worksheet = book.sheet_by_index(0)

	for i in range (worksheet.nrows-1):
		print i
		place = Mumbai_db(
						placeId = worksheet.cell(i+1,0).value,
						latitude = worksheet.cell(i+1,1).value,
						longitude = worksheet.cell(i+1,2).value,
						defaultHappiness = worksheet.cell(i+1,3).value,
						sightSeeing = worksheet.cell(i+1,4).value,
						religious = worksheet.cell(i+1,5).value,
						amusement = worksheet.cell(i+1,6).value,
						nightLife = worksheet.cell(i+1,7).value,
						shopping = worksheet.cell(i+1,8).value,
						cost = worksheet.cell(i+1,9).value,
						openTime = worksheet.cell(i+1,10).value,
						dueTime = worksheet.cell(i+1,11).value,
						serviceTime = worksheet.cell(i+1,12).value,
						name = worksheet.cell(i+1,13).value,
						timings = worksheet.cell(i+1,14).value,
						description = worksheet.cell(i+1,15).value,
						comment1 = worksheet.cell(i+1,16).value,
						comment2 = worksheet.cell(i+1,17).value,
						)
		place.save()

	return 0
