def isYearLeap(year):
  if year % 4 == 0:
      if year % 100 == 0:
          if year % 400 == 0:
              return True
          else:
              return False
      else:
          return True
  else:
      return False

def daysInMonth(year, month):
  months =["Enero", "Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
  
  if months[month-1]=="Enero":
    return 31
  elif months[month-1]=="Febrero":
    if isYearLeap(year):
      return 29
    else:
      return 28
  elif months[month-1]=="Marzo":
    return 31
  elif months[month-1]=="Abril":
    return 30
  elif months[month-1]=="Mayo":
    return 31
  elif months[month-1]=="Junio":
    return 30
  elif months[month-1]=="Julio":
    return 31
  elif months[month-1]=="Agosto":
    return 31
  elif months[month-1]=="Septiembre":
    return 30
  elif months[month-1]=="Octubre":
    return 31
  elif months[month-1]=="Noviembre":
    return 30
  elif months[month-1]=="Diciembre":
    return 31
  else:
    return None


testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]

for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
