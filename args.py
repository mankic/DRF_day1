# 입력된 값을 모두 더해주는 함수

def sum(*args): 
    result = 0
    for x in args:
        result += x
    return result


print(sum(1,2,3,4,5,6))


