def solution(nums):
    answer = 0
    cnt=len(nums)/2
    nums_set=set(nums)
    if len(nums_set)<cnt:
        answer=len(nums_set)
    else:
        answer=cnt
    return answer