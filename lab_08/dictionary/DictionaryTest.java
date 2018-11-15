package dictionary;

public class DictionaryTest {
    public static void main(String[] args) {
        Dictionary english =  new EnglishDictionaryFactory().getDictionary();
        english.translateWord("hello");
        english.translateWord("abracadabra");

        Dictionary french =  new FrenchDictionaryFactory().getDictionary();
        french.translateWord("salut");

        Dictionary german =  new GermanDictionaryFactory().getDictionary();
        german.translateWord("hallo");
    }
}
