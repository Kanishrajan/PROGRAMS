# Node Class
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class Solution:
    def removeDuplicates(self, head):
        curr = head

        while curr and curr.next:
            if curr.data == curr.next.data:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head


# Helper function to create linked list
def create_list(arr):
    if not arr:
        return None

    head = Node(arr[0])
    curr = head

    for x in arr[1:]:
        curr.next = Node(x)
        curr = curr.next

    return head


# Helper function to print linked list
def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


if __name__ == "__main__":

    test_cases = [
        [1,1,2,3,3],
        [1,1,1,1],
        [1,2,3,4],
        [2,2,3,3,4,4,5],
        [5]
    ]

    sol = Solution()

    for arr in test_cases:
        head = create_list(arr)

        print("Original List:")
        print_list(head)

        head = sol.removeDuplicates(head)

        print("After Removing Duplicates:")
        print_list(head)

        print("-" * 45)
