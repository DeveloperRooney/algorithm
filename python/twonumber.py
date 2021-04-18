# 값 두 개 뽑아서 더하기
# 정수 리스트 numbers를 입력하였을 때 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return

def solution(numbers):
    
    answer = []

    for x in range(len(numbers)-1):
        for y in range(1+x, len(numbers)):
            if numbers[x] + numbers[y] not in answer:
                print(numbers[x], "  ", numbers[y])
                answer.append(numbers[x] + numbers[y])
    return answer

arr = [5, 0, 2, 7]

arr = solution(arr)
arr = sorted(arr)

print(arr)

