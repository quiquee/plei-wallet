#!/usr/bin/python3
import argparse
import pleibip32
import pleiutils
import os
import sys
import re

parser=argparse.ArgumentParser(description="A wallet for offline signing of Plei transactions",
                                formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('-S',metavar='MNEMONIC',default='MNEMONIC', type=str, help='Env variable to use for masterseed')
parser.add_argument('-X', metavar='XPUB',type=str, help='Env variable to use for public extended key')
parser.add_argument('-P',metavar='XPRIV', type=str, help='Env variable to use for private extended key')
parser.add_argument('--path',metavar='<path>', type=str, help='Derivation path to generate new master')
parser.add_argument('--depth',metavar='<depth>', type=str, help='Depth for address derivation')

parser.add_argument('action', 
                    type=str, help=
'''Action can be one of: 
genmaster       Generate a master key and shows all details (danger) 
seed2addr       Uses the mnemonic to generate a new address using <path>
xpub2addr       Uses the Xpub to generate a new address using <depth>

<depth> can be specified as a single digit, or a sequence: 0..10 
''')

args = parser.parse_args()


if args.action == "genmaster":
    mnemonic = os.getenv('MNEMONIC')
    if(mnemonic):
        bip32_ctx=pleibip32.genMaster(mnemonic)
        print (bip32_ctx.PublicKey().ToExtended() )
    else:
        print("Need to define a mnemonic")


if args.action == "xpub2addr":
    xpub = os.getenv('XPUB')    
    
    if(xpub):
        if not args.depth:
            print("Need to define a depth")        
            sys.exit(1)        
        
        else:
            print("Generating from xpub: " + xpub)
            p=re.compile("(\d+)(\.+(\d+))*")
            m=p.search(args.depth)
            lastdepth=0
            if not m:
                print("Need to define a depth in the format 'n..m' , or 'n'")        
                sys.exit(1)        

            if m.group(3):                
                print("Generaring multiple addresses from " +m.group(1) + " to " + m.group(3))
                lastdepth=int(m.group(3))
            else:            
                print("Generaring single address " +m.group(1) )
                lastdepth=int(m.group(1))

            depth=int(m.group(1))
            while depth<=lastdepth:
            
                bip32_ctx = pleibip32.deriveFromXPub(xpub,int(depth))
                pub_key=bip32_ctx.PublicKey().RawUncompressed()
                print(pleibip32.ethFromPub(pub_key.ToBytes()))
                depth=depth+1
    else:
        print("Need to define XPUB environment")        
        sys.exit(1)
        
if args.action == "seed2addr":
    mnemonic = os.getenv('MNEMONIC')
    if mnemonic:
        if not args.path:
            print("Need to define a derivation path")
            sys.exit(1)
        else:
            print("Generating from mnemonic using path " + args.path)
            bip32_ctx=pleibip32.genAddress(mnemonic, args.path)            
            pub_key=bip32_ctx.PublicKey().RawUncompressed()
            print(pleibip32.ethFromPub(pub_key.ToBytes()))
    else:
        print("Need to define a mnemonic")
        sys.exit(1)

    