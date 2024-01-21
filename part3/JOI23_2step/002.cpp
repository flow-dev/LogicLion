#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    // 入力
    int N;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; i++) {
        cin >> A.at(i);
    }
    bool a = false;

    // 操作
    for (int i = 0; i < N - 2; i++) {
        for (int j = i + 1; j < N - 1; j++) {
            for (int k = j + 1; k < N; k++) {
                if (A.at(i) == A.at(j) - 3 == A.at(k) - 6) {
                    a = true;
                    break;
                }
            }
            if (a) {
                break;
            }
        }
        if (a) {
            break;
        }
    }

    // 結果を出力
    if (a) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
    return 0;
}