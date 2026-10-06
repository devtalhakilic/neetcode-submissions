class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        gorulenler = set()
        sayi = len(nums)
        
        for i in range(sayi):
            if nums[i] in gorulenler:
                return True
            else:
                gorulenler.add(nums[i])
        return False

