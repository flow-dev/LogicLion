def max_planted_flowers(N, garden):
    max_flowers = 0

    for r in range(N):
        for x in range(r + 1, N - r):
            for y in range(r + 1, N - r):
                flowers_planted = count_flowers(N, garden, r, x, y)
                max_flowers = max(max_flowers, flowers_planted)

    return max_flowers

def count_flowers(N, garden, r, x, y):
    colors = ['R', 'Y', 'B']
    flowers_planted = 0

    for i in range(N):
        for j in range(N):
            d = abs(i - x) + abs(j - y)
            if d <= r and garden[i][j] == colors[d]:
                flowers_planted += 1

    return flowers_planted

if __name__ == "__main__":
    N = int(input())
    garden = [input() for _ in range(N)]

    result = max_planted_flowers(N, garden)
    print(result)
