li = [1, 29, 99, 0, 8]
print(li)

w = len(li) - 1
# 外层循环n-1次；
for i in range(w):
    # 设首位为当前最小值
    minimum = li[i]
    position = i
    n = w - i
    # 内层第一轮循环n-1次
    # 往后依次减1
    for l in range(n):
        # 找出最小值
        if li[w-l] < minimum:
            minimum = li[w-l]
            position = w-l
    # 交换首位和最小值
    li[i], li[position] = li[position], li[i]

print(li)

# 输出为：
# [1, 29, 99, 0, 8]
# [0, 1, 8, 29, 99]
