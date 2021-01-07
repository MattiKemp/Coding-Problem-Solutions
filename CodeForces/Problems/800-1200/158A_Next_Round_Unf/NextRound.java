import java.util.Scanner;
// Since the particpant input is sorted descendingly all we need to 
// is keep track of how many elements before spot k are equal to the score of k
public class NextRound{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int prev = -1;
        int prevSpot = -1;
        int spot;
        for(int i = 0; i < n; i++){
           spot = sc.nextInt();
           if(spot != prev){
               if(spot==0){
                   prevSpot = i;
                   prev = spot;
                   break;
               }
               //prev = spot;
               prevSpot = i;
               if(i > k-1){
                   break;
               }
               else{
                   prev = spot;
               }
           }
           else{
               if(i==n-1){
                   prevSpot = i+1;
                   prev = spot;
               }
           }
        }
        System.out.println(prevSpot);
        System.out.println(prev);
        if(prevSpot > k-1){
            System.out.println(k+(prevSpot-k));
        }
        else{
            System.out.println(k+(prevSpot+1-k));
        }
    }
}

