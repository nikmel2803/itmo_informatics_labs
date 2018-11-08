package Bank;

public class BankTest {
    public static void main(String[] args) {
        BankAccount acc1 = new BankAccount("2342234", 2000, 0);
        BankAccount acc2 = new AccountOne("2345113", 4000,
                1000, "05.10.2053", 0.53);
        System.out.println(acc1);
        System.out.println(acc2);
    }
}
