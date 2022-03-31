class FactorialCalculator:
  def __init__(self):
    self.factorials = [1]
  
  def __call__(self, n):
    if n < 0:
      raise Exception("No negative numbers")
    elif n < len(self.factorials):
      return self.factorials[n]  
    else:   
      x = len(self.factorials) - 1
      result = self.factorials[x]

      while x < n:
        x += 1
        result *= x 
        self.factorials.append(result)
        
      return result

def tester():
  fact = FactorialCalculator()
  while True:
    x = int(input("Enter a number: "))
    print(f"The factorial of {x} is: {fact(x)}")

