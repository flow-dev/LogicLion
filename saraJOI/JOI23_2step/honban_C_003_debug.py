def process_string(S):
    i = 0
    print(S)
    while i + 2 < len(S):
        prefix = S[i:i+3]
        print(prefix,i)

        if prefix == "RGB":
            i += 3
        elif prefix == "RBG":
            S = S[:i+1] + 'G' + S[i+2:]
            i += 1
        elif prefix == "GRB":
            S = S[:i] + '-' + S[i+1:]
            S = S[:i+1] + 'G' + S[i+2:]
            i += 2
            print(S,i)
        elif prefix == "GBR":
            S = S[:i] + '-' + S[i+1:]
            S = S[:i+2] + '-' + S[i+3:]
            i += 2
        elif prefix == "BGR":
            S = S[:i] + '-' + S[i+1:]
            S = S[:i+2] + '-' + S[i+3:]
            i += 2
        elif prefix == "BRG":
            S = S[:i] + '-' + S[i+1:]
            i += 1
        else:
            i += 1

    return S

# テストケース
S = "GRBBRG"
result = process_string(S)
print(result)
