#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin >> N;

  vector<int> A(N);

  for (int i = 0; i < N; i++) {
    cin >> A.at(i);
  }

  int sum = 0;

  for (int i = 0; i < N; i++) {

    sum += A.at(i);

  }

  // 平均点
  int mean = sum / N;

  // 平均点から何点離れているかを計算して出力
  for (int i = 0; i < N; i++) {

    // ②ここにプログラムを追記
    // 負の数を出力しないように注意
    if (A.at(i) > mean) {
      cout << A.at(i) - mean << endl;
    }
    else {
      cout << mean - A.at(i) << endl;
    }

  }

}
