nums = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

res = {}

for i in range(1, 10):

    c = 0

    for n in nums:
        if n % i == 0:
            c = c + 1

    res[i] = c

print(res)
