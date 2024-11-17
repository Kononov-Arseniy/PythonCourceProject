#пройдено 703/717 тестов
nums = [-1,-2,-3,-4,-5]
k = 2
x = 2
left = 0
ans = []
right = k - 1
cnt_arr = []
for i in range(0,right + 1):
    cnt_arr.append(nums[i])
while (right != len(nums) - 1):
    cnt_sorted = cnt_arr
    cnt_sorted = sorted(cnt_arr)
    if (cnt_sorted[x-1] < 0):
        ans.append(cnt_sorted[x-1])
    else:
        ans.append(0)
    cnt_arr = cnt_arr[1:]
    right += 1
    cnt_arr.append(nums[right])
cnt_sorted = cnt_arr
cnt_sorted = sorted(cnt_arr)
if (cnt_sorted[x-1] < 0):
    ans.append(cnt_sorted[x-1])
else:
    ans.append(0)
print(ans)