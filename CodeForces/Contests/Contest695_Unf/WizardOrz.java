import java.util.Scanner;
import java.lang.StringBuilder;
public class WizardOrz{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        sc.nextLine();
        StringBuilder sb = new StringBuilder(201000);
        int spot = 0;
        while(t > 0){
            int n = sc.nextInt();
            int start = 9;            
            for(int i = 0; i < n; i++){
                sb.append(start);
                start--;
                if(start == -1)
                    start = 9;
            }
            System.out.println(sb.substring(spot,sb.length()));
            spot+=n;
            t--;
            sc.nextLine();
        }
    }
}

