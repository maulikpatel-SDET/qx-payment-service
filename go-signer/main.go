// CR-02  Go service signs with the ECDSA key GENERATED in qx-key-service.
// Uses the generic crypto.Signer interface - no "ecdsa" or "elliptic" import.
// Algorithm is only known from the key file.
package main

import (
	"crypto"
	"crypto/rand"
	"crypto/sha256"
	"crypto/x509"
	"encoding/pem"
	"fmt"
	"os"
)

const keyPath = "/opt/qx/qx-key-service/keys/ec_signing_private.pem"

func main() {
	raw, err := os.ReadFile(keyPath)
	if err != nil {
		panic(err)
	}
	block, _ := pem.Decode(raw)
	parsed, err := x509.ParsePKCS8PrivateKey(block.Bytes)
	if err != nil {
		panic(err)
	}
	signer := parsed.(crypto.Signer)
	digest := sha256.Sum256([]byte("settlement batch"))
	sig, err := signer.Sign(rand.Reader, digest[:], crypto.SHA256)
	if err != nil {
		panic(err)
	}
	fmt.Println("signature bytes:", len(sig))
}
