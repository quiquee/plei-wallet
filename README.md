# plei-utils
A library to validate addresses , potentially add whitelisted addresses in a smart way

```
enrique@UX425EA ~/project/plei-wallet $ python3
Python 3.8.10 (default, Sep 28 2021, 16:10:42) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import pleiutils
>>> pleiutils.test()
Valid ronin, return 1
Ethereum address is correct
Ethereum address is not correct return 1
Not even 20 bytes
>>>
```
# pleiwallet
Includes the pleiwallet functionality (wip)
Sample use:

## Generate an address from the master seed using a path:
```
export MNEMONIC="grow either tiny identify decrease sand immune perfect warrior reward music boil"
$ ./pleiwallet.py --path "m/44'/60'/0'/0/0"  seed2addr
Generating from mnemonic using path m/44'/60'/0'/0/0
0x21ccda5126537ed51242695d2d0d05cc1c818af6
```
## Generate BIP32 extended keys from path
```
export MNEMONIC="grow either tiny identify decrease sand immune perfect warrior reward music boil"
$ ./pleiwallet.py --path "m/44'/60'/0'/0"  seed2bip32keys -W
Generating BIP32 extended keys from mnemonic using path m/44'/60'/0'/0
xpub6EAX9vxqYHfCaGioK9XL54t6idECWKxRJ9TvCcpSTLB8ht6gJKWkgv9AcgfdaVLbLsZehC6UyAc2hs4wkWpaokXm5UmD2Uz7kRqVGh4mLW6
xprvA1BAkRRwhv6uMneLD7zKhvwNAbPi6sEZvvYKQEQptze9q5mXknCW97pgmSAE4cciAjFURnBFpt42bMcHiGjAN4Hw7M6Az9GUdqV5gNGrQD4

```

## Using the XPUB, generate an address at depth n 
```
export XPUB="xpub6EAX9vxqYHfCaGioK9XL54t6idECWKxRJ9TvCcpSTLB8ht6gJKWkgv9AcgfdaVLbLsZehC6UyAc2hs4wkWpaokXm5UmD2Uz7kRqVGh4mLW6"
$ ./pleiwallet.py --depth 0 xpub2addr
Generating from xpub:
0x21ccda5126537ed51242695d2d0d05cc1c818af6
```

## Using the XPRIV, generate one or several addresses
Use the following mnemonic to reproduce: peasant gaze salad best tell harbor cube blast give aim clinic task
In the Ian Coleman website enter this 12 workds and choose Coin: Ethereum

The xpriv of the Ethereum (same as Ronin) derivation path m/44'/60'/0'/0 is xprvA1ENE... 
Define and environment XPRIV with that value:

```
$ export XPRIV="xprvA1ENEHk9tE6xmKWmRCmdjgPhiSuMh9LTmifnuVXu48oqn26ezNvNe5xJUVoF6fFBcUkRuTiTaU3uCpszxGJbYRKapEibjrek9btnHzLppbr"
```

Generate 6 addresses, from 0 to 5 , using that XPRIV as follows
```
./pleiwallet.py xpriv2addr --depth 0..5 -W
```
Check that you have exactly the same output, but for the Address, which will all be lowercase
```
Generating from xpriv: xprvA1ENEH
Generaring multiple addresses from 0 to 5

0xaa646a03625e8b237375a4b8d019cf45cdabec1a      02c24235eef43126ade108173816b4a08b53a31f9e1ef313d59c1da98ff96a0ef8      897baed181da130c5f83a9521a537ee63a9f7504e07fc7b1e5fa53513eb52297
0x859c95e52c0c22fade1e8bfd5a58eb3c1d634846      021fdfbb1722df0849c3e0bbc06fc1e347feb1336b2f5fd62c28131faf71b16dfc      242b80849c7b7f77200bfa5f056d0233e7145150bd0c0b68ff356545c9dec017
0xf2fe6b62db78d18d8fb9e97dad20dbc08f33903e      02a43f040874318da2c00df970654d8bfbc0dd50dafbc928b70fd2d40959b4fd0d      a8a3fd9030012b3068e32000dd41fe33cfb9a67a9d780650b5015176d2646441
0x2a5ebdf070a40672e5b0ac1b67b383c17e2ed9ac      0215a29786fe97bcbf541ff004b1d6670fa53fb2c30944c4b54b043b5c5e17ee83      4c72e3943cba2cc2c4af49f54f11fa6fd17faf3d6ee1cd0b0930cab54887a04a
0x919540693312fc18e837308536d8dcb8a238e131      02e4750b070bc0881f60e15632a0bb9c6992a7227f6ccd6673d66cd753411a468e      f2627d51773fb1f5e4fc1f4607d1f39f974a76b5eecf69d8eade80152264bf4d
0x7eb3efeb4fae31dcce2d25f0c5658cbf9f1713fb      024f6fd04aa5afb4ff49b97b66db294f78c0b63d1e57eca080205d3dfe02bdc67c      be58e1f86690f8d63540435a6bff3ade60e3955578f1f4841ebfb78f8afa219b
```

More info, ./pleiwallet.py -h
```
$ ./pleiwallet.py -h
usage: pleiwallet.py [-h] [-S MNEMONIC] [-X XPUB] [-P XPRIV] [--path <path>] [--depth <depth>] action

A wallet for offline signing of Plei transactions

positional arguments:
  action           Action can be one of: 
                   genmaster       Generate a master key and shows all details (danger) 
                   seed2addr       Uses the mnemonic to generate a new address using <path>
                   xpub2addr       Uses the Xpub to generate a new address using <depth>

optional arguments:
  -h, --help       show this help message and exit
  -S MNEMONIC      Env variable to use for masterseed
  -X XPUB          Env variable to use for public extended key
  -P XPRIV         Env variable to use for private extended key
  --path <path>    Derivation path to generate new master
  --depth <depth>  Depth for address derivation
```



