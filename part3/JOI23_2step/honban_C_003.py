def calc_min_cost(N, S, A, B, C):
    def count_color(color):
        return sum([1 for light in lights if light == color])

    def calculate_cost():
        count_R = count_color('R')
        count_G = count_color('G')
        count_B = count_color('B')

        return min(
            A * (count_G + count_B),
            B * (count_R + count_B),
            C * (count_R + count_G)
        )

    def is_valid(lights):
        return all(lights[i] != lights[i + 1] for i in range(len(lights) - 1))

    lights = list(S)
    min_cost = float('inf')

    for i in range(N):
        for j in range(i + 1, N + 1):
            sublights = lights[i:j]
            original_cost = calculate_cost()

            for k in range(len(sublights)):
                new_lights = lights[:i] + lights[j:]
                new_lights.insert(i + k, sublights[k])

                if is_valid(new_lights):
                    new_cost = calculate_cost()
                    print(f"New lights: {''.join(new_lights)}, Cost: {new_cost}")

                    min_cost = min(min_cost, new_cost)

    return min_cost

if __name__ == '__main__':
    N = int(input())
    S = input()
    A, B, C = map(int, input().split())

    result = calc_min_cost(N, S, A, B, C)
    print(result)
