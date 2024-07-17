# 홀수/짝수 판별기 함수, 매개변수 입력에 따라 홀수 또는 짝수를 자동으로 판별하는 함수를 작성하시오
# 반환되는 값은 '홀수' 또는 '짝수'
def find_odd_even(n):
    result = 0
    if n%2 == 0:
        result = "짝수"
    else:
        result = "홀수"
    return result
print(find_odd_even(256))

# 판매가가 저장된 리스트가 있을 때
numbers = [100, 200, 300]
# 부가세가 포함된 가격을
def cost(numbers):
    result = []
    for n in numbers:
        result.append(n + (n * 0.1))
    return result
print(cost(numbers))
# 리스트로 반환하는 함수를 작성하시오.
