package gift;

public class Postcard extends Gift {
    private String wish;

    public String getWish() {
        return wish;
    }

    public void setWish(String wish) {
        this.wish = wish;
    }

    @Override
    void buy() {
        System.out.println("Открытка куплена");
    }

    @Override
    void give(String name) {
        System.out.println("Открытка подарена. Получатель: " + name + ". Пожелание: " + getWish());
    }
}
