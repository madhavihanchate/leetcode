class Solution:
    def getSecondLargest(self, arr):
        slargest=-1
        largest=arr[0]
        for i in range(len(arr)):
            if arr[i] > largest:
                largest = arr[i]
                
        for i in range(len(arr)):
            if arr[i] > slargest and arr[i]!=largest:
                slargest = arr[i]
        return slargest
        