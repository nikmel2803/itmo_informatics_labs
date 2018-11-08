// Алгоритм:
// https://courses.openedu.ru/assets/courseware/v1/322c885e7b64fc33531228c16f37585d/asset-v1:ITMOUniversity+DIGCUL+summer_2018+type@asset+block/Ib_lecture.pdf

import java.math.BigInteger;

public class Crypt {
    public static void main(String[] args) {
        int p = 43, q = 61;
        int n = p * q; //2623
        int phi = (p - 1) * (q - 1); //2520
        int e = 11;
        int d = 2291;
        // {e, n} - public key
        // {d, n} - private key

        // encryption
        String originalMess = "Привет как дела?";
        System.out.println("originalMess: " + originalMess);

        StringBuilder encResult = new StringBuilder();
        for (char ch : originalMess.toCharArray()) {
            BigInteger r = BigInteger.valueOf((int) ch);
            BigInteger c = r.pow(e).mod(BigInteger.valueOf(n));
            encResult.append(c).append(" ");
        }
        System.out.println("encryptedMess: " + encResult);

        // decryption
        StringBuilder decrRes = new StringBuilder();
        for (String c : encResult.toString().split(" ")) {
            BigInteger x = new BigInteger(c);
            x = x.pow(d).mod(BigInteger.valueOf(n));
            decrRes.append((char) x.intValue());
        }
        System.out.println("decryptedMess: " + decrRes);

    }
}