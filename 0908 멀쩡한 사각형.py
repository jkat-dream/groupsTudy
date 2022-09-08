import math
def solution(w,h):
    return w*h - (w+h-math.gcd(w,h))

    #최대공약수가 1일때-w+h-1
    #최대공약수가 1보다 큰 경우-w+h-g(최대공약수)