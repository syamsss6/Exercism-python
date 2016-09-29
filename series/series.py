def slices(series,n):
 numbers = [int(digit) for digit in series]
 if 1 <= n <= len(numbers):
   return [numbers[i:i+n] for i in range(len(numbers) - n + 1)]
       

 else:
  raise ValueError("Invalid slice length for this series")


