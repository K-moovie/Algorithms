package Algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class BOJ_1904 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int d[] = new int[n+1];
        d[0] = 0; d[1] = 1; d[2] = 2;
        for(int i=3;i<=n;i++){
            d[i] = d[i-2] + d[i-1];
            d[i]%=15746;
        }
        System.out.print(d[n]);
    }
}