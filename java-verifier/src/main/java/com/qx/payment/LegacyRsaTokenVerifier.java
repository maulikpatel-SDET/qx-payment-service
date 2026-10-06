// CR-04  MIGRATION GAP: qx-key-service now signs tokens with ML-DSA-65 (TokenIssuer.java),
// but this verifier in qx-payment-service was never updated and still uses RSA.
package com.qx.payment;

import java.nio.file.Files;
import java.nio.file.Path;
import java.security.KeyFactory;
import java.security.PublicKey;
import java.security.Signature;
import java.security.spec.X509EncodedKeySpec;

public class LegacyRsaTokenVerifier {
    static final Path KEY = Path.of("/opt/qx/qx-key-service/keys/rsa_signing_public.der");

    public static boolean verify(byte[] token, byte[] sig) throws Exception {
        PublicKey pub = KeyFactory.getInstance("RSA")
                .generatePublic(new X509EncodedKeySpec(Files.readAllBytes(KEY)));
        Signature v = Signature.getInstance("SHA256withRSA");
        v.initVerify(pub);
        v.update(token);
        return v.verify(sig);
    }
}
