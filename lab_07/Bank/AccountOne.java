package Bank;

public class AccountOne extends BankAccount {
    private String expirationDate;

    public String getExpirationDate() {
        return expirationDate;
    }

    public void setExpirationDate(String expirationDate) {
        this.expirationDate = expirationDate;
    }

    public double getPercent() {
        return percent;
    }

    public void setPercent(double percent) {
        this.percent = percent;
    }

    private double percent;

    public AccountOne(String accountNumber, int accountLimit, int currentFund, String expirationDate, double percent) {
        super(accountNumber, accountLimit, currentFund);
        this.expirationDate = expirationDate;
        this.percent = percent;
    }

    @Override
    public String toString() {
        return super.toString()+String.format("expirationDate: %s\n" +
                "percent: %f", getExpirationDate(), getPercent());
    }
}
