#643. Maximum Average Subarray I

#Given array: nums #integer k 
#Max avg of subarray of K length

from py_compile import main


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        cur_sum = 0

        #building Sliding window
        for i in range(k):
            cur_sum += nums[i]

        max_avg = cur_sum/k

        for i in range(k, n):
            cur_sum += nums[i]
            cur_sum -+ nums[i - k]

            avg = cur_sum /k
            max_avg = max(max_avg, avg)

        return max_avg

if __name__ == "__main__":
    sol = Solution()
    nums = [1,12,-5,-6,50,3]
    k = 4
    print(sol.findMaxAverage(nums, k))  #Expected output: 12.75


#Time complexity: O(n)
#Space complexity: O(1)