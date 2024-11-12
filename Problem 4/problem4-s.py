class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, n = 0, len(s)

        # Helper function to parse optional sign
        def parseSign(index):
            if index < n and (s[index] == '+' or s[index] == '-'):
                return index + 1
            return index

        # Helper function to parse a sequence of digits
        def parseDigits(index):
            start = index
            while index < n and s[index].isdigit():
                index += 1
            return index, index > start  # Return new index and whether we found at least one digit

        # Parse the optional sign
        i = parseSign(i)

        # Parse the integer or decimal part
        i, isNumeric = parseDigits(i)

        # Check for a decimal point and digits after it
        if i < n and s[i] == '.':
            i += 1
            i, hasDecimalDigits = parseDigits(i)
            isNumeric = hasDecimalDigits or isNumeric  # Valid if there's a digit before or after the dot

        # Parse the exponent part if present
        if isNumeric and i < n and (s[i] == 'e' or s[i] == 'E'):
            i += 1
            i = parseSign(i)  # Optional sign in exponent
            i, hasExponentDigits = parseDigits(i)
            if not hasExponentDigits:  # Exponent must have digits
                return False

        # Check if we've processed all characters and if it was a valid number
        return isNumeric and i == n
