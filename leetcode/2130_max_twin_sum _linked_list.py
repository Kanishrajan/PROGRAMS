from typing import Optional

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        a=[]
        while head:
            a.append(head.val)
            head=head.next

        ans=0
        for i in range(len(a)//2):
            ans=max(ans,a[i]+a[len(a)-i-1])

        return ans


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


if __name__ == "__main__":

    test_cases = [
        [5,4,2,1],
        [4,2,2,3],
        [1,100000],
        [1,2,3,4,5,6],
        [10,20,30,40]
    ]

    sol = Solution()

    for arr in test_cases:
        head = create_list(arr)

        print("Linked List:", arr)
        print("Maximum Twin Sum:", sol.pairSum(head))
        print("-" * 45)