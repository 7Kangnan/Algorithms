li = [1, 29, 99, 0, 8]
print(li)

w = len(li) - 1
# 外层循环n-1次；
for i in range(w):
    n = i + 1
    while n > 0 and li[n] < li[n-1]:
        li[n], li[n-1] = li[n-1], li[n]
        n -= 1

print(li)

# 输出为：
# [1, 29, 99, 0, 8]
# [0, 1, 8, 29, 99]
