# Problem Specification

  Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Problem background

  Palindromic numbers are different in various base cases. This program can consider a possible base and determine whether the number is a palindrome in this base.

# Propsed algorithm

  Get all the "digits" in this base from the number inside a list

  Loop through the list until the middle is reached and compare the digits from theith back position of the list to ith front position of the list

  If one of the comparsions fails return false

  return true

## Time Complexity

   O(n)

# Languages used

+ Python

# Test cases

## Required Tests

+ Test known palindromic numbers in various bases
+ Test known non-palindromic numbers in various bases

## Implemented tests
### Python

  - Palindromic number generator was implemented to test for known palindromic numbers

# Time complexity results

  Put the time complexity results here
