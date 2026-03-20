import sys

def find_min_max_recursive(arr, low, high):
    if low == high:
        return arr[low], arr[low]
    
    if high == low + 1:
        return (arr[low], arr[high]) if arr[low] < arr[high] else (arr[high], arr[low])
    
    mid = (low + high) // 2
    min1, max1 = find_min_max_recursive(arr, low, mid)
    min2, max2 = find_min_max_recursive(arr, mid + 1, high)
    
    return min(min1, min2), max(max1, max2)

def solve():
  """
  Reads input from stdin, solves the problem, and prints the output.
  """
  try:
    # --- Input reading ---
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    
    # --- Solution ---
    # The following variables are available:
    # n: int
    # nums: list of ints
    
    if n == 0:
        print("No elements in array") # Or handle as per problem spec for empty array
    else:
        min_val, max_val = find_min_max_recursive(nums, 0, n - 1)
        print(min_val, max_val)
    
  except (ValueError, IndexError):
    pass

if __name__ == "__main__":
    solve()
