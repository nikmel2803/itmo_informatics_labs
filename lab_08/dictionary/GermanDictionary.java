package dictionary;

import java.util.HashMap;

public class GermanDictionary implements Dictionary {
    private HashMap<String, String> dict;

    public GermanDictionary() {
        this.dict = new HashMap<>();
        this.dict.put("hallo", "привет");
        this.dict.put("die welt", "мир");
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
