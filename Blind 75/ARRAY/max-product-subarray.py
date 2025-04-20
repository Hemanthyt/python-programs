class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
		# code here
        res=max(arr)
        currMax,currMin = 1,1
        for i in arr:
            temp = i*currMax
            currMax = max(temp,i*currMin,i)
            currMin = min(temp,i*currMin,i)
            res = max(res,currMax)
        return res