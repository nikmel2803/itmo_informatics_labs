package Ship;

public class Ship {
    private String title;
    private String captainName;
    private int port;
    private char type;

    public void updateShipInfo(String title) {
        this.title = title;
    }


    public void updateShipInfo(String title, String captainName) {
        this.title = title;
        this.captainName = captainName;
    }

    public void updateShipInfo(String title, String captainName, int port) {
        this.title = title;
        this.captainName = captainName;
        this.port = port;
    }

    public void updateShipInfo(String title, String captainName, int port, char type) {
        this.title = title;
        this.captainName = captainName;
        this.port = port;
        this.type = type;
    }

    @Override
    public String toString() {
        return String.format("title: %s\n" +
                "captainName: %s\n" +
                "port: %d\n" +
                "type: %c", title, captainName, port,type);
    }
}
