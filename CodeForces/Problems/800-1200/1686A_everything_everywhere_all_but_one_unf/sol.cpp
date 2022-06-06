#include <bits/stdc++.h>
//#include <iostream>

using namespace std;

#define ll long long
#define ld long double

const int MAX_N = 1e5 + 5;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

void solve(int * nums, int intn){
    //cout << intn << endl;
    //cout << nums[0] << endl;
    int mean = 0;
    bool equal = true;
    for(int i = 0; i < intn; i++){
        mean += nums[i]; 
        if(i > 0 && nums[i] != nums[i-1]){
            equal = false;
        }
    }
    if(equal){
        cout << "YES" << endl;
        return;
    }
    //////cout << mean << endl;
    for(int i = 0; i < intn; i++){
        int temp_n = mean-nums[i];
        bool once = false;
        while(temp_n % (intn-1) == 0 && temp_n > (intn-1)){
            temp_n /= (intn-1);
            once = true; 
        }
        if(once && temp_n == nums[i]){
            cout << "YES" << endl;
            ////////cout << nums[i] << endl;
            return;
        }
    }
    cout << "NO" << endl;
    return;
}


int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    //freopen("output.txt", "w", stdout);
    //freopen("input.txt", "r", stdin); 
    int tc = 1;
    cin >> tc;

    int intn;
    for (int t = 1; t <= tc; t++) {
        ////cout << "Case #" << t << ": ";
        cin >> intn;
        int nums[intn];
        for(int j=0; j<intn; j++){
            cin >> nums[j];
        }
        solve(nums, intn);
    }   
}

