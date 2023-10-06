def solution(land, P, Q):
    n = len(land)
    lands = [] 
    answer_list = []

    for i in range(n):
        lands += land[i] #land를 하나의 리스트로 변환
    
    # 중복된 값을 제거하기 위해 lands를 set으로 변환한 후 다시 리스트로 변환
    one_lands = list(set(lands))

    for j in one_lands: #0, 1, 2, 3, 4를 기준으로 계산
        down_count = 0 #삭제
        up_count = 0 #추가
        for k in lands: # [4,4,3,3,2,2,2,1,0] 값 하나하나 비교하기
            count = j - k
            if count < 0: #삭제 값 증가
                down_count += count
            elif count > 0: #증가 값 증가
                up_count += count
        
        answer_list.append(abs(down_count) * Q + up_count * P)

    return min(answer_list)

print(solution([[4,4,3],[3,2,2],[2,1,0]], 5, 3))
# 결과: 33