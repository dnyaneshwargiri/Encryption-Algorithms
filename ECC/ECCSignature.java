import java.math.BigInteger;
import java.security.*;
import java.security.spec.*;
import java.util.Arrays;

import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;

public class ECCSignature {
  public static void main(String[] args) throws Exception {
    KeyPairGenerator kpg;
    kpg = KeyPairGenerator.getInstance("EC","SunEC");
    ECGenParameterSpec ecsp;
    ecsp = new ECGenParameterSpec("sect163k1");
    kpg.initialize(ecsp);

    KeyPair kp = kpg.genKeyPair();
    PrivateKey privKey = kp.getPrivate();
    PublicKey pubKey = kp.getPublic();
    System.out.println(privKey.toString());
    System.out.println(pubKey.toString());
    
    String text = "In teaching others we teach ourselves";
    System.out.println("Text: " + text);
    byte[] baText = text.getBytes("UTF-8");
    
    Signature ecdsa;
    ecdsa = Signature.getInstance("SHA1withECDSA","SunEC");
    ecdsa.initSign(privKey);
    
    Cipher cs=Cipher.getInstance("AES");
    byte [] newprivKey=Arrays.copyOf(privKey.getEncoded(), 16);
    SecretKeySpec skp=new SecretKeySpec(newprivKey, "AES");
    cs.init(Cipher.ENCRYPT_MODE,(SecretKey)(skp));
    byte [] dec=cs.doFinal(baText);
    System.out.println("Encrypted text :"+dec);

  
    ecdsa.update(baText);
    byte[] baSignature = ecdsa.sign();
    System.out.println("Signature: " + (new BigInteger(1, baSignature).toString(16)));

    Signature signature;
    signature = Signature.getInstance("SHA1withECDSA","SunEC");
    signature.initVerify(pubKey);
    signature.update(baText);
    boolean result = signature.verify(baSignature);
    System.out.println("Valid: " + result);
    
    cs=Cipher.getInstance("AES");
    newprivKey=Arrays.copyOf(privKey.getEncoded(), 16);
    skp=new SecretKeySpec(newprivKey, "AES");
    cs.init(Cipher.DECRYPT_MODE,(SecretKey)(skp));    
    System.out.println("Decrypted text :"+new String(cs.doFinal(dec)));
  }
}