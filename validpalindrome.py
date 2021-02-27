def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s==s[::-1]
    
'''
isalnum() is used for alpha numeric values, first we are checking that the number in s
is alphanumeric or not then we are joining them without commas and other thing and then coonverting 
into lowercase and then checking if the reverse is equal to it or not
'''