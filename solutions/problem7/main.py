import sys

def decimal_to_binary_recursive(n):
    if n == 0:
        return "0"
    
    def convert(num):
        if num == 0:
            return ""
        return convert(num // 2) + str(num % 2)
    
    return convert(n)

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
    
    result = decimal_to_binary_recursive(n)
    print(result)
    
  except (ValueError, IndexError):
    pass

if __name__ == "__main__":
    solve()
