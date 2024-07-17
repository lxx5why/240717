# 구구단 2-9단을 출력
# 출력할 때, 2X3=6과 같이 어떤 값을 곱하였는지도 함께 출력
for n in range(2, 10):
    for k in range(1, 10):
        print(n, " X", k, "=", n*k)

# 구구단 함수를 작성
# 매개변수 입력에 따라 해당 구구단을 화면에 출력하는 함수
def mul_numbers(x):
    print(x)
    for n in range(1, 10):
        print(x, "X", n, "=", x*n)
mul_numbers(2)

# # 사용자로부터 문자메시지를 입력 받아서
# text = input("문자 메시지를 입력해주세요:")
# # 문자메시지 길이 판별 함수
# x = "내가 입력하는 문자 메시지"
# print(len(x))
# # 문자메시지 길이에 따라 문자 요금이 결정되는 프로그램을 작성
# def find_len(x):
#     # 요금을 반환하기 위해서 변수 설정 (초기화)
#     result= 0
#     if len(x) <= 20:
#         print("50원")
# # 메시지의 길이가 20 이하면 50원, 20을 초과하면 100원
#     def find_len(x):
#         elif len(x) > 20:(
#             result) = 100
#         return result
# # 문자 요금을 반환하는 코드를 작성
# text = input("문자 메시지를 입력해주세요")
# var = find_len(text)
# print(var)
a = input("문자를 입력하세요: ")
def fun (a):
    return a
result = fun(a)
if len(result) <= 20:
    print("문자 요금은 50원입니다.")
else:
    print("문자 요금은 100원입니다.")

# 학점 변환기 함수
def score(a):
    result = 0
    if 0 <= a <= 20:
        result = "E"
    elif 21 <= a <= 40:
        result = "D"
    elif 41 <= a <= 60:
        result = "C"
    elif 61 <= a <= 80:
        result = "B"
    elif 81 <= a <= 100:
        result = "A"
    return result
sc = int(input("점수를 입력해주세요: "))
print(score(sc))

# 점수 구간에 해당하는 학점이 아래와 같이 정의
# 사용자로부터 score를 입력 받아
# 학점으로 환산하여 반환하는 함수를 작성

# 리스트 변수의 평균 값을 구하는 함수를 작성

def mean_list (x):
    result = 0
    for i in x:
        result = result + i
        avg = result / len(x)
    return avg
var = list(range(2, 99999))
print(mean_list(var))
# 리스트의 길이는 매번 달라질 수 있음에 유의
# sum() 함수를 사용할 수 없다