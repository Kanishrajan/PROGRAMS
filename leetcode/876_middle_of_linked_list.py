# Definition for singly-linked list
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def middleNode(self, head):
        a = []
        
        while head:
            a.append(head)
            head = head.next
        
        return a[len(a)//2]


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
        [1,2,3,4,5],
        [1,2,3,4,5,6],
        [1],
        [1,2]
    ]

    sol = Solution()

    for arr in test_cases:
        head = create_list(arr)

        print("Original List:")
        print_list(head)

        mid = sol.middleNode(head)

        print("Middle Node onwards:")
        print_list(mid)

        print("-"*40)