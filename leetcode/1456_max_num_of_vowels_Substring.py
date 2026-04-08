class Solution(object):
    def maxVowels(self, s, k):
        v='aeiou'
        max_v=0
        curr_v=0
        left=0
        for i in range(k):
            if s[i] in v:
                curr_v+=1
        max_v=max(max_v,curr_v)
        for i in range(k,len(s)):
            if s[left] in v:
                curr_v-=1
                left+=1
            else:
                left+=1
            if s[i] in v:
                curr_v+=1
            max_v=max(max_v,curr_v)
        return max_v