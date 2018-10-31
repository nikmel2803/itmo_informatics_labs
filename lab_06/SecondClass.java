public class SecondClass {
    public static void main(String[] args) {
        String s = "13.7";
        Double a = new Double(s);
        char c = "qwe".charAt(2); // символ со 2-й позиции
        System.out.println(a);
        System.out.println(c);
        String k = "135";
        Integer iS = new Integer(k);
        System.out.println("1 способ: " + iS);
        int iSS = Integer.parseInt(k);
        System.out.println("2 способ: " + iSS);
        String s1 = "Java is one of the best languages!";
        System.out.println(s1.charAt(4));
        String s2 = "Java is one of the most beautiful languages!";
        System.out.println(s1.equals(s2));
        boolean d = s1.contains("best");
        System.out.println("best is in s1: " + d);
    }
}
