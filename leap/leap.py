def is_leap_year(year):
 if (year % 4 == 0 and (year % 400 ==0 or year % 100 !=0)):
  return

p=is_leap_year(1996)
print p
