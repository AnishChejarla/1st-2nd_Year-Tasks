import re 
def valid_ethereum_address(address):
    check_ethereum_regex=re.compile(r'^0x[0-9a-fA-F]{40}$')
    #regex=regular expression.
    #r'=raw string, it treats backslashes as regular characters.
    #0x=ethereum address has to start with 0x.
    #{40}=this indicates that there should be 40 characters excluding 0x.
    #$=this indicates that the pattern must end in the specified way.
    return bool(check_ethereum_regex.match(address))
def main():
    ethereum_address="0xAceFDBAE9F951F6EF32B3CAa1960F1A8c82ED54C"
    if valid_ethereum_address(ethereum_address):
        print("True")
    else:
        print("False")
main()


