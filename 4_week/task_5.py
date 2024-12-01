'''
https://leetcode.com/problems/pancake-sorting/?envType=problem-list-v2&envId=array
'''

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        i = 0
        ans = []
        k = 0
        m = max(arr)
        #print(m)
        b = sorted(arr)
        print(arr)
        print(b)
        lenth = len(arr) - 1
        while arr != b:
            print(i)
            print(arr)
            if i != lenth and i != 0 and arr[i] == m:
                k = i + 1
                for j in range(0,int((k)/2+k%2)):
                    c = arr[j]
                    arr[j] = arr[k-1-j]
                    arr[k-1-j] = c
                ans.append(k)
                print(arr)
                k = lenth + 1
                for j in range(0,int((lenth + 1)/2)):
                    c = arr[j]
                    arr[j] = arr[lenth-j]
                    arr[lenth-j] = c
                lenth -= 1
                ans.append(k)
                print(arr)
                #newarr = arr[:lenth+1]
                m = 0
                for j in range(0,lenth+1):
                    if arr[j] > m:
                        m = arr[j]
                #print(m)
                i = 0
                print(arr)
            elif i == 0 and arr[i] == m:
                k = lenth + 1
                for j in range(0,int((lenth + 1)/2)):
                    c = arr[j]
                    arr[j] = arr[lenth-j]
                    arr[lenth-j] = c
                lenth -= 1
                ans.append(k)
                m = 0
                for j in range(0,lenth+1):
                    if arr[j] > m:
                        m = arr[j]
                i = 0
                print(arr)
                #print(m)
            elif i == lenth and arr[i] == m:
                lenth -= 1
                m = 0
                for j in range(0,lenth+1):
                    if arr[j] > m:
                        m = arr[j]
                i = 0
                #print(m)
                i = 0
                print(arr)
            else: i+=1
        return(ans)
