package Program.Pattern;

import java.util.Scanner;

public class diamond {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 1; i <= n; i++) {
            System.out.println(" ".repeat(n - i) + "* ".repeat(i));
        }
        for (int j = n - 1; j >= 1; j--) {
            System.out.println(" ".repeat(n - j) + "* ".repeat(j));
        }

        sc.close();
    }
}
