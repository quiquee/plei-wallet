import binascii
import sha3
from _pysha3 import keccak_256
from bip_utils import Bip39SeedGenerator, Bip32Secp256k1


def genAddress(mnemonic,path):
    seed_bytes = Bip39SeedGenerator(mnemonic).Generate()
    bip32_ctx = Bip32Secp256k1.FromSeedAndPath(seed_bytes, path)
    return bip32_ctx

def genMaster(mnemonic):
    seed_bytes = Bip39SeedGenerator(mnemonic).Generate()
    bip32_ctx = Bip32Secp256k1.FromSeed(seed_bytes)
    return bip32_ctx

def deriveFromPub(xpub_key_bytes,depth):    
    bip32_ctx = Bip32Secp256k1.FromPublicKey(xpub_key_bytes)
    return bip32_ctx.ChildKey(depth)

def deriveFromXPub(xpub_key,depth):    
    bip32_ctx = Bip32Secp256k1.FromExtendedKey(xpub_key)
    return bip32_ctx.ChildKey(depth)

def ethFromPub(pub_key_bytes):
    addr= keccak_256(pub_key_bytes[1:]).digest()[-20:]
    return "0x{}".format( addr.hex())

# Test with https://iancoleman.io/bip39/
# Generate from mnemonic
def test():
    mnemonic = mnemonic="grow either tiny identify decrease sand immune perfect warrior reward music boil"
    # Test 0
    path = "m/44'/60'/0'/0/0"
    print ("\n Start test 0")
    print ("Menonic: " + mnemonic)
    print ("Path: " + path)
    bip32_ctx = genAddress(mnemonic, path)

    priv_key = bip32_ctx.PrivateKey().Raw()
    priv_key_hex = priv_key.ToHex()
    print("Priv Key: " + priv_key_hex)

    pub_key= bip32_ctx.PublicKey().RawUncompressed()
    pub_key_bytes=pub_key.ToBytes()
    pub_key_hex=pub_key.ToHex()
    print("Pub Key: " +pub_key_hex)
    print ("Address ( 0x21 ... ) " + ethFromPub(pub_key_bytes))
    print("Terminated test 0")

    # Test 1
    path = "m/44'/60'/0'/0/1"
    print ("\n Start test 1")
    print ("Menonic: " + mnemonic)
    print ("Path: " + path )
    bip32_ctx = genAddress(mnemonic, path)
    pub_key= bip32_ctx.PublicKey().RawUncompressed()
    print("Pub_key: " + pub_key.ToHex())
    print("Address ( 0xb37...): " + ethFromPub(pub_key.ToBytes()))
    print("Terminated test 1")

    # Test 2
    path = "m/44'/60'/0'/0/0"
    print ("\n Start test 2 - Derive first Child .. /1 from seed")
    print ("Menonic: " + mnemonic)
    print ("Path: " + path )
    bip32_ctx = genAddress(mnemonic, path)
    master_pub=bip32_ctx.PublicKey().RawUncompressed()
    bip32_ctx_1 = deriveFromPub(master_pub.ToBytes(),1)
    pub_key_1=bip32_ctx_1.PublicKey().RawUncompressed()
    print("Pub_key: " + pub_key_1.ToHex())
    print("Address ( 0xb37...): " + ethFromPub(pub_key_1.ToBytes()))
    print("Terminated test 2")

    # Test 3
    print ("\n Start test 3 - master and 1st child")
    bip32_ctx = genMaster(mnemonic)
    xpriv=bip32_ctx.PrivateKey().ToExtended()
    print("Master xpriv (xprv9s21...): " + xpriv)

    xpub=bip32_ctx.PublicKey().ToExtended()
    print("Master xpub: " + xpub)

    bip32_ctx_0 = bip32_ctx.ChildKey(0)
    test5_xpub = bip32_ctx_0.PublicKey().ToExtended()
    print ("BIP32 Ext key m/0 ( xpub69jSR...): " + test5_xpub )

    pub_key_0_0 = bip32_ctx_0.ChildKey(0).PublicKey().RawCompressed()

    print("Pub_key m/0/0 (0x03c3e...): " + pub_key_0_0.ToHex())
    print("Address m/0/0 ( 0x515a5...): " + ethFromPub(pub_key_0_0.ToBytes()))
    print("Terminated test 3")

    # test 4
    print ("\n Start test 4 - 1st child from master xpub")
    print ("xpub: " + xpub)
    bip32_ctx = deriveFromXPub(xpub,0)
    bip32_ctx_0=bip32_ctx.ChildKey(0)
    pub_key_0_c=bip32_ctx_0.PublicKey().RawCompressed()
    pub_key_0_u=bip32_ctx_0.PublicKey().RawUncompressed()
    print("Xpub m/0")
    print("Pub_key Compressed m/0/0 (0x03c3e...): " + pub_key_0_c.ToHex())
    print("Address m/0/0 ( 0x515a5...): " + ethFromPub(pub_key_0_u.ToBytes()))
    print("Terminated test 4")


    # test 5
    print ("\n Start test 5 - 1st child from 1st child xpub")
    print ("xpub: " + test5_xpub)
    bip32_ctx_0 = deriveFromXPub(test5_xpub,0)
    pub_key_0_c=bip32_ctx_0.PublicKey().RawCompressed()
    pub_key_0_u=bip32_ctx_0.PublicKey().RawUncompressed()
    print("Pub_key m/0/0 (0x03c3e...): " + pub_key_0_c.ToHex())
    print("Address m/0/0 ( 0x515a5...): " + ethFromPub(pub_key_0_u.ToBytes()))
    print("Terminated test 5")

