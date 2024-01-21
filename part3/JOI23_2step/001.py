def can_select_cards(cards):
    card_set = set(cards)

    for current_card in cards:
        # 次の2つの整数が存在するかどうかをチェック
        next_two_exist = (
            current_card + 3 in card_set and
            current_card + 6 in card_set
        )

        if next_two_exist:
            return "Yes"

    return "No"

if __name__ == '__main__':
    N = int(input())
    COST = list(map(int, input().split()))

    result = can_select_cards(COST)
    print(result)  # 出力: Yes / No
