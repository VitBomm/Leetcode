# Definition for singly-linked list.
from typing import Optional
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_list = []
        l2_list = []
        while l1:
            l1_list.append(l1.val)
            l1 = l1.next
        while l2:
            l2_list.append(l2.val)
            l2 = l2.next
        l1_list.reverse()
        l2_list.reverse()
        number_str_1 = ""
        number_str_2 = ""
        for i in l1_list:
            number_str_1 += str(i)
        for i in l2_list:   
            number_str_2 += str(i)
        total = int(number_str_1) + int(number_str_2)
        total_str = str(total)
        total_str = total_str[::-1]
        dummy_head = ListNode(int(total_str[0]))
        current = dummy_head
        for digit in total_str[1:]:
            current.next = ListNode(int(digit))
            current = current.next
        return dummy_head