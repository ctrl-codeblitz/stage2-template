# Problem 9 — All Subsets

Given a set of distinct elements, output all subsets using recursion. Include or exclude each element and recurse.

## Input Format

- First line: n (number of elements)
- Second line: n space-separated elements (single characters or words)

## Output Format

2^n lines, each containing one subset (space-separated elements). Empty set represented as an empty line. Any deterministic order is acceptable (e.g., lexicographic).

## Example

Input:
- 2
- a b

Output:

- a
- a b
- b

## Constraints

- Elements are distinct
- n ≥ 1

## Expected Complexity

- Time: O(2^n)
- Space: O(n) recursion stack
