# QUESTION
# Given a valid (IPv4) IP address, return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".

#  Example 1:

# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"

class Solution:
    def defangIPaddr(self, address: str) -> str:
        address = list(address)
        for i in range(0,len(address)):
            if(address[i] == "."):
                address[i]="[.]"
        address = "".join(address)
        return address