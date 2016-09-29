def distance(wd1,wd2):
 p=list(wd1)
 q=list(wd2)
 count=0
 for i in range(len(wd1)):
  if q[i] != p[i]:
   count+=1 
 return count


#distance('A','A')
#distance('A','G')
#distance('AG','CT')
#distance('AT', 'CT')
#distance('GGACG', 'GGTCG')
#distance('GATACA', 'GCATAA')
#distance('GGACGGATTCTG', 'AGGACGGATTCT')
