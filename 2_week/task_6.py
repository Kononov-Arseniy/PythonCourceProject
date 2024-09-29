# не дорешано 72/152

num = [0]*10
secret = str(input())
guess = str(input())
bulls = 0
cows = 0
istr = ""
for i in range(0,len(secret)):
    if secret[i] == guess[i]:
        bulls += 1
        istr += str(i)
        if i != len(secret) - 1:
            secret = secret[:i] + '%' + secret[i+1:]
        else:
            secret = secret[:i] + '%'
b = bulls
for i in range(0,len(secret)):
    if b > 0 and guess[i] in secret and num[int(guess[i])] < b and not(str(i) in istr):
        cows += 1
        num[int(guess[i])] += 1
    elif b == 0 and guess[i] in secret and num[int(guess[i])] < secret.count(str(int(guess[i]))):
        cows += 1
        num[int(guess[i])] += 1
ans = str(bulls) + 'A' + str(cows) + 'B'
print(ans)