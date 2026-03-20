import sys

def power_recursive(x, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        half_power = power_recursive(x, n // 2)
        return half_power * half_power
    else:
        return x * power_recursive(x, n - 1)

def solve():
  """
  Reads input from stdin, solves the problem, and prints the output.
  """
  try:
    # --- Input reading ---
    x = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    
    # --- Solution ---
    # The following variables are available:
    # x: int
    # n: int
    
    result = power_recursive(x, n)
    print(result)
    
  except (ValueError, IndexError):
    pass

if __name__ == "__main__":
    solve()
