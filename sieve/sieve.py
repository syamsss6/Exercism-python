def sieve(n):
 limit=n+1
 p=[i for i in range(2,limit)]
 for i in p:
  fact=range(i,limit,i)
  for j in fact[1:]:
    if j in p:
      p.remove(j)
   
 return p


print sieve(1000)
