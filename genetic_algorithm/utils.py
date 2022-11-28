import struct


def bin2float(b):
	""" Convert binary string to a float.

    Attributes:
        :b: Binary string to transform.
    """
	h = int(b, 2).to_bytes(8, byteorder="big")
	return struct.unpack('>d', h)[0]


def float2bin(f, bits: int = 64):
	"""
		Convert float to 64-bit binary string.

		Attributes:
		:f: Float number to transform.
	"""
	[d] = struct.unpack(">Q", struct.pack(">d", f))
	return f'{d:0{bits}b}'


def int2bin(value, bits: int = 4):
	return bin(value).replace('0b', '').rjust(bits, '0')


def bin2int(b):
	return int(b, 2)
