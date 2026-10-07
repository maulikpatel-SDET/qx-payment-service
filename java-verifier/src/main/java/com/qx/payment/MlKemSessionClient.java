// R3-07 SENDER side: payment-service encapsulates a session key to key-service's ML-KEM-768 public key.
package com.qx.payment;

import java.nio.file.Files;
import java.nio.file.Path;
import java.security.KeyFactory;
import java.security.PublicKey;
import java.security.SecureRandom;
import java.security.Security;
import java.security.spec.X509EncodedKeySpec;
import javax.crypto.KeyGenerator;

import org.bouncycastle.jcajce.SecretKeyWithEncapsulation;
import org.bouncycastle.jcajce.spec.KEMGenerateSpec;
import org.bouncycastle.jce.provider.BouncyCastleProvider;

public class MlKemSessionClient {
    static final Path KEY = Path.of("/opt/qx/qx-key-service/keys/mlkem_public.key");

    public static SecretKeyWithEncapsulation newSession() throws Exception {
        Security.addProvider(new BouncyCastleProvider());
        PublicKey pk = KeyFactory.getInstance("ML-KEM", "BC")
                .generatePublic(new X509EncodedKeySpec(Files.readAllBytes(KEY)));
        KeyGenerator kg = KeyGenerator.getInstance("ML-KEM", "BC");
        kg.init(new KEMGenerateSpec(pk, "AES"), new SecureRandom());
        return (SecretKeyWithEncapsulation) kg.generateKey();
    }
}
