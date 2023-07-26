n, m = map(int, input().split())
card = list(map(int, input().split()))
card.sort()

for i in range(n):
    for j in range(n+1):
        for k in range(n+2):
            sum = card[i] + card[j] + card[k]

            if sum<=m:
                
print(sum)
