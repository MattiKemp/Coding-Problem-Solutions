import java.util.Scanner;
public class strangelist{
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
			int sum = 0;
			int possibleSum = 0;
			boolean robot = true;
			boolean not = false;
			for(int j = 0; j < n; j++){
				sum+=arr[j];
				if(robot){
					if(arr[j]%x==0){
						int temp = arr[j];
						int count = 1;
						while(temp > 0 && temp%x==0){
							count*=x;
							temp/=x;
							sum+=count*temp;
						}

					}
					else{
						not = true
						robot = false;
					}
				}
			}
			System.out.println(sum);
		}
	}
}
