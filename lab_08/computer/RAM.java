package computer;

public class RAM implements Memory {
    private String data = "";

    @Override
    public boolean writeData(String data) {
        this.data += data;
        return true;
    }

    @Override
    public String getData() {
        return data;
    }
}
