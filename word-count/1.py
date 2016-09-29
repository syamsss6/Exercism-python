from collections import Counter
def word_count(text):
 def removing(string):
   return string.lower() if string.isalnum() else ' '

 p=''.join(i for i in text if i.isalnum())
 #print p.split()
 return Counter(p.split())




#print word_count("olly olly in come free")
print word_count('car : carpet as java : javascript!!&@$%^&')


