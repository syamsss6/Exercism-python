def prime_factors(n):
 fact=[]
 i=2
 while i <= n:
   if n%i == 0:
     fact.append(i)
     n=n/i
   else:
      i=i+1
     

 return fact
