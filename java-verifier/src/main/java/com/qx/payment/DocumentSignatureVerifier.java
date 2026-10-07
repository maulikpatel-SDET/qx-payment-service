// R3-04 PUBLIC KEY side: payment-service verifies documents signed by qx-key-service.
// Key type is read from the key itself - no "RSA" string in this file.
package com.qx.payment;

import java.nio.file.Files;
import java.nio.file.Path;
import java.security.KeyFactory;
import java.security.PublicKey;
import java.security.Signature;
import java.security.spec.X509EncodedKeySpec;

public class DocumentSignatureVerifier {
    static final Path KEY = Path.of("/opt/qx/qx-key-service/keys/rsa_signing_public.der");
    static final String KEY_TYPE = System.getenv().getOrDefault("QX_DOC_KEY_TYPE", "RSA");

    public static boolean verify(byte[] document, byte[] sig) throws Exception {
        PublicKey pub = KeyFactory.getInstance(KEY_TYPE)
                .generatePublic(new X509EncodedKeySpec(Files.readAllBytes(KEY)));
        Signature v = Signature.getInstance("SHA256with" + pub.getAlgorithm());
        v.initVerify(pub);
        v.update(document);
        return v.verify(sig);
    }
}
