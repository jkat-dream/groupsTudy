def solution(numbers):
    answer = set()
    length = len(numbers)
    
    for i in range(length):
        for j in range(i+1, length):
            total = numbers[i] + numbers[j]
            
            answer.add(total)
    answer = sorted(answer)
    return answer