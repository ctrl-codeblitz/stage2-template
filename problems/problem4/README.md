# Problem 4 — Power (x^n)

Given base x and non-negative integer exponent n, compute x^n recursively. 

## Input Format

- Two integers x and n, separated by whitespace
- They may appear on the same line or on separate lines

## Output Format

A single integer: x^n

## Example

Input:
2 10

Output:
1024

## Constraints

- x and n are integers with n non-negative
- Result fits in 64-bit signed range

## Expected Complexity

- Time: O(log n) with squaring optimization
- Space: O(log n) recursion stack
