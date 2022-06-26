// Optimal solution:
// Runtime: O(n^2) (n x n matrix)
// Space: O(1) (not including input matrix) ie it is in place.
void rotate(vector<vector<int>>& matrix) {
    int temp;
    int height = matrix.size();
    int width = matrix.size();
    for(int i = 0; i < height/2; i++){
        for(int j = 0; j < width; j++){
            temp = matrix[i][j];
            matrix[i][j] = matrix[height-i-1][j];
            matrix[height-i-1][j] = temp;
        }   
    }   
    for(int i = 0; i < height; i++){
        for(int j = 0; j < i; j++){
            temp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = temp;
        }   
    }
}
