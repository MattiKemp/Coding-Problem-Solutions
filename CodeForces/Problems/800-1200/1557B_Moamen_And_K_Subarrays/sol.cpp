#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define ld long double
#define sza(x) ((int)x.size())
#define all(a) (a).begin(), (a).end()

void solve(int n, int k, int * arr) {
    int sortedArr[n];
    //copy array
    for(int i = 0; i < n; i++){
        sortedArr[i] = arr[i];
    }
    sort(sortedArr, sortedArr + n);
    int total = 1;
    for(int i = 0; i < n-1; i++){
        if(arr[i] > arr[i+1]){
            total++;
        }
        else{
            if(sortedArr[lower_bound(sortedArr, sortedArr + n, arr[i+1])-sortedArr-1] != arr[i]){
                total++;
            }
        }
    }
    if(total <= k){
        cout << "YES" << endl;
    }
    else{
        cout << "NO" << endl;
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    cin >> tc;
    for (int t = 1; t <= tc; t++) {
        int n;
        int k;
        cin >> n;
        cin >> k;
        int arr[n];
        for(int i = 0; i < n; i++){
            cin >> arr[i];
        }
        solve(n,k,arr);
    }
}


