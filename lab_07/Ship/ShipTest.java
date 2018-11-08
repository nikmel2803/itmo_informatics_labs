package Ship;

public class ShipTest {
    public static void main(String[] args) {
        Ship ship = new Ship();
        ship.updateShipInfo("Volga", "Pasha", 23, 'c');

        Ship ship1 = new Ship();
        ship1.updateShipInfo("Volga", "Pasha", 23);

        Ship ship2 = new Ship();
        ship2.updateShipInfo("Volga", "Pasha");

        Ship ship3 = new Ship();
        ship3.updateShipInfo("Volga");

        System.out.println(ship);
        System.out.println(ship1);
        System.out.println(ship2);
        System.out.println(ship3);
    }
}
