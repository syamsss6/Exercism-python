def parse_binary(binary):
 if set(binary) - set('01'):
   raise ValueError('invalid')
 else:
  return sum(int(binary) * 2**i for (i,binary) in enumerate(reversed(binary)))
