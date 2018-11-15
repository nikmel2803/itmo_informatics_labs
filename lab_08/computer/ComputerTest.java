package computer;

import java.util.ArrayList;

public class ComputerTest {
    public static void main(String[] args) {
        ArrayList<Keyboard> keyboards = new ArrayList<>();
        keyboards.add(new Keyboard());

        ArrayList<Screen> screens = new ArrayList<>();
        screens.add(new Screen());

        Computer comp = new Computer(
                new CPU(),
                new Bus(),
                new RAM(),
                new SSD(),
                keyboards,
                screens
        );
        comp.getCpu().perform("1+1");
        comp.getScreens().get(0).sendData("daaata");

    }
}
