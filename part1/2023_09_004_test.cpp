#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> A(N);
    for(int i = 0; i < N; i++) cin >> A[i];
    vector<bool> pushed(10);
    for(int i = 0; i < N; i++) pushed[A[i]] = true;
    for(int i = 0; i < 10; i++) {
        if(pushed[i]) cout << i << endl;
    }
    return 0;
}