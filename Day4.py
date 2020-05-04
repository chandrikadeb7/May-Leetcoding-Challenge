class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num ^ int(bin(num)[2:].replace("0","1"),2)
