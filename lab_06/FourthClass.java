public class FourthClass {
    public static void main(String[] args) {
        for (int i = 0; i < 30; i++) {
            if (i % 2 == 0) {
                double d = (double) i / 4;
                System.out.print(d + "; "); // вывод в одну строку
            }
        }
        System.out.println();
        int year = 2016;
        switch (year) {
            case 2014:
                System.out.println("You're 3rd year student");
                break;
            case 2015:
                System.out.println("You're 2nd year student");
                break;
            case 2016:
                System.out.println("You're 1st year student");
                break;
        }

        System.out.println("R = x1 & x2 | x3");
        System.out.println("Таблица истинности");
        System.out.println("x1 x2 x3  R");
        func(false, false, false);
        func(false, false, true);
        func(false, true, false);
        func(false, true, true);
        func(true, false, false);
        func(true, false, true);
        func(true, true, false);
        func(true, true, true);
        System.out.println();
        for (int i = 0; i < 130; i++) {
            if (i > (23 * 3)) break;
            if (i % 7 == 0)
                System.out.print(i + " ");

        }
    }

    public static void func(boolean x1, boolean x2, boolean x3) {
        System.out.println((x1 ? "1 " : "0 ") + (x2 ? "1 " : "0 ") + (x3 ? "1 " : "0 ") + (x1 & x2 | x3 ? " 1" : " 0"));
    }

}
