# Easiest Way of CRC-16 XMODEM Calculation

This Python script calculates the CRC-16 checksum using the XMODEM protocol. The CRC (Cyclic Redundancy Check) is commonly used for error-checking in data transmission and storage.

## Usage

To use the script, provide a hexadecimal string as input, and it will output the CRC-16 checksum in hexadecimal format.

### Example

```python
import binascii

def calculate_crc16_xmodem(data):
    data = binascii.unhexlify(data)
    crc = binascii.crc_hqx(data, 0)
    crc16_xmodem = f"{crc:04X}"
    print(crc16_xmodem)
    return crc16_xmodem

# Sample usage
data = "12345678"  # Hexadecimal string input
checksum = calculate_crc16_xmodem(data)
print(f"CRC-16 XMODEM Checksum: {checksum}")
