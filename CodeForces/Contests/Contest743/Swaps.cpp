#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define ld long double
#define sza(x) ((int)x.size())
#define all(a) (a).begin(), (a).end()

void solve(int n, int * arrA, int * arrB) {
    int operations = 0;

}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    cin >> tc;
    for (int t = 1; t <= tc; t++) {
        int n;
        cin >> n;
        int arrA[n];
        for(int i = 0; i < n; i++){
            cin >> arrA[i];
        }
        int arrB[n];
        for(int i = 0; i < n; i++){
            cin >> arrB[i];
        }
        solve(n, arrA, arrB);
    }
}


