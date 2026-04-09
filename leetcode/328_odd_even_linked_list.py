from typing import Optional

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None: return head
        odd=ListNode(0)
        odd_ptr=odd
        even=ListNode(0)
        even_ptr=even
        idx=1
        while head!=None:
            if idx%2==0:
                even_ptr.next=head
                even_ptr=even_ptr.next
            else:
                odd_ptr.next=head
                odd_ptr=odd_ptr.next
            head=head.next
            idx+=1
        even_ptr.next=None
        odd_ptr.next=even.next
        return odd.next


# helper function to create linked list
def create_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for v in arr[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


# helper function to print linked list
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


if __name__ == "__main__":

    test_cases = [
        [1,2,3,4,5],
        [2,1,3,5,6,4,7],
        [1],
        [1,2]
    ]

    sol = Solution()

    for arr in test_cases:
        head = create_list(arr)

        print("Original List:")
        print_list(head)

        head = sol.oddEvenList(head)

        print("Odd-Even Rearranged:")
        print_list(head)

        print("-"*40)