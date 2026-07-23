class Solution(object):
    def removeDuplicates(self, nums):

        # If the array is empty, there are no unique elements
        if not nums:
            return 0

        # i points to the index of the last unique element
        i = 0

        # j scans the array from the second element onwards
        for j in range(1, len(nums)):

            # If we find a new unique element
            if nums[i] != nums[j]:

                # Move i to the next position
                i += 1

                # Place the new unique element at index i
                nums[i] = nums[j]

        # Number of unique elements = last index + 1
        return i + 1