import sys

def find_subsets_recursive(elements, index, current_subset, all_subsets):
    if index == len(elements):
        all_subsets.append(list(current_subset))
        return
    
    # Exclude current element
    find_subsets_recursive(elements, index + 1, current_subset, all_subsets)
    
    # Include current element
    current_subset.append(elements[index])
    find_subsets_recursive(elements, index + 1, current_subset, all_subsets)
    current_subset.pop() # Backtrack

def solve():
  """
  Reads input from stdin, solves the problem, and prints the output.
  """
  try:
    # --- Input reading ---
    n = int(sys.stdin.readline())
    elements = sys.stdin.readline().split()
    
    # --- Solution ---
    # The following variables are available:
    # n: int
    # elements: list of str
    
    all_subsets = []
    find_subsets_recursive(elements, 0, [], all_subsets)
    
    # Sort for deterministic output, as specified in problem description
    # Sort by length, then lexicographically for elements within subset
    all_subsets.sort(key=lambda x: ' '.join(sorted(x)))

    for subset in all_subsets:
        print(' '.join(subset))
    
  except (ValueError, IndexError):
    pass

if __name__ == "__main__":
    solve()
