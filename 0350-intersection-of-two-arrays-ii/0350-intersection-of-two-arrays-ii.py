class Solution(object):
    def intersect(self, nums1, nums2):
        answer = []

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    answer.append(nums1[i])
                    nums2[j] = None      # Mark as used
                    break                # Stop searching for this element

        return answer