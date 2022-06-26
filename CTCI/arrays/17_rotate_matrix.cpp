#include <iostream>

using namespace std;

template <int height, int width>
void print(int (&arr)[height][width]){
    for(int i = 0; i < height; i++){
        for(int j = 0; j < width; j++){
            cout << arr[i][j] << ", ";
        }
        cout << endl;
    }
}

template <int height, int width>
void solve(int (&arr)[height][width]){
    int temp;
    for(int i = 0; i < height/2; i++){
        for(int j = 0; j < width; j++){
            temp = arr[i][j];
            arr[i][j] = arr[height-i-1][j];
            arr[height-i-1][j] = temp;
        }
    }
    for(int i = 0; i < height; i++){
        for(int j = 0; j < width-i; j++){
            temp = arr[i][j];
            arr[i][j] = arr[height-j-1][width-i-1];
            arr[height-j-1][width-i-1] = temp;
        }
    }
}

int main(){
    cout << "rotate matrix solution" << endl;
    int arr[5][5] = {{1,2,3,4,5},
        {6,7,8,9,10},
        {11,12,13,14,15},
        {16,17,18,19,20},
        {21,22,23,24,25}};
    print(arr);
    solve(arr);
    cout << endl;
    print(arr);

    return 0;
}
