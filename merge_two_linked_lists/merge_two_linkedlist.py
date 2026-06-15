from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if(list1 == None):
            return list2

        elif list2 == None:
            return list1

        else:
            merge_list = ListNode()
            head = merge_list

            while(list1 != None and list2 != None):

                if(list1.val < list2.val):

                    merge_list.val = list1.val
                    merge_list.next = ListNode()

                    merge_list = merge_list.next
                    list1 = list1.next

                else:

                    merge_list.val = list2.val
                    merge_list.next = ListNode()

                    merge_list = merge_list.next
                    list2 = list2.next

            if(list1 == None):

                merge_list.val = list2.val
                merge_list.next = list2.next

            else:

                merge_list.val = list1.val
                merge_list.next = list1.next

            return head


# Helper function to create linked list
def create_list(arr):

    dummy = ListNode()
    current = dummy

    for num in arr:
        current.next = ListNode(num)
        current = current.next

    return dummy.next


# Helper function to print linked list
def print_list(head):

    while head:
        print(head.val, end=" -> ")
        head = head.next

    print("None")


# Test
list1 = create_list([1, 2, 4])
list2 = create_list([1, 3, 4])
print(list1)
print(list1.val)
print(list1.next)


# sol = Solution()

# result = sol.mergeTwoLists(list1, list2)

# print_list(result)