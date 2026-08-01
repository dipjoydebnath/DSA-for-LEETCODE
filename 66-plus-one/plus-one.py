class Solution(object):
    def plusOne(self, digits):

        single_integer = int("".join(map(str, digits)))
        single_integer = single_integer + 1
        str(single_integer)
        result = list(map(int, (str(single_integer))))

        return result
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        