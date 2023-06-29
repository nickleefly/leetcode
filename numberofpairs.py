import pdb


class Solution:
    def findPairsBinarySearch(self, arr, target):
        res = 0
        for i in range(len(arr)):
            # pdb.set_trace()
            first = arr[i]
            remain = arr[i+1:]
            l = 0
            h = len(remain)-1
            print("i is ", i)
            while l < h:
                m = l+(h-l)//2
                print("m is %d, remain[m] is %s" % (m, remain[m]))
                if first+remain[m] >= target:
                    h = m
                else:
                    l = m+1
            print("remain is %s, l is %d" % (remain, l))
            res += len(remain)-l
            print("res is ", res)
        return res

    def numberOfPairs(self, nums, target):
        low = 0
        high = len(nums) - 1
        pairs = 0
        while low < high:
            # print("high is %d, low is %d" % (high, low))
            # currrent pointer at high, if sum >= target, move pointer from high to left
            if nums[high] + nums[low] >= target:
                pairs += high - low
                high -= 1
            else:
                low += 1
        return pairs


s = Solution()
print(s.findPairsBinarySearch([1, 3, 7, 9, 10, 11], 7))
# print(s.numberOfPairs([1,3,7,9,10,11],7))
