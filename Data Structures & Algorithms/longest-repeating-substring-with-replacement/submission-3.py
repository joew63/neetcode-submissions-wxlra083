class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        for target_char in set(s):
            count = 0
            left = 0
            for right in range(len(s)):
                if s[right] != target_char:
                    count += 1
                while count > k:
                    if s[left] != target_char:
                        count -= 1
                    left += 1
                longest = max(longest, right - left + 1)
        return longest