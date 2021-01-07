import java.util.Scanner;
import java.lang.Math;
public class strangepartition{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		for(int i = 0; i < num; i++){
			int n = sc.nextInt();
			int x = sc.nextInt();
			int[] arr = new int[n];
			for(int j = 0; j < n; j++){
				arr[j] = sc.nextInt();
			}
			int max = 0;
			for(int j = 0; j < n; j++){
				max += Math.ceil(arr[j]/((double)x));
			}
			int min = 0;
			int spot =0;
			while(spot < n){
				if(arr[spot]%x!=0){
					if(spot < n-1 && arr[spot+1]%x!=0){
						arr[spot] += arr[spot+1];
						arr[spot+1] = 0;
					}
				}
				spot+=1;
			}
			for(int j = 0; j < n; j++){
				min += Math.ceil(arr[j]/((double)x));
			}
			System.out.print(min +" ");
			System.out.println(max);
		}
	}
}
