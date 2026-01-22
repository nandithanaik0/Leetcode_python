#217. Contains Duplicate

# i/p --> nums
#o/p --> true/ false -->true if atleast elements occurs twice --> else false  no dupicates

#1. Brute force approach

"""
nums = [1,2,3,1]

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] == nums[j]:
            print(True)
            exit()
print(False)
time complexity: O(n^2)
space complexity: O(1)
"""
#2. Using Sorting
"""
nums = [1,2,3,1]
nums.sort() --> [1,1,2,3]

##here we observe that after sorting the duplicates are adjacent to each other

here time: complexity: O(n log n) due to sorting
space complexity: O(1)
"""

#3. Using Hashing (using extra space)
#help us insert elements in O(1) time and check is a certain element exists

class Solution:
    def containsDuplicate(self,nums: List[int]) -> bool:
        hashset = set()

        for i in nums:
           if i in hashset:
               return True
           hashset.add(i)
        return False
    
if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,1]
    print(sol.containsDuplicate(nums))  #Expected output: True
    

