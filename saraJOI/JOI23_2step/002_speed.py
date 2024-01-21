def calculate_sale_price(N, M, P, A, Q, customer_info):
    total_price = 0

    # 辞書に価格情報を事前に格納
    price_dict = {}
    for i in range(N):
        if A[i] not in price_dict:
            price_dict[A[i]] = P[i]
        else:
            price_dict[A[i]] = min(price_dict[A[i]], P[i] // 2)

    for k in range(Q):
        Tk = customer_info[k][0]
        Lk = customer_info[k][1] - 1
        Rk = customer_info[k][2] - 1

        customer_price = sum(price_dict[A[i]] if A[i] == Tk else P[i] for i in range(Lk, Rk + 1))

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
