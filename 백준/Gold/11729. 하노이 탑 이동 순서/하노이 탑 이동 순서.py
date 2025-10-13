# BOJ 11729: 하노이 탑 이동 순서
import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

n = int(input().strip())
write = sys.stdout.write

# 총 이동 횟수 먼저 출력
write(str((1 << n) - 1) + "\n")

def move(k: int, s: int, a: int, t: int) -> None:
    if k == 0:
        return
    move(k - 1, s, t, a)    # 위의 k-1개를 보조(a)로
    write(f"{s} {t}\n")     # 가장 큰 1개를 목적지(t)로
    move(k - 1, a, s, t)    # 보조(a)의 k-1개를 목적지(t)로

move(n, 1, 2, 3)
