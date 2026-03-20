import sys

def is_palindrome_recursive(s):
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome_recursive(s[1:-1])
    else:
        return False

def solve():
  """
  Reads input from stdin, solves the problem, and prints the output.
  """
  try:
    # --- Input reading ---
    s = sys.stdin.readline().strip()
    
    # --- Solution ---
    # The following variables are available:
    # s: str
    
    result = is_palindrome_recursive(s)
    print(result)
    
  except (ValueError, IndexError):
    pass

if __name__ == "__main__":
    solve()
