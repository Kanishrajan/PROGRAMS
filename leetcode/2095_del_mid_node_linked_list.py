from typing import Optional

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next
        return head


# Helper function to create linked list
def create_list(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    curr = head

    for x in arr[1:]:
        curr.next = ListNode(x)
        curr = curr.next

    return head


# Helper function to print linked list
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


if __name__ == "__main__":

    test_cases = [
        [1,3,4,7,1,2,6],
        [1,2,3,4],
        [2,1],
        [1]
    ]

    sol = Solution()

    for arr in test_cases:
        head = create_list(arr)

        print("Original List:")
        print_list(head)

        new_head = sol.deleteMiddle(head)

        print("After Deleting Middle:")
        print_list(new_head)

        print("-" * 45)