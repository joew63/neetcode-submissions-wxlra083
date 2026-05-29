class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for num in range(len(temperatures)):
            count = 1
            index = 1
            if num + index == len(temperatures):
                result.append(0)
            else:
                while temperatures[num] >= temperatures[num + index]:
                    count += 1
                    index += 1
                    if num + index == len(temperatures):
                        count = 0
                        break
                result.append(count)
        return result