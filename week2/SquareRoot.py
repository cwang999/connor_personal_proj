class SqrtCalculator:
  def __init__(self):
    self.sqrts = []
  
  def __call__(self, n):
    if n < 0:
      raise Exception("No negative numbers")
    
    if n >= len(self.sqrts):
      for x in range(len(self.sqrts), n + 1):
        self.sqrts.append(x ** 0.5)
        
    return self.sqrts[n]

def sqrt(x):
  return x ** 0.5

def tester():
  sqrt_calc = SqrtCalculator()
  while True:
    x = int(input("Enter a number: "))
    print(f"Imperative says the square root of {x} is: {sqrt(x)}")
    print(f"OOP says the square root of {x} is {sqrt_calc(x)}")

tester()

