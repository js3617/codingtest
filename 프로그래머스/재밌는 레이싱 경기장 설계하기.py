def solution(heights):
    heights.sort()
    n = len(heights)
    h = n // 2
    min_list = []
    if n % 2 == 0:
        small = heights[:h]
        big = heights[h:]
        answer = [road for bundle in zip(big, small) for road in bundle]
        for i in range(len(answer) - 1):
                subtraction = answer[i] - answer[i + 1]
                min_list.append(abs(subtraction))
    else:
        light = heights[:h]
        heavy = heights[h+1:]
        result = [node for pair in zip(light, heavy) for node in pair]

        first = result[0] - heights[h]
        last = result[-1] - heights[h]

        if abs(first) > last:
            result.insert(0, heights[h])
            for i in range(len(result) - 1):
                subtraction = result[i] - result[i + 1]
                min_list.append(abs(subtraction))
        else:
            result.append(heights[h])
            for i in range(len(result) - 1):
                subtraction = result[i] - result[i + 1]
                min_list.append(abs(subtraction))

    

    return min(min_list)
heights = [1,2,4,8,20,22,30]
result = solution(heights)
print(result)