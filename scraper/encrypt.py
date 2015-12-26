import os, random, struct, hashlib
from Crypto.Cipher import AES

def encrypt(password, filein, fileout=None, chunksize=64*1024):
	if not fileout:
		fileout = filein + '.enc'

	key = hashlib.sha256(password).digest()
	iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
	encryptor = AES.new(key, AES.MODE_CBC, iv)
	filesize = os.path.getsize(filein)

	with open(filein, 'rb') as filein:
		with open(fileout, 'wb') as fileout:
			fileout.write(struct.pack('<Q', filesize))
			fileout.write(iv)

			while True:
				chunk = filein.read(chunksize)

				if len(chunk) == 0:
					break
				elif len(chunk) % 16 != 0:
					 chunk += ' ' * (16 - len(chunk) % 16)

				fileout.write(encryptor.encrypt(chunk))

def decrypt(password, filein, fileout=None, chunksize=24*1024):
	if not fileout:
		fileout = os.path.splitext(filein)[0]

	print fileout + '\n'*3

	key = hashlib.sha256(password).digest()

	with open(filein, 'rb') as filein:
		size = struct.unpack('<Q', filein.read(struct.calcsize('Q')))[0]
		iv = filein.read(16)
		decryptor = AES.new(key, AES.MODE_CBC, iv)

		with open(fileout, 'wb') as fileout:
			while True:
				chunk = filein.read(chunksize)

				if len(chunk) == 0:
					break

				fileout.write(decryptor.decrypt(chunk))

			fileout.truncate(size)