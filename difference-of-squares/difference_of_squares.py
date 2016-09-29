def square_of_sum(n):
 sm= n * (n + 1) / 2
 return sm**2
def sum_of_squares(n):
 return sum(n*n for n in range(n+1))

def difference(n):
 return square_of_sum(n) - sum_of_squares(n)

