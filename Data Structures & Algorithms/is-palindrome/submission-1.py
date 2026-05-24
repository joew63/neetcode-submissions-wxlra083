class Solution:
    def isPalindrome(self, s: str) -> bool:
        fixed_string = ''.join(filter(str.isalnum, s)).lower()
        # fixed_string.lower()
        print(fixed_string)
        for index in range(len(fixed_string)):
            if index >= len(fixed_string) / 2:
                return True
            if fixed_string[index] != fixed_string[len(fixed_string) - 1 - index]:
                return False
        return True