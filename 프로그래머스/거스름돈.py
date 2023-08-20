def solution(n, money):
    answer = 0 
    #만약 n = 5 money=[1,2,5]

    result = [0] * (n + 1) 

    for i in range(money, n+1, money): #money 부터 거스름돈 n + 1 까지 money의 크기 만큼 증가

    return result[n] % 1000000007

n = 5
money = [1, 2, 5]
result = solution(n, money)
print(result)

#result 리스트에 0들을 1씩 추가?
# 예시로 하면 
# 1, 1, 1, 1, 1
# 1, 1, 1, 2, 0
# 1, 0, 2, 2, 0
# 0, 0, 0, 0, 5
# 리스트에는 1, 2, 5씩 증가 가능 그러면 리스트 5개의 안에 있는 합들이 n을 넘지 않아야 함
# 1로 다 채우고 2로 다 채우다 넘으면 틀렸다 하고 2로 다채운 값을 맨 앞부터 1로 바꾸면서 확인
# 그러다 5가 넘지 않는 상황이 발생하면 값을 계산해서 5랑 같다면 탈출
# 아 이건 문제가 좀 될거같음 안돼 이러면 2,3번의 예시가 나올 수 없음
#피곤함..ㅂ2