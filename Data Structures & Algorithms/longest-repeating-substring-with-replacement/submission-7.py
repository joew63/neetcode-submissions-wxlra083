class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        left = 0
        count = collections.defaultdict(int)
        max_freq = 0

        for right in range(len(s)):
            count[s[right]] += 1
            max_freq = max(max_freq, count[s[right]])
            
            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            
            
            longest = max(longest, right - left + 1)
        return longest