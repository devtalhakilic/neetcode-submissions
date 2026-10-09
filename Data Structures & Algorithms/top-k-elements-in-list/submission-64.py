class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = {}
        for i in range(len(nums)):
             if nums[i] not in output:
                 output[nums[i]] = 1
             else:
                 output[nums[i]] += 1
            
        sonuc = list(sorted(output, key=output.get, reverse=True))[:k]
        return sonuc
        