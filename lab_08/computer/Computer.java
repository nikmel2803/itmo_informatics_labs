package computer;

import java.util.ArrayList;

public class Computer {
    private CPU cpu;
    private Bus bus;
    private RAM ram;
    private SSD disk;
    private ArrayList<Keyboard> keyboards;
    private ArrayList<Screen> screens;

    public Computer(CPU cpu, Bus bus, RAM ram, SSD disk, ArrayList<Keyboard> keyboards, ArrayList<Screen> screens) {
        this.cpu = cpu;
        this.bus = bus;
        this.ram = ram;
        this.disk = disk;
        this.keyboards = keyboards;
        this.screens = screens;
    }

    public CPU getCpu() {
        return cpu;
    }

    public void setCpu(CPU cpu) {
        this.cpu = cpu;
    }

    public Bus getBus() {
        return bus;
    }

    public void setBus(Bus bus) {
        this.bus = bus;
    }

    public RAM getRam() {
        return ram;
    }

    public void setRam(RAM ram) {
        this.ram = ram;
    }

    public SSD getDisk() {
        return disk;
    }

    public void setDisk(SSD disk) {
        this.disk = disk;
    }

    public ArrayList<Keyboard> getKeyboards() {
        return keyboards;
    }

    public void setKeyboards(ArrayList<Keyboard> keyboards) {
        this.keyboards = keyboards;
    }

    public ArrayList<Screen> getScreens() {
        return screens;
    }

    public void setScreens(ArrayList<Screen> screens) {
        this.screens = screens;
    }
}
