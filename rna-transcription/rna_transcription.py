def to_rna(word):
 s=[]
 for i in word:
  if 'G' in i:
   s.append('C')
  elif 'C' in i:
   s.append('G')
  elif 'T' in i:
   s.append('A')
  elif 'A' in i:
   s.append('U')
  else:
   s.append(i)
 return ''.join(s)
 


