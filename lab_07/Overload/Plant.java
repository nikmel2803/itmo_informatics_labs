package Overload;

public class Plant {
    private String type;
    private String color;
    private String existenceArea;
    private boolean rare;

    public Plant(String type, String color, String existenceArea, boolean rare) {
        this.type = type;
        this.color = color;
        this.existenceArea = existenceArea;
        this.rare = rare;
    }

    public Plant(String type, String color, String existenceArea) {
        this.type = type;
        this.color = color;
        this.existenceArea = existenceArea;
    }


    public Plant() {
    }

    public Plant(String type, String color) {
        this.type = type;
        this.color = color;
    }

    public Plant(String type) {
        this.type = type;
    }

    public void print() {
        System.out.println("type: " + this.type + "; color: " + this.color +
                "; existenceArea: " + this.existenceArea + "; rare: " + this.rare);
    }
}
