package dictionary;

import java.util.HashMap;

public class FrenchDictionary implements Dictionary{
    private HashMap<String, String> dict;

    public FrenchDictionary() {
        this.dict = new HashMap<>();
        this.dict.put("salut", "привет");
        this.dict.put("le monde", "мир");
    }

    @Override
    public boolean translateWord(String word) {
        String translatedWord = dict.get(word);
        if (translatedWord != null) {
            System.out.println(String.format("Перевод слова %s -- %s", word, translatedWord));
            return true;
        }
        return false;
    }
}
