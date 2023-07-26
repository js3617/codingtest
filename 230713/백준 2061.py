k, L = map(int, input().split())
 # L까지 설정하는 것은 좋은 암호인지 판단하기 위해 K를 인수분해하는 과정에서 L 이상의 인수가 있는지를 확인하는 것
for i in range(2, L):  # k를 인수분해하여 L보다 크거나 같은 인수가 있는지를 검사
    if k % i == 0:
        print("BAD", i)
        exit() # L까지 범위를 설정하여 K의 인수 중 L 이상의 수가 있는지를 확인합니다. 만약 K의 인수 중 하나라도 L 이상이면, 해당 값을 출력하고 "BAD"를 출력하여 좋은 암호가 아니라고 판단하는 것
        
print("GOOD")