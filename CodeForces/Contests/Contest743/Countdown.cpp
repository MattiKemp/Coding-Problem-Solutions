#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define ld long double
#define sza(x) ((int)x.size())
#define all(a) (a).begin(), (a).end()

void solve(int n, char * digits) {
    int operations = 0;
    //int trailingZeros = 0;
    int trailingInts = 0;
    bool found = false;
    // non leading zeros
    for(int i = 0; i < n; i++){
        if(digits[i]!='0'){
            operations += (int) (digits[i]-'0');
            found = true;
            if(i!=n-1){
                trailingInts++;
            }
        }
    }
    operations += trailingInts;
    if(trailingInts == 0 && digits[n-1]=='0'){
        cout << 0 << endl;
    }
    else{
        cout << operations  << endl;
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    cin >> tc;
    for (int t = 1; t <= tc; t++) {
        int n;
        cin >> n;
        char digits[n];
        cin >> digits;
        solve(n, digits);
    }
}


