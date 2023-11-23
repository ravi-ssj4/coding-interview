class Solution:
    # Partition Labels:

    # eg 1:
    # s = "ababcbacadefegdehijhklij"
    # output = [9, 7, 8]

    # eg 2:
    #     0123456789
    # s = "eccbbbbdec"
    # output = [10]

    # from eg. 2, its clear that we need to somehow have the last idx of 'e'
    # like here, lastidx of 'e' = 8

    # so we can try for a partition starting from 0th till the 8th idx, but
    # we have other chars in between, which might come later than last idx of 'e' ie. 8
    # so we need to grow our partition based on the elements we see in between start idx of 'e'
    # and end idx of 'e'

    # -> better to store last indices of all chars in the string beforehand
    # -> iterate over the string char by char and keep on growing partitions and noting their size
    # -> once we are done with a partition, we can store the size and reset the size variable

    #     0123456789
    # s = "eccbbbbdec"

    # lastIdx = {
    #     'e': 8,
    #     'c': 9,
    #     'b': 6,
    #     'd': 7
    # }

    # i = 9
    # s[i] = 'c'
    # end = 9
    # size = 9

    def partitionLabels(self, s):
        lastIdx = {}
        
        for i in range(len(s)):
            lastIdx[s[i]] = i
        
        end = 0
        size = 0
        result = []
        for c in s:
            size += 1
            end = max(end, lastIdx[c])
            if i == end:
                result.append(size)
                size = 0
        return result
        