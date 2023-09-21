# def solution(heights):
#     heights.sort()
#     n = len(heights)
#     h = n // 2 #중앙값
#     min_list = []
#     if n % 2 == 0: #짝수인 경우의 수 
#         small = heights[:h] #중앙값을 기준으로 앞으로는 작은 수
#         big = heights[h:] #중앙값을 기준으로 뒤로는 큰수
#         answer = [road for bundle in zip(big, small) for road in bundle] #순서를 섞음
#         for i in range(len(answer) - 1): #앞뒤 값을 빼기
#                 subtraction = answer[i] - answer[i + 1]
#                 min_list.append(abs(subtraction)) # 값 저장
#     else: #홀수의 경우
#         light = heights[:h]
#         heavy = heights[h+1:]
#         result = [node for pair in zip(light, heavy) for node in pair]

#         first = result[0] - heights[h]
#         last = result[-1] - heights[h]

#         if abs(first) > last:
#             result.insert(0, heights[h])
#             for i in range(len(result) - 1):
#                 subtraction = result[i] - result[i + 1]
#                 min_list.append(abs(subtraction))
#         else:
#             result.append(heights[h])
#             for i in range(len(result) - 1):
#                 subtraction = result[i] - result[i + 1]
#                 min_list.append(abs(subtraction))

    

#     return min(min_list)

# import itertools as it
# import numpy as np
# def minus(x):
#     return abs(x[0] - x[1])
# def solution(h):
    
#     n = len(h)
#     all_h = list(it.permutations(h,2))
#     all_h2 = list(map(minus, all_h))
#     print(all_h,all_h2)
#     print(list(set(all_h2)))
#     # all_h = np.array(all_h)
#     # A = abs(all_h[:,:-1]-all_h[:,1:])
#     # A = np.array(list(map(sorted, A)))
#     # A =
#     # retrun max(A[:,0])
#     # for i in all_h:
#     #     i = list(i)
#     #     A = np.array(i[:-1]) -np.array(i[1:])
#     #     A = min(list(map(abs,A)))
#     #     # print(max_min)
#     #     if max_min < A :
#     #         # print(A)
#     #         max_min = A
    
#     # return max_min
# heights = [1,2,4,8,20,22,30]
# result = solution(heights)
# print(result)



def solution(heights):
    heights.sort() #정렬
    n = len(heights)
    h = n // 2 #중앙값
    min_list = []
    if n % 2 == 0: #작수의 경우
        small = heights[:h] #중앙 값 보다 작은
        big = heights[h:] #중앙 값 보다 큰
        answer = [road for bundle in zip(big, small) for road in bundle]
        for i in range(len(answer) - 1): #앞뒤 값 비교해서 계산
                minus = answer[i] - answer[i + 1]
                min_list.append(abs(minus)) #min_list 에추가
    else: #홀수의 경우
        light = heights[:h] 
        heavy = heights[h+1:] #중앙 값 보다 1 큰수들
        result = [node for pair in zip(light, heavy) for node in pair]

        first = result[0] - heights[h] #정리된 하나의 리스트에서 첫번째와 중앙값 빼기
        last = result[-1] - heights[h] #마지막 인덱스와 중앙값 빼기

        if abs(first) > last:
            result.insert(0, heights[h]) #맨앞에 중앙값 추가
            for i in range(len(result) - 1):
                minus = result[i] - result[i + 1]
                min_list.append(abs(minus))
        else:
            result.append(heights[h]) #맨뒤에 중앙값 추가
            for i in range(len(result) - 1):
                minus = result[i] - result[i + 1]
                min_list.append(abs(minus))

    

    return min(min_list)
heights = [1,2,4,8,20,22,30]
result = solution(heights)
print(result)