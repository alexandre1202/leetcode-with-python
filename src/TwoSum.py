# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
#
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]

def twoSum(n, target):
    seen = {}
    for i, num in enumerate(n):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None

# --- tests ---
# A list of (nums, target, expected) tuples. Each tuple is a scenario.
# This is like a parameterized JUnit test: one data row per case.
test_cases = [
    ([2, 7, 11, 15], 9, [0, 1]),   # example 1 — partner found later
    ([3, 2, 4], 6, [1, 2]),        # example 2 — answer isn't the first pair
    ([3, 3], 6, [0, 1]),           # example 3 — same value twice, different indices
    ([1, 2, 3], 100, None),        # no pair sums to target -> we return None
    ([0, 4, 3, 0], 0, [0, 3]),     # zeros: 0 + 0 == 0
]

for nums, target, expected in test_cases:
    result = twoSum(nums, target)
    # assert == JUnit's assertEquals; it raises AssertionError if the check fails.
    # The text after the comma is the message shown when it fails.
    assert result == expected, f"FAIL: twoSum({nums}, {target}) = {result}, expected {expected}"
    print(f"PASS  twoSum({nums}, {target}) -> {result}")

print("All tests passed.")

