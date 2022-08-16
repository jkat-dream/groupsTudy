from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer=[]
    
    for c in course:
        food = []
        for o in orders:
            if len(o) < c : continue
            food.extend(list(combinations(sorted(o), c)))  # o번 손님의 음식의 조합
        if not food : break
        dic = Counter(food)
        order = sorted(dic, reverse=True, key=lambda x: dic[x])  # 주문순
        _max = dic[order[0]]
        if _max < 2 : continue
        j = 0
        
        while _max == dic[order[j]]:
            answer.append("".join(order[j]))	# 튜플을 문자열로 변환
            j += 1

    answer.sort()
    
    return answer