left = list(input())
right = []           # 임시 공간
M = int(input())
for m in range(M):
    ord = list(input().split())

    if ord[0] == 'L':               # 커서 왼쪽 이동
        if left:                         # 값이 존재할 때
            right.append(left.pop())      # right 공간에 저장
    elif ord[0] == 'D':             # 커서 오른쪽 이동
        if right:                        # 값이 존재할 때 left에 저장
            left.append(right.pop())      
    elif ord[0] == 'B':             # 커서 왼쪽 문자 삭제
        if left:
            left.pop()
    else:                           # ord[1] 문자 추가
        left.append(ord[1])

# 모든 ord가 종료되면 저장된 문자를 가져와 다시 저장
left.extend(reversed(right))
print(''.join(left))