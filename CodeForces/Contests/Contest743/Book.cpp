#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define ld long double
#define sza(x) ((int)x.size())
#define all(a) (a).begin(), (a).end()


void solve(int n, vector<vector<int>> &adjList) {
    // reverse the graph
    vector<vector<int>> newGraph;
    for(int i = 0; i < n; i++){
        vector<int> newList;
        newGraph.push_back(newList);
    }
    for(int i = 0; i < n; i++){
        for(int j = 0; j < adjList[i].size(); j++){
            newGraph[adjList[i][j]].push_back(i);
        }
    }
    bool noReqFound = false;
    for(int i = 0; i < n; i++){
        if(newGraph[i].size()==0){
            noReqFound = true;
            break;
        }
    }
    if(!noReqFound){
        cout << -1 << endl;
    }
    cout << -2 << endl;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    cin >> tc;
    for (int t = 1; t <= tc; t++) {
        int n;
        cin >> n;
        vector<vector<int>> adjList;
        for(int i = 0; i < n; i++){
            int neighborN;
            cin >> neighborN;
            vector<int> neighbors;
            for(int j = 0; j < neighborN; j++){
                int neighbor;
                cin >> neighbor;
                neighbors.push_back(neighbor);
            }
            adjList.push_back(neighbors);
        }
        solve(n, adjList);
    }
}


