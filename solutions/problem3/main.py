import sys

def sum_digits_recursive(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_digits_recursive(n // 10)

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
    
    result = sum_digits_recursive(n)
    print(result)
    
  except (ValueError, IndexError):
    pass

if __name__ == "__main__":
    solve()
