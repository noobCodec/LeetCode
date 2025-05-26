#Solution1
def longestPalindrome(words) -> int:
    d = {}
    res = 0
    for word in words:
        if(word in d and d[word] > 0):
            res+=4
            d[word] -=1
        else:
            backwords = word[::-1]
            d[backwords] = d.get(backwords,0) + 1
    for item in d:
         if(d[item] == 1 and item[0] == item[1]):
              res+=2
              break
    return res
#Solution2
def longestPalindrome2(words) -> int:
    d = {}
    res = 0
    for word in words:
        if(word in d and d[word] > 0):
            res+=4
            d[word] -=1
        else:
            backwords = word[::-1]
            d[backwords] = d.get(backwords,0) + 1
    for item in d:
         if(d[item] == 1 and item[0] == item[1]):
              res+=2
              break
    return res

def test_answers():
        assert(longestPalindrome(["lc","cl","gg"]) == 6)
        assert(longestPalindrome(["ab","ty","yt","lc","cl","ab"]) == 8)
        assert(longestPalindrome(["cc","ll","xx"]) == 2)
        assert(longestPalindrome(["io","io"]) == 0)
        assert(longestPalindrome(["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]) == 22)
        assert(longestPalindrome(["qo","fo","fq","qf","fo","ff","qq","qf","of","of","oo","of","of","qf","qf","of"]) == 14)
        assert(longestPalindrome(["bb","bb"]) == 4)