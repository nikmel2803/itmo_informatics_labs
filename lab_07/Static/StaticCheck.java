package Static;

public class StaticCheck {
    public static void main(String[] args) {
        while(StaticContainer.counter < 100){
            StaticContainer.operation();
        }
        System.out.println(StaticContainer.counter);
    }
}
