# Definition for singly-linked list
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        prev=None
        curr=head
        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        return prev


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
        [1,2],
        [1],
        []
    ]

    sol = Solution()

    for arr in test_cases:
        head = create_list(arr)

        print("Original List:")
        print_list(head)

        reversed_head = sol.reverseList(head)

        print("Reversed List:")
        print_list(reversed_head)

        print("-"*40)