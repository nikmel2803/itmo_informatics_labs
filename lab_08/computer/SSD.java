package computer;

public class SSD implements Memory {
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
