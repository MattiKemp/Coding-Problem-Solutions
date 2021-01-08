import java.util.Scanner;
public class EvenOdds{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        long k = sc.nextLong();
        long oddNum = n/2;
        if(n%2==1)
            oddNum++;
        if(k <= oddNum)
            System.out.println(2*k-1);
        else
            System.out.println(2*(k-oddNum)); 
    }
}
