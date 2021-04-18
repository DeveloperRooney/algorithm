# 동명이인을 찾는 알고리즘

# 이름 입력 :
# 출력 : 반복되는 이름의 집합

def samename(arr):
    length = len(arr)
    result = set()

    for x in range(0, length - 1):
        for y in range(x + 1, length):
            if arr[x] == arr[y]:
                result.add(arr[x])
    return result

nameList = []

while True:
    print("이름 입력 : ", end = "")
    name = input()
    if name == "0000":
        break
    nameList.append(name)


print(nameList)

nameList = samename(nameList)

print(nameList)


# 파이썬 set : 중복을 가지지 않는다 / 순서가 없다