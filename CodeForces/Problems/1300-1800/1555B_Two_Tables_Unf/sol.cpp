#include <bits/stdc++.h>
#include <string>
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



void solve(int w, int h, int x1, int y1, int x2, int y2, int width, int height) {
    if(w-(x2-x1) < width || h-(y1-y1) < height){
        cout << -1 << endl;
    }
    // calculate the minimum gaps on each side of the table.
    int minHori = min(x1,w-x2);
    int minVert = min(y1,h-y2);
    // calculate the maximum gaps on each side of the table, whatever isn't the minimum
    int maxHori = max(x1,w-x2);
    int maxVert = max(y1,h-y2);
    int horizontalShift = -1;
    if(w-(x2-x1) >= width){
        width-maxHori;
    }

}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    cin >> tc;
    for (int t = 1; t <= tc; t++) {
        int w;
        int h;
        cin >> w;
        cin >> h;
        int x1;
        int y1;
        int x2;
        int y2;
        cin >> x1;
        cin >> y1;
        cin >> x2;
        cin >> y2;
        //cout << x1 << " " << y1 << " " << x2 << " " << y2;
        int width;
        int height;
        cin >> width;
        cin >> height;
        solve(w,h,x1,y1,x2,y2,width,height);
    }
}
