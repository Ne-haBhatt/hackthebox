# Man In The Middle
## Challenge Description:
Help! One of our red teamers has captured something between a user and their computer, but we've got no idea what we're looking at! Can you take a look?

### STEPS:
### ![ab](https://github.com/user-attachments/assets/2ab2f2c6-2848-4763-879e-b8502a393ce8) - unzip the file usimg the password 'hackthebox'
### ![ab](https://github.com/user-attachments/assets/9bc335a7-ca3f-4715-b597-0531b00803c0) - look inside the file
### ![ab](https://github.com/user-attachments/assets/542877e5-67af-4055-acce-d065c60f46c0) - We have a binary file named 'mitm.log'. Open this file in Wireshark.
### ![ab](https://github.com/user-attachments/assets/eb588a3a-d3a7-4f7a-801c-a19f09292cb6) - We can see the HCI_MON (Bluetooth Linux HCI Monitor Transport) protocol,L2CAP protocol,their length,information,etc.
### ![ab](https://github.com/user-attachments/assets/1fd5f885-3f50-4cb6-ad69-e5d542b08f53) - Save the file in the system and write python code for extracting the flag. 

```
from scapy.all import *

pcap_file = 'mitm.pcapng'

KEYS = {
    0x1e: ('1', '!'),
    0x1f: ('2', '@'),
    0x20: ('3', '#'),
    0x21: ('4', '$'),
    0x22: ('5', '%'),
    0x23: ('6', '^'),
    0x24: ('7', '&'),
    0x25: ('8', '*'),
    0x26: ('9', '('),
    0x27: ('0', ')'),
    0x2c: (' ', ' '),
    0x2d: ('-', '_'),
    0x2e: ('=', '+'),
    0x2f: ('[', '{'),
    0x30: (']', '}'),
    0x31: ('\\', '|'),
    0x33: (';', ':'),
    0x34: ('\'', '"'),
    0x35: ('`', '~'),
    0x36: (',', '<'),
    0x37: ('.', '>'),
    0x38: ('/', '?'),
}

# populate a-z and A-Z
for offset in range(0, 26):
    KEYS[0x04 + offset] = (chr(0x61 + offset), chr(0x41 + offset))


def decode_bytes(data):
    decoded = ''
    for bytes in data:
        shift = bytes[0] == 0x02
        code = bytes[2]
        if code in KEYS:
            decoded += KEYS.get(code)[1 if shift else 0]
    return decoded


def parse_capture():
    capture = rdpcap(pcap_file)
    data = []
    for packet in capture:
        raw_data = packet.getlayer(Raw).load
        frame = raw_data[4:]
        if len(frame) == 17:
            data.append(frame[10:13])
    return data


if __name__ == '__main__':    
    data = parse_capture()
    flag = decode_bytes(data)
    print(flag)

```

### ![ab](https://github.com/user-attachments/assets/1c4e5a26-7913-45f5-b6b2-a20ab3e87c1d) - all the files should be in the same folder.
### ![ab](https://github.com/user-attachments/assets/0c223bf6-ac83-48c1-9bc9-d74349395198) - run the python code and you will receive the flag.
