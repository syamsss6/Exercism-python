def word_count(s):
 s=''.join(i if i.isalnum() else ' ' for i in s)
 wct={}
 for i in s.lower().split():
   wct[i] = wct.get(i, 0) + 1
 return wct



#print stri("car : carpet as java : javascript!!&@$%^&")
#print stri("one fish two fish red fish blue fish")
#print stri("testing 1 2 testing")
#print stri("wait for       it")
#print stri('rah rah ah ah ah\nroma roma ma\n'
#                       'ga ga oh la la\nwant your bad romance')
#print stri("hey,my_spacebar_is_broken.")
#print srti("")
