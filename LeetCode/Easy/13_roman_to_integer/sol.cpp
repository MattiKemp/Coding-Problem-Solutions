class Solution {
public:
    int romanToInt(string s) {
        int conv_int = 0;
        for(int i = 0; i < s.size(); i++){
        char curr = s.at(i);
        if(curr=='M'){
                                conv_int += 1000;
                                            }
                        else if(curr=='D'){
                                            conv_int += 500;
                                                        }
                                    else if(curr=='C'){
                                                        if(i < s.size()-1){
                                                                                if(s.at(i+1)=='M'){
                                                                                                            conv_int += 900;
                                                                                                                                    i++; 
                                                                                                                                                            continue;
                                                                                                                                                                                }
                                                                                                    else if(s.at(i+1)=='D'){
                                                                                                                                conv_int += 400;
                                                                                                                                                        i++;
                                                                                                                                                                                continue;
                                                                                                                                                                                                    }
                                                                                                                    }
                                                                        conv_int += 100;
                                                                                    }
                                                else if(curr=='L'){
                                                                    conv_int += 50;
                                                                                }
                                                            else if(curr=='X'){
                                                                                if(i < s.size()-1){
                                                                                                        if(s.at(i+1)=='C'){
                                                                                                                                    conv_int += 90;
                                                                                                                                                            i++;
                                                                                                                                                                                    continue;
                                                                                                                                                                                                        }
                                                                                                                            else if(s.at(i+1)=='L'){
                                                                                                                                                        conv_int += 40;
                                                                                                                                                                                i++;
                                                                                                                                                                                                        continue;
                                                                                                                                                                                                                            }
                                                                                                                                            }
                                                                                                conv_int += 10;
                                                                                                            }
                                                                        else if(curr=='V'){
                                                                                            conv_int += 5;
                                                                                                        }
                                                                                    else if(curr=='I'){
                                                                                                        if(i < s.size()-1){
                                                                                                                                if(s.at(i+1)=='X'){
                                                                                                                                                            conv_int += 9;
                                                                                                                                                                                    i++;
                                                                                                                                                                                                            continue;
                                                                                                                                                                                                                                }
                                                                                                                                                    else if(s.at(i+1)=='V'){
                                                                                                                                                                                conv_int += 4;
                                                                                                                                                                                                        i++;
                                                                                                                                                                                                                                continue;
                                                                                                                                                                                                                                                    }
                                                                                                                                                                    }
                                                                                                                        
                                                                                                                        conv_int += 1;
                                                                                                                                    }
                                                                                            }
return conv_int;
}
};
