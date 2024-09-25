'''
https://school.programmers.co.kr/learn/courses/30/lessons/181884?language=python3
정수 배열 numbers와 정수 n이 매개변수로 주어집니다.
numbers의 원소를 앞에서부터 하나씩 더하다가 그 합이 n보다 커지는 순간 이때까지 더했던 원소들의 합을 return 하는 solution 함수를 작성해 주세요.
'''
def solution(numbers, n):
    all_sum = 0

    for num in numbers:
        all_sum += num
        if all_sum > n:
            return all_sum

    return all_sum


print(solution([34, 5, 71, 29, 100, 34], 123))

# [34, 5, 71, 29, 100, 34]	123	139
# [58, 44, 27, 10, 100]	139	239


# solution([34, 5, 71, 29, 100, 34], 123)    # 139
# 34 + 5 + 71 + ... + = C
# 110 + 29 > 123
# C > 123