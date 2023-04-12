import sys

T = int(sys.stdin.readline())
for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print('Case #{i}: {a} + {b} = {ans}' .format(i=i+1, ans=A + B, a=A, b=B))