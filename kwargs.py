# 입력받은 정보 출력하기

def user_info(**kwargs):
    print(kwargs.values())
    print(kwargs['name'])
    print(f'이름:{kwargs["name"]} / 나이:{kwargs["age"]}')
    return

user_info(name='홍길동', age='47')

# def user_info(**kwargs):
#     for key, value in kwargs.items():   # 딕셔너리를 리스트처럼 풀수있는 기능 .items()
#         print()