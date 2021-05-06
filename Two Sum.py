class Solution:
    List=[]
    def twoSum(self, nums, target):
        List=[]
        self.nums=nums
        self.target=target
        type(nums)
        type(target)
        dictionary={}
        length=len(nums)
        i=0
        while i<length:
        
            value=target - nums[i]
            print(value)
            if value in dictionary:
                return(dictionary[value],i)
               
            dictionary[nums[i]]=i
            
            i=i+1
            
Instantiating_Variable=Solution()
Instantiating_Variable.twoSum([2,7,11,15],9)
