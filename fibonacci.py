import sys 
def fibonacci_number(n):
  try: 
    if n == 0 or n == 1:
      return n
    else:
      return fibonacci_number(n - 1) + fibonacci_number(n - 2)
  except:
    sys.exit("No negative numbers! Fool.")
while True:
  f = input('Which Fibonacci number to find? (small number): ')
  print(fibonacci_number(int(f)))
