li = [1, 29, 99, 0, 8]
print(li)

w = len(li) - 1
# 外层循环n-1次；
for i in range(w):
    n = w - i
    # 内层第一轮循环n-1次
    # 往后依次减1
    for l in range(n):
        # 后比前小就交换
        if li[w-l] < li[w-l-1]:
            li[w-l], li[w-l-1] = li[w-l-1], li[w-l]

print(li)

# 输出为：
# [1, 29, 99, 0, 8]
# [0, 1, 8, 29, 99]
