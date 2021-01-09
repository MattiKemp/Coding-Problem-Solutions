import java.util.Scanner;
public class HillsValleys{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for(int j = 0; j < t; j++){
            int n = sc.nextInt();
            int intim = 0;
            int[] list = new int[n];
            for(int i = 0; i < n; i++){
                list[i] = sc.nextInt();
            }
            sc.nextLine();
            int[] newList = new int[n];
            for(int i = 1; i < n-1; i++){
                if(list[i] > list[i-1] && list[i] > list[i+1]){
                    newList[i] = list[i];
                    intim++;
                }
                else if(list[i] < list[i-1] && list[i] < list[i+1]){
                    newList[i] = -(1*list[i]);
                    intim++;
                }
                //System.out.print(newList[i] + ",");
            }
            //System.out.println(intim);
            if(intim == 0)
                System.out.println(0);
            else{
                boolean found = false;
                boolean broke = false;
                for(int i = 2; i < n-2; i++){
                    if(newList[i]!=0){
                        if((newList[i-1]!=0 && newList[i+1]!=0))
                            if((newList[i-1] == newList[i+1]) || (newList[i-1] < 0 && newList[i+1] <0)|| (newList[i-1] > 0 && newList[i+1] > 0)){
                                intim-=3;
                                System.out.println(intim);
                                broke = true;
                                break;
                        }
                        else if(newList[i-1]!=0 || newList[i+1]!=0){
                            found = true;
                        }
                    }
                }
                if(!broke && found && intim>1){
                    intim-=2;
                    System.out.println(intim);
                }
                else if(!broke){
                    intim-=1;
                    System.out.println(intim);
                }
            }
        }
    }
}
