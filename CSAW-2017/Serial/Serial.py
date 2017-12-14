from pwn import *

bytes = []
def count (input):
	c = 0
	for i in range(8):
		if input[i] == '1':
			c += 1
	return c

def correct (input):
	byte = input[1:9]
	start = input[0]
	end = input[10]
	purity = input[9]
	print start, byte, purity, end
	if start != '0' or end != '1':
		return "0"
	elif (count(byte)+1) % 2 != int(purity):
		bytes.append(byte)
		return "1"
	else:
		return "0"

r = remote("localhost", 8000)

print(r.recvuntil("retransmit."))
r.recvline()
round = 1
while True:
	try:
		line = r.recvline()[:-1]
	except:
		break

	# print "DEBUG:", round, line#, correct(line)
	r.sendline(correct(line))
	round += 1
print "flag{".encode("hex")
flag = ""
print "".join([chr(int(b,2)) for b in bytes])


