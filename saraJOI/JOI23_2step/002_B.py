def min_height_difference_binary_search(A, B, C, D):
    # 各クラスの身長を結合してソート
    all_heights = sorted(A + B + C + D)

    # 最小の差を初期化
    min_height_difference = float('inf')

    # 各クラスの生徒の身長に対して二分探索
    for i in range(len(A)):
        for j in range(len(B)):
            # 二分探索で候補を探す
            candidate_left = max(A[i], B[j])
            candidate_right = min(C[-1], D[-1])

            # 差を計算して最小値を更新
            min_height_difference = min(min_height_difference, candidate_right - candidate_left)

            # 最小値が0になったらそれ以上の探索は不要
            if min_height_difference == 0:
                return 0

    return min_height_difference

# 入力例
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

# 結果の出力
result = min_height_difference_binary_search(A, B, C, D)
print(result)
