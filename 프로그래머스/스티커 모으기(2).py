def solution(sticker):
    answer = 0
    if len(sticker) <= 3:
        return max(sticker)
    
    n = len(sticker)
    l1 = [0] + sticker[: -1]
    l2 = [0] + sticker[1:]
    for i in range(2,n):
        l1[i] = max(l1[i] + l1[i-2], l1[i-1])
    for i in range(2,n):
        l2[i] = max(l2[i] + l2[i-2], l2[i-1])

    return max(l1[-1],l2[-1])