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
