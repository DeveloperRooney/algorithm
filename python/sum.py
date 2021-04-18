# 1~n까지 연속한 숫자의 합을 구하는 알고리즘
# 입력 :
# 출력 : 1부터 입력받은 숫자까지의 합

def sum(number):
    sum = 0
    for x in range(1, number + 1):
        sum += x

    return sum

print("숫자 입력 : ", end = '')
num = int(input())

print ("입력한 숫자 : ",num)
print ("1 ~ 입력한 숫자까지의 합 : ", sum(num))

