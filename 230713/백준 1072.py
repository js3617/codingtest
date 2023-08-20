x, y = map(int, input().split())
z = (y*100) // x

if z > 98: # 99 이상이면 -1 출ㄺ
    print(-1)
    exit()
    
start = 0
end = x
while start < end: #시작지점이 끝지점 보다 작을 때 까지 반복한다
    mid = (end + start) // 2 
    if (y + mid) * 100 // (x + mid) != z: #z와 같은지 비교
        end = mid
    else:
        start = mid + 1

mid = start
print(mid)