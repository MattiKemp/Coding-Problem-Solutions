#include <bits/stdc++.h>
#include <vector>

using namespace std;

#define ll long long
#define ld long double
#define sza(x) ((int)x.size())
#define all(a) (a).begin(), (a).end()

int primes[12] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};
bool pDNumComp[1000];

bool isComposite(int n){
    for(int i = 0; i < 12; i++){
        if(n%primes[i]==0 && n!=primes[i]){
            return true;
        }
    }
    return false;
}

void setup(){
    // generate all 1-3 digit prime digt numbers (only prime digits).
    vector<int> pDNums;
    pDNums.push_back(2);
    pDNums.push_back(3);
    pDNums.push_back(5);
    pDNums.push_back(7);
    int prevSize = 0;
    int currentSize = 4;
    for(int k = 0; k < 1; k++){
        for(int i = prevSize; i < currentSize; i++){
            int pow10 = (int)pow(10,k+1);
            pDNums.push_back(2*pow10 + pDNums[i]);
            pDNums.push_back(3*pow10 + pDNums[i]);
            pDNums.push_back(5*pow10 + pDNums[i]);
            pDNums.push_back(7*pow10 + pDNums[i]);
        }
        prevSize = currentSize;
        currentSize = pDNums.size();
    }
    for(int i = 4; i < pDNums.size(); i++){
        if(isComposite(pDNums[i])){
            pDNumComp[pDNums[i]]=true;
        }
    }
}

// used to check all three digit values
void checkAllThreeDigit(){
    vector<int> pDNums;
    pDNums.push_back(2);
    pDNums.push_back(3);
    pDNums.push_back(5);
    pDNums.push_back(7);
    int prevSize = 0;
    int currentSize = 4;
    for(int k = 0; k < 2; k++){
        for(int i = prevSize; i < currentSize; i++){
            int pow10 = (int)pow(10,k+1);
            pDNums.push_back(2*pow10 + pDNums[i]);
            pDNums.push_back(3*pow10 + pDNums[i]);
            pDNums.push_back(5*pow10 + pDNums[i]);
            pDNums.push_back(7*pow10 + pDNums[i]);
        }
        prevSize = currentSize;
        currentSize = pDNums.size();
    }
//    for(int i = 0; i < pDNums.size(); i++){
//        cout << pDNums[i] << endl;
//    }
    // check to see if all the 3 digits values are composite in some way.
    for(int i = prevSize; i < currentSize; i++){
        bool found = false;
        //cout << pDNums[i] << endl;
        //if(isComposite(pDNums[i])){
        //    found = true;
        //}
        //cout << pDNums[i] << endl;
        //cout << pDNums[i] - (pDNums[i]/100)*100 << endl;
        if(isComposite(pDNums[i] - (pDNums[i]/100)*100)){
            found = true;
        }
        //cout << pDNums[i]/10 - ((pDNums[i]/10)%10) + pDNums[i]%10 << endl;
        if(isComposite(pDNums[i]/10 - ((pDNums[i]/10)%10) + pDNums[i]%10)){
            found = true;
        }
        //cout << pDNums[i]/10 << endl;
        if(isComposite(pDNums[i]/10)){
            found = true;
        }
        if(!found){
            cout << "failed for: " << pDNums[i] << endl;
        }
    }
}

void solve(int k, int * arr) {
    int curr = 0;
    for(int i = 0; i < k; i++){
        curr = arr[i]*10;
        for(int j = i+1; j < k; j++){
            if(pDNumComp[curr+arr[j]]){
                cout << 2 << endl;
                cout << curr+arr[j] << endl;
                return ;
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    //checkAllThreeDigit();
    setup();
    int tc = 1;
    cin >> tc;
    for (int t = 1; t <= tc; t++) {
        int k;
        cin >> k;
        int arr[k];
        char tempArr[k];
        cin >> tempArr;
        bool found = false;
        for(int i = 0; i < k; i++){
            arr[i] = tempArr[i]-'0';
            if(arr[i]==1 || arr[i]==4 || arr[i]==6 || arr[i]==8 || arr[i]==9){
                cout << 1 << endl;
                cout << arr[i] << endl;
                found = true;
                break;
            }
        }
        if(!found){
            solve(k, arr);
        }
    }
}
