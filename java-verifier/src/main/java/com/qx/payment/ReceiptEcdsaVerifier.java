// R3-05 PUBLIC KEY side: payment-service (Java) verifies ECDSA receipts signed in qx-key-service (Python).
package com.qx.payment;

import java.nio.file.Files;
import java.nio.file.Path;
import java.security.KeyFactory;
import java.security.PublicKey;
import java.security.Signature;
import java.security.spec.X509EncodedKeySpec;

public class ReceiptEcdsaVerifier {
    static final Path KEY = Path.of("/opt/qx/qx-key-service/keys/ec_signing_public.der");

    public static boolean verify(byte[] receipt, byte[] sig) throws Exception {
        PublicKey pub = KeyFactory.getInstance("EC")
                .generatePublic(new X509EncodedKeySpec(Files.readAllBytes(KEY)));
        Signature v = Signature.getInstance("SHA256withECDSA");
        v.initVerify(pub);
        v.update(receipt);
        return v.verify(sig);
    }
}
