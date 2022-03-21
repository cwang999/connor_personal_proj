def fib_seq(n):
    if n == 0:
        print(0)
        return
        
    if n < 0:
        raise Exception("Can't use negative n")
    
    def helper(idx, curr, prev):
        print(curr)
        if idx == n:
            return
        helper(idx + 1, curr + prev, curr)
    
    print(0)
    helper(1, 1, 0)
        
def print_fib(n):
    try:
        fib_seq(n)
    except:
        print("Invalid n")
        
while True:
  f = input('Which Fibonacci number to find? (small number): ')
  print(fib_seq(int(f)))
