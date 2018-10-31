import java.util.Arrays;

public class ThirdClass {
    public static void main(String[] args) {
        double[] arr = {0.5, 1.3, 2.7, 0.2};
        Arrays.sort(arr);
        System.out.println(Arrays.toString(arr));
        System.out.println(arr[2]);
        System.out.println(arr.length);
        String s = "Peter Piper picked a peck of pickled peppers";
        String[] stringArray = s.split(" ");
        System.out.println(Arrays.toString(stringArray));
        System.out.println("5 element: " + stringArray[4]);
        Arrays.sort(stringArray);
        System.out.println(Arrays.toString(stringArray));
        boolean n = Arrays.asList(stringArray).contains("peppers");
        System.out.println("peppers is in stringArray: " + n);
    }
}
