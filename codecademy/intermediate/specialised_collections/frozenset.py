"""
Frozenset is a class that creates an immutable version of the set class.

This means that once a frozenset is created, it cannot be changed.
"""

# Example 1

# Create a frozenset
frozen_set = frozenset(["apple", "orange", "banana", "apple", "apple", "orange"])
print(frozen_set) # will print frozenset({'orange', 'apple', 'banana'})

# Example 2

# Create an empty frozenset
empty_frozen_set = frozenset()
print(empty_frozen_set) # will print frozenset()

