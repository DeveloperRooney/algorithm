# 최대값 구하기

def maxnum(number):

    max = 0
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]

    return max

a = [2, 4, 51, 29, 20]

number = maxnum(a)

print(number)