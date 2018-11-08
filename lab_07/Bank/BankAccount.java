package Bank;

public class BankAccount {
    private static String holdersName = "Ваня Иванов";
    private String accountNumber;
    private int accountLimit;
    private int currentFund;

    public BankAccount(String accountNumber, int accountLimit, int currentFund) {
        this.accountNumber = accountNumber;
        this.accountLimit = accountLimit;
        this.currentFund = currentFund;
    }

    public static String getHoldersName() {
        return holdersName;
    }

    public static void setHoldersName(String holdersName) {
        BankAccount.holdersName = holdersName;
    }

    public String getAccountNumber() {
        return accountNumber;
    }

    public void setAccountNumber(String accountNumber) {
        this.accountNumber = accountNumber;
    }

    @Override
    public String toString() {
        return String.format("holder\'sName: %s\n" +
                "accountNumber: %s\n" +
                "accountLimit: %d\n" +
                "currentFund: %d\n", getHoldersName(), getAccountNumber(), getAccountLimit(), getCurrentFund());
    }

    public int getAccountLimit() {
        return accountLimit;
    }

    public void setAccountLimit(int accountLimit) {
        this.accountLimit = accountLimit;
    }

    public int getCurrentFund() {
        return currentFund;
    }

    public void setCurrentFund(int currentFund) {
        this.currentFund = currentFund;
    }
}
