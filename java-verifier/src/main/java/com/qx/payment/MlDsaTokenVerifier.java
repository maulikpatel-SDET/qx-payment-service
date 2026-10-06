// CR-03  Verifies with the ML-DSA-65 public key GENERATED in qx-key-service. Should be PQC safe.
package com.qx.payment;

import java.nio.file.Files;
import java.nio.file.Path;
import java.security.KeyFactory;
import java.security.PublicKey;
import java.security.Security;
import java.security.Signature;
import java.security.spec.X509EncodedKeySpec;

import org.bouncycastle.jce.provider.BouncyCastleProvider;

public class MlDsaTokenVerifier {
    static final Path KEY = Path.of("/opt/qx/qx-key-service/keys/mldsa_public.key");

    public static boolean verify(byte[] token, byte[] sig) throws Exception {
        Security.addProvider(new BouncyCastleProvider());
        PublicKey pub = KeyFactory.getInstance("ML-DSA", "BC")
                .generatePublic(new X509EncodedKeySpec(Files.readAllBytes(KEY)));
        Signature v = Signature.getInstance("ML-DSA", "BC");
        v.initVerify(pub);
        v.update(token);
        return v.verify(sig);
    }
}
