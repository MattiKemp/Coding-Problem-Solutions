#include <iostream>

using namespace std;

template<int height, int width>
void print(int (&arr)[height][width]){
    for(int i = 0; i < height; i++){
        for(int j = 0; j < height; j++){
            cout << arr[i][j] << ", ";
        }
        cout << endl;
    }
}

// the problem with this solution is that we need to choose
// a flag number that isn't in the array at all, which is somewhat
// hard to figure out without extra storage space.
// What can be done though, is to choose a number that is 
// extremely unlikely, like a huge negatve number.
template<int height, int width>
void solve(int (&arr)[height][width]){
    for(int i = 0; i < height; i++){
        for(int j = 0; j < height; j++){
            if(arr[i][j]==0){
                for(int k = 0; k < height; k++){
                    arr[k][j]=-1;
                }
                for(int k = 0; k < width; k++){
                    arr[i][k]=-1;
                }
            }
        }
    }
    for(int i = 0; i < height; i++){
        for(int j = 0; j < height; j++){
            if(arr[i][j]==-1){
                arr[i][j] = 0;
            }
        }
    }
}

int main(){
    int arr[5][5] = {{1,2,3,4,5},
        {6,0,8,9,10},
        {11,12,13,14,15},
        {16,17,18,0,20},
        {21,22,23,24,25}};
    print(arr);
    solve(arr);
    cout << endl;
    print(arr);
    return 0;
}
