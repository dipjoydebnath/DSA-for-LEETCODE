class Solution(object):
    def addBinary(self, a, b):

        decimal_integer_a = int(a, 2)
        decimal_integer_b = int(b, 2)
        #   going to sum of the both integers
        sum_both_integers = (decimal_integer_a + decimal_integer_b)

            # converting the sum of integers into binary string    
        sum_both_integers_binarystr = bin(sum_both_integers)

        #   now going to remove the 0b here
        sum_both_integers_binarystr = bin(sum_both_integers)[2:]

        return sum_both_integers_binarystr



        """
        :type a: str
        :type b: str
        :rtype: str
        """
        