class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        result = 0
        
        for i in range(n):
            visited = [0]*256
            
            for j in range(i,n):
                if(visited[ord(s[j])] == True):
                    break
                else:
                    result = max(result, j - i + 1)
                    visited[ord(s[j])] = True
                    
            visited[ord(s[i])] = False
        return result

                    
        