package computer;

public class CPU implements ProcessingUnit {
    @Override
    public boolean perform(String command) {
        System.out.println("CPU is working!");
        return true;
    }
}
