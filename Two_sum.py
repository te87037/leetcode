"""
author Rex.lin
easy level
"""
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictx = {}
        for i,n in enumerate(nums,0):
            rest = target - n
            if rest in dictx:
                return dictx[rest],i
            dictx[n] = i
