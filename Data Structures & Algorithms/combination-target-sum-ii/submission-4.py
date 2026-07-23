class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = list()
        candidates.sort()
        self.loop(candidates, target, 0, 0, list(), result)
        return result

    def loop(self, candidates, target, current, index, so_far, result):
        if target == current:
            result.append(list(so_far))
            return
        if current < target:
            for n in range(index, len(candidates)):
                if n > index and candidates[n] == candidates[n-1]:
                    continue
                so_far.append(candidates[n])
                self.loop(candidates, target, current + candidates[n], n + 1, so_far, result)
                so_far.pop()
        return