class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            if i == len(arr) - 1:
                arr[i] = -1
                break
            m = max(arr[i + 1 :])
            arr[i] = m
        return arr
