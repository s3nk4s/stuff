from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util import asn1

asn1Pub = '30818902818100e1d4bd3dfe117f772a011f1ae06633ba446142ed92a7c577dd0ea91497dc679efd19a5070a164f5a3bf80b70b93f3c17ec4866d1523ae106cbdd083fa5b591da5e44204db28eedd936df375f145afb01144ffc583281fbe4282d1372d36eb4da86f21bb8c0681068858ba5d27cdf79c1a5d979f18e228d52a6b296b60aacc801020301000130333434fd4b5cc0'.decode('hex')

seq = asn1.DerSequence()
seq.decode(asn1Pub)

keyPub = RSA.construct((seq[0],seq[1]))

clearKey = '40404040404040403131313131313131'.decode('hex')

cipher = PKCS1_OAEP.new(keyPub) #new(key, hashAlgo=None, mgfunc=None, label='') If not specified, Crypto.Hash.SHA (that is, SHA-1) is used. If not specified, the standard MGF1 is used (a safe choice).
encryptedKey = cipher.encrypt(clearKey)

print encryptedKey.encode('hex')