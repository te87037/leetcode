"""
author Rex.lin
easy level
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            x = abs(x)
            x = str(x)
            x = '-{}'.format(str(x)[::-1])
            x = int(x)
            if x< -(1 << 31) or x > (1 << 31) - 1:
                return 0
            else:
                return x
        elif x < -(1 << 31) or x > (1 << 31) - 1:
            return 0
        else:
            x = str(x)
            x = str(x)[::-1]
            x = int(x)
            if x< -(1 << 31) or x > (1 << 31) - 1:
                return 0
            else:
                return x
