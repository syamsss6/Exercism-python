
PLAIN = 'abcdefghijklmnopqrstuvwxyz'
CIPHER = 'zyxwvutsrqponmlkjihgfedcba'
def encode(plaintext):
 s=''
 l=[]
 plain=plaintext.lower()
 word=[plain[i] for i in range(len(plain))]
 for i in word:
   if i in PLAIN:
     l.append(PLAIN.index(i))

 for i in l:
  s=s+CIPHER[i]
 return s

#print encode("Truth is fiction.")

def decode(cipher):
 
 l=[]
 s=''
 word=[cipher[i] for i in range(len(cipher))]
 for i in word:
  if i in CIPHER:
   l.append(CIPHER.index(i))
 for i in l:
  s=s+PLAIN[i]
 return s
#print decode('vcvix rhn')
