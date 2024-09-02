import json
from pwn import *
from Crypto.Util.number import long_to_bytes

r = remote("IP ADDRESS", PORT NO)

r.sendlineafter(b"> ", b"1")
r.sendlineafter(b"message: ", b"0")
data = json.loads(r.recvuntil(b'\n').strip().decode().replace("'", "\""))

c1 = int(data["c"])
n = int(data["n"])

r.sendlineafter(b"> ", b"1")
r.sendlineafter(b"message: ", str(c1).encode())
c2 = int(json.loads(r.recvuntil(b"\n").strip().decode().replace("'", "\""))["c"])

rn = (c2 * pow(c1, -1, n**2)) % n**2
gm = (c1*pow(rn, -1, n**2)) % n**2

# These next 3 lines are used to make sure that gm is actually that value
r.sendlineafter(b"> ", b"2")
r.sendlineafter(b"gm: ", str(gm).encode())
assert json.loads(r.recvuntil(b"\n").strip().decode().replace("'", "\""))['λ']


print(long_to_bytes((gm-1)//n).decode())
