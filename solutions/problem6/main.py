import sys

def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

def solve():
  """
  Reads input from stdin, solves the problem, and prints the output.
  """
  try:
    # --- Input reading ---
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    target = int(sys.stdin.readline())
    
    # --- Solution ---
    # The following variables are available:
    # n: int
    # nums: list of ints
    # target: int
    
    result = binary_search_recursive(nums, target, 0, n - 1)
    print(result)
    
  except (ValueError, IndexError):
    pass

if __name__ == "__main__":
    solve()
