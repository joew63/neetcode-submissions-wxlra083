class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for index in range(len(s2) - len(s1) + 1):
            substring = s2[index : index + len(s1)]
            if sorted(substring) == sorted(s1):
                return True
        return False