public class FifthClass {
    public static void main(String[] args) {
        Planet planet = new Planet("Earth-01", 6371.0, 149.6);
        System.out.println(planet.name);
        planet.setName("Earth");
        System.out.println(planet.getName());
        System.out.println(planet.toThousandKm("radius"));
        Satellite a = new Satellite("Moon", 345.2, 1.02);
        System.out.println("period in year: "+a.getPeriod());
        System.out.println("period in days: "+a.getPeriodInDays());
        a.print();
    }
}
