#17952
n = int(input())
score = 0
count_num = []

for i in range(n):
   a = list(map(int, input().split()))
   if a[0] == 1: #새로운 과제
      count_num.append((a[1], a[2])) #점수 시간 더하기
   if count_num:
      result, time = count_num.pop() #최근 과제에서 점수와 시간 꺼냄
      time -= 1
      
      if time == 0:
         score += result #과제 시간이 0 되면 점수 추가
      else:
         count_num.append((result, time))#다시 계산

print(score)