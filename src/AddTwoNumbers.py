# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None or l2 is None:
            return None

        num1 = self._getRevertedNumber(l1)
        num2 = self._getRevertedNumber(l2)

        total = num1 + num2                 # an int, e.g. 342 + 465 = 807
        return self._buildList(total)       # convert the int back into a ListNode chain

    def _getRevertedNumber(self, listNode: Optional[ListNode]) -> Optional[int]:
        result = 0
        place = 1
        while listNode is not None:
            result += listNode.val * place
            place *= 10
            listNode = listNode.next
        return result

    def _buildList(self, number: int) -> Optional[ListNode]:
        # Build a linked list of the digits, least-significant first (the format
        # this problem uses). dummy head avoids a special case for the first node.
        dummy = ListNode()
        current = dummy
        while True:                         # do-while: always make >=1 node (handles number == 0)
            current.next = ListNode(number % 10)   # % 10  -> last digit
            current = current.next
            number //= 10                          # // 10 -> drop the last digit
            if number == 0:
                break
        return dummy.next


# --- tests ---
def to_list(node):
    """ListNode chain -> Python list, so we can compare/print easily."""
    out = []
    while node is not None:
        out.append(node.val)
        node = node.next
    return out


def from_list(values):
    """Python list -> ListNode chain."""
    dummy = ListNode()
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next


sol = Solution()
test_cases = [
    ([2, 4, 3], [5, 6, 4], [7, 0, 8]),   # 342 + 465 = 807
    ([0], [0], [0]),                     # 0 + 0 = 0  (edge: single zero)
    ([9, 9], [1], [0, 0, 1]),            # 99 + 1 = 100  (carry ripples, list grows)
]

for a, b, expected in test_cases:
    result = to_list(sol.addTwoNumbers(from_list(a), from_list(b)))
    assert result == expected, f"FAIL: {a} + {b} = {result}, expected {expected}"
    print(f"PASS  {a} + {b} -> {result}")

print("All tests passed.")
