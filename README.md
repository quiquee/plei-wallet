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

Generate an address from the master seed using a path:
```
export MNEMONIC="grow either tiny identify decrease sand immune perfect warrior reward music boil"
$ ./pleiwallet.py --path "m/44'/60'/0'/0/0"  seed2addr
Generating from mnemonic using path m/44'/60'/0'/0/0
0x21ccda5126537ed51242695d2d0d05cc1c818af6
```

Using the XPUB, generate an address at depth n
```
export XPUB="xpub6EAX9vxqYHfCaGioK9XL54t6idECWKxRJ9TvCcpSTLB8ht6gJKWkgv9AcgfdaVLbLsZehC6UyAc2hs4wkWpaokXm5UmD2Uz7kRqVGh4mLW6"
$ ./pleiwallet.py --depth 0 xpub2addr
Generating from xpub:
0x21ccda5126537ed51242695d2d0d05cc1c818af6
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



