class Solution(object):
    def minimumPushes(self, word):
        pushes = 0

        for i in range(len(word)):
            pushes += (i // 8) + 1

        return pushes
        