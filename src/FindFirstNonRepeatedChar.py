from typing import List

class Solution:
    def findFirstNonRepeated(self, inputChars: str) -> str:
        countedChars = {}
        for ic in inputChars:
            countedChars[ic] = countedChars.get(ic, 0) + 1
        for ic in countedChars:
            if countedChars[ic] == 1:
                return ic
        return ""

test_cases = [
    ("aaabbcccdeeefffffxxz", "d"),
    ("aaaabccccddeeefffffxxz", "b"),
]

solution = Solution()
for t in test_cases:
    print(t[0])
    print(solution.findFirstNonRepeated(t[0]))
    print(t[1])
    assert solution.findFirstNonRepeated(t[0]) == t[1], "Values must be equal"
