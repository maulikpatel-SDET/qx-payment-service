// R3-20 Loads the private key from the PKCS12 keystore committed in qx-key-service.
// Algorithm is taken from the key at runtime - no algorithm name in this file except the keystore type.
package com.qx.payment;

import java.io.FileInputStream;
import java.security.KeyStore;
import java.security.PrivateKey;
import java.security.Signature;

public class KeystoreSigner {
    static final String STORE = "/opt/qx/qx-key-service/keystore/qx-signing.p12";
    static final char[] PASSWORD = "changeit".toCharArray();   // TEST ONLY

    public static byte[] sign(byte[] data) throws Exception {
        KeyStore ks = KeyStore.getInstance("PKCS12");
        try (FileInputStream in = new FileInputStream(STORE)) {
            ks.load(in, PASSWORD);
        }
        PrivateKey key = (PrivateKey) ks.getKey("qx-signing", PASSWORD);
        Signature s = Signature.getInstance("SHA256with" + key.getAlgorithm());
        s.initSign(key);
        s.update(data);
        return s.sign();
    }
}
