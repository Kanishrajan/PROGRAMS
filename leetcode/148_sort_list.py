from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        a=[]
        while head!=None:
            a.append(head.val)
            head=head.next
        a.sort()
        head=temp
        i=0
        while head!=None:
            head.val=a[i]
            head=head.next
            i+=1
        head=temp
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
        [4,2,1,3],
        [-1,5,3,4,0],
        [1],
        [5,4,3,2,1],
        [2,2,2,2]
    ]

    sol = Solution()

    for arr in test_cases:
        head = create_list(arr)

        print("Original:")
        print_list(head)

        sorted_head = sol.sortList(head)

        print("Sorted:")
        print_list(sorted_head)
        print("-"*30)