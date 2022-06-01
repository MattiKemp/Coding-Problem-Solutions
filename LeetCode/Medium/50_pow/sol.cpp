// This problem is really rough and has bad documentation.
// The majority of the problem is dealing with strange error handling given the documented output restrictions. 
// Solutions in other languages that don't have integer limits are much cleaner as the positive and negative integer limits are where the majority of issues come up. 
class Solution{
    public:
        double myPow(double x, int n){ 
            if(n==0){
                return 1;
            }   
            int temp_n = -1*(n<0) + 1*(n>0);
            std::pair<int,double> delta_n_arr[32] = {{temp_n, x}};
            int arr_ptr = 0;
            bool is_pos = n > 0;
            while(temp_n != n){ 
            if((is_pos && abs(delta_n_arr[arr_ptr].first) <= 2147483647-abs(temp_n) && temp_n + delta_n_arr[arr_ptr].first <= n) || (!is_pos && temp_n + delta_n_arr[arr_ptr].first >= -2147483648 && temp_n + delta_n_arr[arr_ptr].first >= n)) { 
                temp_n += delta_n_arr[arr_ptr].first;
                x *= delta_n_arr[arr_ptr].second;
                arr_ptr++;
                delta_n_arr[arr_ptr] = {temp_n, x};
            }   
            else{
                arr_ptr--; 
            }
        }   
        if(is_pos){
            return x;
        }
        return 1/x;
    }   
};
