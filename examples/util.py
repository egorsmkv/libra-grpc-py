def reverse_bytes(value):
    value = bytearray.fromhex(value)
    value.reverse()

    return bytes(value)
