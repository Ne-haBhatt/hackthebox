from unicorn import *
from unicorn.arm_const import *
from pwn import *

SERVER = "94.241.45.123"
PORT = 47050

def emulate_arm(hex_code):
    uc = Uc(UC_ARCH_ARM, UC_MODE_ARM)

    ADDRESS = 0x1000000

    uc.mem_map(ADDRESS, 2 * 1024 * 1024)
    uc.mem_write(ADDRESS, hex_code)

    try:
        uc.emu_start(ADDRESS, ADDRESS + len(hex_code))
    except UcError as e:
        print(f"Error: {e}")

    r0_value = uc.reg_read(UC_ARM_REG_R0)
    return r0_value

def ConnectServer():
    p = remote(SERVER, PORT)

    for i in range(50):
        level = p.recvuntil(": ")
        hex_code = p.recvuntil("Register r0:").decode().split("\n")[0]

        r0_result = emulate_arm(bytes.fromhex(hex_code))
        print(f"Level: {i+1}, The R0 result: {str(r0_result)}")

        p.sendline(str(r0_result).encode())
    p.interactive()

ConnectServer()
