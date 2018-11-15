package computer;

public class Screen implements IODevice {
    @Override
    public String read() {
        return null;
    }

    @Override
    public void sendData(String data) {
        System.out.println("Получены данные");
    }
}
