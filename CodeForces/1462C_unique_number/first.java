import java.util.Scanner;
public class first{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[9];
        for(int i = 0; i < n; i++){
            int curr = sc.nextInt();
            if(curr > 45){
                System.out.println(-1);
            }
            else{
                 arr = new int[]{9,8,7,6,5,4,3,2,1};
                 long power = 1;
                 long smallest = 0;
                 while(curr != 0){
                    boolean found = false;
                    for(int j = 0; j < 9; j++){
                        if(arr[j] != 0 && curr-arr[j] >=0){
                            curr-=arr[j];
                            smallest += power*arr[j];
                            power*=10;
                            arr[j] = 0;
                            found = true;
                            break;
                        }
                    }
                    if(!found){
                        System.out.println(-1);
                        break;
                    }
                 }
                 if(curr==0) System.out.println(smallest);
            }
        }
    }
}
