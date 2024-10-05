'''
https://leetcode.com/problems/insert-interval/?envType=problem-list-v2&envId=array
'''

class Solution(object):
    def insert(self, inter, new_inter):
        new_arr = []
        fl = 0
        i1 = new_inter[0]
        i2 = new_inter[1]
        if len(inter) > 0:
            for i in range(0,len(inter)):
                if fl == 0 and new_inter[0] >= inter[i][0] and new_inter[0] <= inter[i][1]:
                    fl = 1
                    i1 = inter[i][0]
                elif fl == 0 and i == 0 and new_inter[0] <= inter[i][0]:
                    fl = 1
                    i1 = new_inter[0]
                elif fl == 0 and new_inter[0] <= inter[i][0]:
                    fl = 1
                    i1 = new_inter[0]
                elif fl == 0:
                    new_arr.append(inter[i])
                if fl == 1 and new_inter[1] < inter[i][0]:
                    i2 = new_inter[1]
                    fl = 2
                    arr = [i1, i2]
                    new_arr.append(arr)
                    new_arr.append(inter[i])
                elif fl == 1 and new_inter[1] <= inter[i][1]:
                    i2 = inter[i][1]
                    fl = 2
                    arr = [i1,i2]
                    new_arr.append(arr)
                elif i == len(inter) - 1 and new_inter[1] >= inter[i][1]:
                    i2 = new_inter[1]
                    fl = 2
                    arr = [i1, i2]
                    new_arr.append(arr)
                elif fl == 2:
                    new_arr.append(inter[i])
        else:
            new_arr.append(new_inter)
        return(new_arr)