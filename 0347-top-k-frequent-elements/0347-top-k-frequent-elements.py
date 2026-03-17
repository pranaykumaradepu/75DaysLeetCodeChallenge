class Solution(object):
    def topKFrequent(self, nums, k):
        # 1. Count frequencies - O(n)
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            
        # 2. Create buckets where index = frequency - O(n)
        # We need len(nums) + 1 buckets
        freq = [[] for _ in range(len(nums) + 1)]
        
        for n, c in count.items():
            freq[c].append(n)
            
        # 3. Build the result by scanning buckets backward - O(n)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                    