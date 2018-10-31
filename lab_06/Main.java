public class Main {
    public static void main(String[] args) {
        hanoi(5, 1, 3);
    }

    public static void hanoi(int n, int i, int j) {
        if (n == 1) System.out.println("переложить " + n + " диск c " + i + " на " + j + " стержнь ");
        else {
            hanoi(n - 1, i, 6 - i - j);
            System.out.println("переложить " + n + " диск c " + i + " на " + j + " стержнь ");
            hanoi(n - 1, 6 - i - j, j);
        }
    }


}
