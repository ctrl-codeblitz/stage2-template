import sys

def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)

def solve():
  """
  Reads input from stdin, solves the problem, and prints the output.
  """
  try:
    # --- Input reading ---
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
    
    # --- Solution ---
    # The following variables are available:
    # a: int
    # b: int
    
    result = gcd_recursive(a, b)
    print(result)
    
  except (ValueError, IndexError):
    pass

if __name__ == "__main__":
    solve()
