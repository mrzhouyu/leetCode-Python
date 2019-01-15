# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 12:26
# @Author  : YuChou
# @Site    : 
# @File    : sumTwo.py
# @Software: PyCharm
def addTwoNumbers(l1,l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
#     sumList = []
#     carry = 0
#     while l1 or l2:
#         if l1 and l2:
#             sum = l1.pop() + l2.pop() +carry
#             carry = 0
#             if sum < 10:
#                 sumList.append(sum)
#             else:
#                 sumList.append(sum % 10)
#                 carry = 1# 一个列表元素只有一位 最多进一位
#
#         elif l1:
#             while l1:
#                 tup = l1.pop()
#                 if tup + carry < 10:
#                     carry = 0
#                     sumList.append(tup + carry)
#                 else:
#                     sumList.append((tup + carry) % 10)
#                     carry = 1
#                 if len(l1) == 0 :
#                     if carry != 0:
#                         sumList.append(carry)
#             break
#
#         elif l2:
#             while l2:
#                 tup = l2.pop()
#                 if tup + carry < 10:
#                     carry = 0
#                     sumList.append(tup + carry)
#                 else:
#                     sumList.append((tup + carry) % 10)
#                     carry = 1
#                 if len(l2) == 0 :
#                     if carry != 0:
#                         sumList.append(carry)
#             break
#     return sumList[::-1]
#
#
# addTwoNumbers([1,2,3],[4,5,6])


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        reNode = ListNode(0)
        carry = 0  # 进位
        re = reNode
        while l1 or l2:
            #
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            sum = carry + a + b
            carry = 1 if sum >= 10 else 0  # 两个Node 任意元素相加 进位不超过1
            re.next = ListNode(sum % 10)
            re = re.next

            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        if carry > 0:
            re.next = ListNode(1)
        return reNode.next

