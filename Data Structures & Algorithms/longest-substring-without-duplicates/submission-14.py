class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        curr = 0
        last_seen = {}

        for i, char in enumerate(s):
            if char in last_seen and last_seen[char] >= curr:
                curr = last_seen[char] + 1
            last_seen[char] = i
            longest = max(longest, i - curr + 1)

        return longest