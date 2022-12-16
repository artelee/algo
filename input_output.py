# 1000번
def get_1000():
    # input_number = input()
    # input_number_list = input_number.replace(' ', ',').split(',')
    a, b = map(int, input().split())
    # if len(input_number_list) == 2:
    #     a, b = int(input_number_list[0]), int(input_number_list[1])
    if 0 < a and b < 10:
        print(a + b)


# 2501번 약수구하기
def get_2501():
    n, k = map(int, input().split())
    n_divisor_list = [(i + 1) for i in range(n) if n % (i + 1) == 0]
    print(n_divisor_list)

get_2501()