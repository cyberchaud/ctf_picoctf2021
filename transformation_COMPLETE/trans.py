# ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

flag = [line.strip() for line in open("enc")]
hexstring = ''

for i in flag[0]:
	#print(i)
	hexstring += hex(ord(i))[2:]
	#print(hexstring, end='')
#print(plaintext)

#print(''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)]))
plaintext = ''
plaintext = bytes.fromhex(hexstring).decode('utf-8')
print(plaintext)
