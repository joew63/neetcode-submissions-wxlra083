class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        if not strs:
            return "[]"
        for string in strs:
            result = result + string + "- "
        return result[0:len(result) - 2]

    def decode(self, s: str) -> List[str]:
        if s == "[]":
            return list()
        x = s.split("- ")
        return x