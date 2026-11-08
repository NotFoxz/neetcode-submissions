
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequentElements = {}
        
        for x in nums:
            if x not in frequentElements:
                frequentElements[x] = 1
            else:
                frequentElements[x] += 1
        
        bucket = [[] for i in range(len(nums) + 1)]

        for num, cou in frequentElements.items():
            bucket[cou].append(num)

        result = []

        for i in range(len(bucket) - 1, 0 ,-1):
            for num in bucket[i]:
                result.append(num)

                if (len(result) == k):
                    return result
