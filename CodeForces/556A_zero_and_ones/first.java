import java.util.Scanner;
public class first{
    /*
     * The problem boils down to comparing how many zeros and ones there are.
     * This is because if there exists any amount of zeross in a string of ones, there will be atleast 1 zero
     * next to a one. 
     * Once this pair is removed there will be again atleast 1 zero next to a one, this repeats
     * till there are no zeros or no ones left in the string. So we can simplify the problem to:
     * count number of ones and the number of zeros in the string, then return abs(zero-one).
     */
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String binary = sc.next();
        int zero = 0;
        int one = 0;
        for(int i = 0; i < n; i++){
            if(binary.charAt(i)=='0'){
                zero++;
            }
            else{
                one++;
            }
        }
        if(zero < one){
            System.out.println(one-zero);
            return;
        }
        System.out.println(zero-one);
        return;
    }
}
