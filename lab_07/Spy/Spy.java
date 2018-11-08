package Spy;

public class Spy {
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getRealName() {
        return realName;
    }

    public void setRealName(String realName) {
        this.realName = realName;
    }

    public int getSquad() {
        return squad;
    }

    public void setSquad(int squad) {
        this.squad = squad;
    }

    public String name;
    private String realName;
    private int squad;

    private String getSpyInfo() {
        return String.format("name: %s\nreal name: %s\nsquad: %d", getName(), getRealName(), getSquad());
    }

    public void print() {
        System.out.println(getSpyInfo());
    }
}
