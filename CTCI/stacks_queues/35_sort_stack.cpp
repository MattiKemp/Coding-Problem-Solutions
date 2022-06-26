#include "../../../Data-Structures-And-Algorithms/Common/c++/data_structures/lists/stack.cpp"
#include <iostream>

/* problem: Write a program to sort a stack such that the smallest items are on the top. You can use an additional temporary stack, but you may not copy the elementes into any other data structure (such as an array). The stack supports the following operations: push, pop, peek, isEmpty */

void solution(){
    stack<int> input_stack = stack<int>();
    input_stack.insert(1);
    input_stack.insert(3);
    input_stack.insert(9);
    input_stack.insert(22);
    input_stack.insert(4);
    input_stack.insert(4);
    input_stack.print();
    stack<int> second = stack<int>();
    int curr_max = -999999;
    int sorted_size = 0;
    while(sorted_size < input_stack.get_size() + second.get_size()){
        int curr_size = input_stack.get_size() - sorted_size;
        bool max_found = false;
        for(int i = 0; i < curr_size; i++){
            int popped = input_stack.pop();
            if(popped > curr_max){
                if(max_found){
                    second.insert(curr_max);
                }
                curr_max = popped;
                max_found = true;
            }
            else{
                second.insert(popped);
            }
        }
        input_stack.insert(curr_max);

        for(int i = 0; i < curr_size-1; i++){
            input_stack.insert(second.pop());
        }
        sorted_size++;    
        curr_max = -9999999;
    }
    input_stack.print();
}


int main(){
    cout << "35 sort_stack solution" << endl;
//    stack<int> input_stack = stack<int>();
//    input_stack.insert(1);
//    input_stack.insert(3);
//    input_stack.insert(9);
//    input_stack.insert(22);
//    input_stack.insert(4);
//    input_stack.print();
//    input_stack.pop();
//    input_stack.pop();
//    input_stack.pop();
//    input_stack.pop();
//    input_stack.pop();
//    input_stack.insert(1);
//    input_stack.print();
    //input_stack.pop();
    solution();
    return 0;
}
