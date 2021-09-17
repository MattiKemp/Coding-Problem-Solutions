#include <bits/stdc++.h>

using namespace std;

template<typename A, typename B> ostream& operator<<(ostream &os, const pair<A, B> &p) { return os << '(' << p.first << ", " << p.second << ')'; }
template<typename T_container, typename T = typename enable_if<!is_same<T_container, string>::value, typename T_container::value_type>::type> ostream& operator<<(ostream &os, const T_container &v) { os << '{'; string sep; for (const T &x : v) os << sep << x, sep = ", "; return os << '}'; }
void dbg_out() { cerr << endl; }
template<typename Head, typename... Tail> void dbg_out(Head H, Tail... T) { cerr << ' ' << H; dbg_out(T...); }
#ifdef LOCAL
#define dbg(...) cerr << "(" << #__VA_ARGS__ << "):", dbg_out(__VA_ARGS__)
#else
#define dbg(...)
#endif

#define ar array
#define ll long long
#define ld long double
#define sza(x) ((int)x.size())
#define all(a) (a).begin(), (a).end()

const int MAX_N = 1e5 + 5;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

unsigned long long p2 [64];
int p2Dig [64][19];
void getDigits(unsigned long long num, int* digits){
    int count = 0;
    while(num>0){
        digits[count] = num%10;
        num /= 10;
        count++;
    }
    for(int i = count; i < 18; i++){
        digits[i] = -1;
    }
    // reverse the array up to the first negative
    digits[18] = count;
    int spot = 0;
    count--;
    while(count > spot){
        int temp = digits[spot];
        digits[spot] = digits[count];
        digits[count] = temp;
        count--;
        spot++;
    }
}

void setup(){
    unsigned long long pOf2 = 1;
    for(int i = 0; i < 64; i++){
        p2[i] = pOf2;
        //cout << p2[i] << endl;
        getDigits(p2[i],p2Dig[i]);
        pOf2 *= 2;
        //cout << p2Dig[i][0] << endl;
    }
}

void solve(int tcase) {
    int digits[19];
    getDigits((unsigned long long)tcase, digits);
    //cout << digits[18] << endl;
    int min = 19;
    for(int i = 0; i < 64; i++){
        for(int j = 0; j < 18; j++){
            int spot = 0;
            for(int k = j; k < 10; k++){
                if(digits[k]==-1 || p2Dig[i][spot]==-1){
                    break;
                }
                else if(digits[k]==p2Dig[i][spot]){
                    spot++;
                }
            }
            int diff = p2Dig[i][18] + digits[18] -2*spot;
            if(diff < min){
                min = diff;
                cout << endl;
            }
        }
    }
    cout << min << endl;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    setup();
    int tc = 1;
    cin >> tc;
    for (int t = 1; t <= tc; t++) {
        //cout << "Case #" << t << ": ";
        int testcase;
        cin >> testcase;
        solve(testcase);
    }
}
