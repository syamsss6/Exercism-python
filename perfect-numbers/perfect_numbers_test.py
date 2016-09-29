
def is_perfect(x):
 s=[]
 i=1
 while i<x:
    if x%i == 0:
       s.append(i)
    i=i+1
 
 return sum(s) == x

   


#print is_perfect(6)
#print is_perfect(8)
#print is_perfect(28)
#print is_perfect(20)
#print is_perfect(42)
#print is_perfect(496)
#print is_perfect(945)
#print is_perfect(8128)
#print is_perfect(33550336)
#print is_perfect(8589869056)
#print is_perfect(137438691328)
