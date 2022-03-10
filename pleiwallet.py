#!/usr/bin/python3
import argparse
import pleibip32
import pleiutils
import os

parser=argparse.ArgumentParser(description="A wallet for offline signing of Plei transactions")
parser.add_argument('-S',metavar='MNEMONIC',default='MNEMONIC', type=str, help='Env variable to use for masterseed')
parser.add_argument('-X', metavar='XPUB',type=str, help='Env variable to use for public extended key')
parser.add_argument('-P',metavar='XPRIV', type=str, help='Env variable to use for private extended key')
parser.add_argument('action', type=str, help='One of gen_master/show_address')

args = parser.parse_args()


if args.action == "genmaster":
    masterseed = os.getenv('MNEMONIC')
    if(masterseed):
        bip32_ctx=pleibip32.genMaster(masterseed)
        print (bip32_ctx.PublicKey().ToExtended() )
    else:
        print("Need to define the master key")

print("End")


