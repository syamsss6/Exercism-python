def sum_of_multiples(max,num):
 result = set()
 for i in num:
  if i:
    for j in range(i,max,i):
      result.add(j)
 return sum(result)


#print sum_of_multiples(20,[7,13,17])
