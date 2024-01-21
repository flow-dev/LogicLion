def calculate_sale_price(N, M, P, A, Q, customer_info):
    total_price = 0

    for k in range(Q):
        Tk = customer_info[k][0]
        Lk = customer_info[k][1] - 1
        Rk = customer_info[k][2] - 1

        customer_price = 0

        if Tk <= M:
            for i in range(Lk, Rk + 1):
                if A[i] == Tk:
                    customer_price += P[i] // 2
                else:
                    customer_price += P[i]
        else:
            for i in range(Lk, Rk + 1):
                customer_price += P[i]

        print(customer_price)
        total_price += customer_price

    return total_price


if __name__ == "__main__":
    N, M, Q = map(int, input().split())

    P = []
    A = []
    for _ in range(N):
        p, a = map(int, input().split())
        P.append(p)
        A.append(a)

    customer_info = [list(map(int, input().split())) for _ in range(Q)]

    calculate_sale_price(N, M, P, A, Q, customer_info)