import datetime

startDate = datetime.datetime.strptime('12122012', '%d%m%Y')
endDate = datetime.datetime.strptime('16122012', '%d%m%Y')
Days = abs((endDate - startDate).days)
print Days