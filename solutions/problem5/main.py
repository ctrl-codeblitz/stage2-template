import sys

def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def solve():
  """
  Reads input from stdin, solves the problem, and prints the output.
  """
  try:
    # --- Input reading ---
    n = int(sys.stdin.readline())
    
    # --- Solution ---
    # The following variables are available:
    # n: int
    
    result = fibonacci_recursive(n)
    print(result)
    
  except (ValueError, IndexError):
    pass

if __name__ == "__main__":
    solve()
