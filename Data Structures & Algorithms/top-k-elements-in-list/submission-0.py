
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num,0)+1
        res = sorted(count.items(),key=lambda pair:pair[1] , reverse=True)
        result = res[:k]
        output=[]
        for pair in result:
            output.append(pair[0])
        return output