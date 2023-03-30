#6550
while True: #반복문
        try:
                s, t = map(str,input().split())
                value = 0 
                result = 0
                for i in range(len(t)):
                        if t[i] == s[value]: #순차적으로 t , s 대조
                                value += 1 #넘어가면서 맞으면 부분 문자열  1 증가
                        if value == len(s): #s의 단어의 길이와 대조
                                result = 1 #1이되면
                                break #멈추기
                if result == 1: #result 가 1이 되면 yes
                        print("yes")
                else:
                        print("no")
        except:
                break