def solution(a, b):
    # a가 b보다 클 수도 있으므로 범위를 정렬
    start, end = min(a, b), max(a, b)
    
    # 방법 1: 반복문으로 합하기
    # return sum(range(start, end + 1))

    # 방법 2: 등차수열 공식 사용 (더 효율적)
    n = end - start + 1  # 항의 개수
    return (start + end) * n // 2