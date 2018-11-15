package dictionary;

public class GermanDictionaryFactory implements DictionaryFactory {
    @Override
    public Dictionary getDictionary() {
        return new GermanDictionary();
    }
}
