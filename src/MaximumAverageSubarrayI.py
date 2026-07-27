# You are given an integer array nums consisting of n elements, and an integer k.
#
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
#
#
#
# Example 1:
#
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        index = 0
        sum = 0
        tempAverage = 0
        if len(nums) == 1:
            return nums[0]

        while index < k:
            sum += nums[index]
            index += 1
        tempAverage += sum / k
        average = tempAverage

        while index < len(nums):
            sum = sum - nums[index - k] + nums[index]
            index += 1
            tempAverage = sum / k
            average = max(tempAverage, average)

        return average


# --- tests ---
sol = Solution()
test_cases = [
    ([1, 12, -5, -6, 50, 3], 4, 12.75),   # example 1
    ([5], 1, 5.0),                        # single element
    ([0, 4, 0, 3, 2], 1, 4.0),            # k == 1 -> just the max element
    ([-1, -12, -5, -6, -50, -3], 2, -5.5),  # ALL negative -> best avg is [-5,-6]/2
]

for nums, k, expected in test_cases:
    result = sol.findMaxAverage(nums, k)
    # abs(diff) < 1e-5 == the problem's "calculation error < 10^-5" rule.
    # (Never compare floats with ==; use a tolerance.)
    assert abs(result - expected) < 1e-5, \
        f"FAIL: findMaxAverage({nums}, {k}) = {result}, expected {expected}"
    print(f"PASS  findMaxAverage({nums}, {k}) -> {result}")

print("All tests passed.")

