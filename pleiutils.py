import eip_55
import re

def addr_validation( addr_str):
    
    if re.search("^ronin:", addr_str):
        ronaddr=re.sub("^ronin:","", addr_str)
        try:
            if int('0x'+ronaddr, 16 ) > 0:
                print("Valid ronin, return 1")
                return 1
        except:
            # wrong Ronin
            print("Wong ronin, return 0: " + ronaddr)
            return 0
    # Check ethereum compatible address
    # "0x" + 20 bytes in HEX
    if len(addr_str) == 42:
        try:
            #print("No test")
            eip_55.test(addr_str)
            print("Ethereum address is correct")
            return 1
        except:
            print("Ethereum address is not correct return 1")
            return 0
    else:
        print("Not even 20 bytes")
        return 0


def test():
    # Valid Ronin:
    addr_validation("ronin:f24cefc48ee7374983abf36baaad0cfe503980c8")    
    # Valid Ethereum
    addr_validation("0xDAc1EA5070e179dE110962c609EBBa7E4eE939Bd")
    # Wrong Ethereum (eip-55 fails)
    addr_validation("0xDAc1EA5070e179dE110962c609EBBa7E4eE939bd")
    # Wrong Ethereum (not a 20bytes address)
    addr_validation("0xDAc1EA5070e179dE110962c609EBBa7E4eE939")
    
    