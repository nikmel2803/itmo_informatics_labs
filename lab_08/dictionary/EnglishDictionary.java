package dictionary;

import java.util.HashMap;

public class EnglishDictionary implements Dictionary {
    private HashMap<String, String> dict;

    public EnglishDictionary() {
        this.dict = new HashMap<>();
        this.dict.put("hello", "привет");
        this.dict.put("word", "мир");
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
