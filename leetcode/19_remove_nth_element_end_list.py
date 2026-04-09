# Definition for singly-linked list
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        fast=head
        slow=head
        for _ in range(n):
            fast=fast.next
        if not fast:
            return head.next
        while fast.next:
            fast,slow=fast.next, slow.next
        slow.next=slow.next.next
        return head


# helper to create linked list
def create_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for v in arr[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


# helper to print linked list
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


if __name__ == "__main__":

    test_cases = [
        ([1,2,3,4,5],2),
        ([1,2,3,4,5],1),
        ([1,2],1),
        ([1],1)
    ]

    sol = Solution()

    for arr,n in test_cases:
        head = create_list(arr)

        print("Original List:")
        print_list(head)

        head = sol.removeNthFromEnd(head,n)

        print("After Removing",n,"th Node From End:")
        print_list(head)

        print("-"*40)