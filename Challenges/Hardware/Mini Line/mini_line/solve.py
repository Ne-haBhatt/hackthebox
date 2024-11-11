from struct import pack

local_24 = [0x61584E52, 0x29682E78, 0x6E297745, 0x4569762E]  
local_28 = [0xCC14961A]
local_38 = [0xCCAE98BE, 0xBEBA1214, 0x30303010, 0x00000088]

flag = bytearray()
for d in local_24:
    for b in pack('<I', d):
        if b:
            flag.append(b ^ 0x1a)

for d in local_28:
    for b in pack('<I', d):
        if b:
            flag.append(b >> 1 ^ 0x39)

for d in local_38:
    for b in pack('<I', d):
        if b:
            flag.append(b >> 1 ^ 0x39)

print(flag.decode())
                     
