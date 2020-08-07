import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        System.out.print(fibonacci(N));
    }

    public static long fibonacci (int n) {
        long first = 0;
        long second = 1;

        if(n == first) {
            return first;
        }
        else if(n == second) {
            return second;
        }
        else {
            long result = 0;
            for(int i = 2; i < n + 1; i++) {
                result = first + second;
                first = second;
                second = result;
            }
            return result;
        }
    }
}
