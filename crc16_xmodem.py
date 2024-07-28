import binascii

def calculate_crc16_xmodem(data):
    data = binascii.unhexlify(data)
    crc = binascii.crc_hqx(data, 0)
    crc16_xmodem = f"{crc:04X}"
    print(crc16_xmodem)
    return crc16_xmodem

