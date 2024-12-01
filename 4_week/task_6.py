#не доделано (45/56 тестов)

words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["e","o"]
s = words2
for o in range(0,len(s)):
    words2 = []
    for i in range(0,len(s[o])):
        words2.append(str(s[o][i]))
    for i in range(0,len(words2)):
        j = 0
        while j < len(words1):
            if not(words2[i][0] in words1[j]) or (words2.count(words2[i]) > words1[j].count(words2[i])):
                words1.remove(words1[j])
            else: 
                j += 1
#print(words2.count("e"))
print(words1)
