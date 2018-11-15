package gift;

public class GiftSharing {
    public static void main(String[] args) {
        Postcard postcard = new Postcard();
        postcard.buy();
        postcard.setWish("Щастя здаровья и т.д.");
        postcard.give("Афанасий");

        Painting painting = new Painting();
        painting.setAuthor("Айвазовский");
        painting.setTitle("Девятый вал");
        painting.buy();
        painting.give("Бориска");
    }
}
