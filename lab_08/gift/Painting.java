package gift;

public class Painting extends Gift {
    private String title;
    private String author;

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }


    @Override
    void buy() {
        System.out.println("Картина куплена. Название: "+getTitle()+", автор: " + getAuthor());
    }

    @Override
    void give(String name) {
        System.out.println("Картина подарена. Получатель: " + name);
    }
}
