def hey(what):

 if what.isupper():
   return 'Whoa, chill out!'
 if what.strip()  == '':
   return 'Fine. Be that way!'
 if what.endswith('?'):
   return 'Sure.'
 if what.endswith(' ')  and '?' in what:
   return 'Sure.'
 else:
   return 'Whatever.'

#print hey('What if we end with whitespace?   ')
#print ss("4?")
#print bob("ZOMG THE %^*@#$(*^ ZOMBIES ARE COMING!!11!!1!")



