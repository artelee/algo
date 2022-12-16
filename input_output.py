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
# N은 1 이상 10,000 이하이다. K는 1 이상 N 이하이다.
def get_2501():
    n, k = map(int, input().split())
    n_divisor_list = [(i + 1) for i in range(n) if n % (i + 1) == 0]
    # print(n_divisor_list)
    if len(n_divisor_list) < k:
        print(0)
    else:
        print(n_divisor_list[k-1])

get_2501()
