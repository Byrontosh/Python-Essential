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


def dayOfYear(year, month, day):
  if ( 1 <= month <= 12 ) and (1 <= day <=31) and (1<=len(str(year))<=4):
    if isYearLeap(year) and daysInMonth(year,month) == day:
      return f'Days of the year {year} is 366, because it\'s a leap year'
    elif isYearLeap(year) and daysInMonth(year,month) != day:
      return None
    else:
      return f'Days of the year {year} is 365, because isn\'t a leap year'
  else:
    return None


print(dayOfYear(2000, 2, 29))
print()
print(dayOfYear(2023, 12, 31))
print()
print(dayOfYear(2012, 2, 29))
print()
print(dayOfYear(2012, 2, 28))





