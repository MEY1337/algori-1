def solution(arr):
    answer = []
    prev = None  # 바로 이전 숫자를 기억할 변수

    for x in arr:
        # 이전 숫자와 다를 때만 추가
        if x != prev:
            answer.append(x)
            prev = x

    return answer
