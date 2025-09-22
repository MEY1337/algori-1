import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    if line == "0":           # 입력 종료
        break

    nums = list(map(int, line.split()))
    N = nums[0]
    arr = nums[1:1+N]

    # 연속 중복 제거
    result = []
    prev = None
    for x in arr:
        if prev is None or x != prev:
            result.append(x)
        prev = x

    # 형식에 맞춰 출력: 값들 + 공백 + $
    print(*result, "$")