// R3-02 VERIFY side: Go service verifies the ES256 JWT issued by qx-key-service (Python).
package main

import (
	"fmt"
	"os"

	"github.com/golang-jwt/jwt/v5"
)

const publicKeyPath = "/opt/qx/qx-key-service/keys/ec_signing_public.pem"

func main() {
	pemBytes, err := os.ReadFile(publicKeyPath)
	if err != nil {
		panic(err)
	}
	pub, err := jwt.ParseECPublicKeyFromPEM(pemBytes)
	if err != nil {
		panic(err)
	}
	token, err := jwt.Parse(os.Args[1], func(t *jwt.Token) (interface{}, error) {
		if _, ok := t.Method.(*jwt.SigningMethodECDSA); !ok {
			return nil, fmt.Errorf("unexpected method %v", t.Header["alg"])
		}
		return pub, nil
	}, jwt.WithValidMethods([]string{"ES256"}))
	if err != nil {
		panic(err)
	}
	fmt.Println("token valid:", token.Valid)
}
