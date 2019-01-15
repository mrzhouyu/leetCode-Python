# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 11:30
# @Author  : YuChou
# @Site    : 
# @File    : Sums.py
# @Software: PyCharm

class Solution:

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # O(n^2)
        for index, value in enumerate(nums[:-1]):
            for index1, value1 in enumerate(nums[index+1:]):
                if value+value1 == target:
                    return [index, index1+index+1]