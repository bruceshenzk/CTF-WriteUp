

str1 = "b1e711f59d73b32730f4f9f9b399beb3b19965237399711bf9279923be11116565059923ce"

str2 = "\x01\xbb\x02\x9b\x03\xc4\x04l\x05J\x06.\x07\"\x08E\t3\n\xb8\x0b\xd5\x0c\x06\r\n\x0e\xbc\x0f\xfa\x10y\x11$\x12\xe1\x13\xb2\x14\xbf\x15,\x16\xad\x17\x86\x18`\x19\xa4\x1a\xb6\x1b\xd8\x1cY\x1d\x87\x1eA\x1f\x94 w!\xf0\"O#\xcb$a%%&\xc0\'\x97(*)\\*\x08+\xc9,\x9f-C.N/\xcf0\xf91>2o3e4\xe75\xc5697\xb78\xef9\xd0:\xc8;/<\xaa=\xc7>G?<@\x81A2BIC\xd3D\xa6E\x96F+GXH@I\xf1J\x9cK\xeeL\x1aM[N\xc6O\xd6P\x80Q-RmS\x9aT=U\xa7V\x93W\x84X\xe0Y\x12Z;[\xb9\\\t]i^\xba_\x99`Hasb\xb1c|d\x82e\xbef\'g\x9dh\xfbigj~k\xf4l\xb3m\x05n\xc2o_p\x1bqTr#sqt\x11u0v\xd2w\xa5xhy\x9ez?{\xf5|z}\xce~\x0b\x7f\x0c\x80\x85\x81\xde\x82c\x83^\x84\x8e\x85\xbd\x86\xfe\x87j\x88\xda\x89&\x8a\x88\x8b\xe8\x8c\xac\x8d\x03\x8eb\x8f\xa8\x90\xf6\x91\xf7\x92u\x93k\x94\xc3\x95F\x96Q\x97\xe6\x98\x8f\x99(\x9av\x9bZ\x9c\x91\x9d\xec\x9e\x1f\x9fD\xa0R\xa1\x01\xa2\xfc\xa3\x8b\xa4:\xa5\xa1\xa6\xa3\xa7\x16\xa8\x10\xa9\x14\xaaP\xab\xca\xac\x95\xad\x92\xaeK\xaf5\xb0\x0e\xb1\xb5\xb2 \xb3\x1d\xb4]\xb5\xc1\xb6\xe2\xb7n\xb8\x0f\xb9\xed\xba\x90\xbb\xd4\xbc\xd9\xbdB\xbe\xdd\xbf\x98\xc0W\xc17\xc2\x19\xc3x\xc4V\xc5\xaf\xc6t\xc7\xd1\xc8\x04\xc9)\xcaU\xcb\xe5\xccL\xcd\xa0\xce\xf2\xcf\x89\xd0\xdb\xd1\xe4\xd28\xd3\x83\xd4\xea\xd5\x17\xd6\x07\xd7\xdc\xd8\x8c\xd9\x8a\xda\xb4\xdb{\xdc\xe9\xdd\xff\xde\xeb\xdf\x15\xe0\r\xe1\x02\xe2\xa2\xe3\xf3\xe44\xe5\xcc\xe6\x18\xe7\xf8\xe8\x13\xe9\x8d\xea\x7f\xeb\xae\xec!\xed\xe3\xee\xcd\xefM\xf0p\xf1S\xf2\xfd\xf3\xab\xf4r\xf5d\xf6\x1c\xf7f\xf8\xa9\xf9\xb0\xfa\x1e\xfb\xd7\xfc\xdf\xfd6\xfe}\xff1"

# Parse str2

str2 = str2.encode("hex")
print(str2)
#str2 = str2.decode('hex')
map1 = {}
print("len",len(str2))
for i in range(255):
	v1 = str2[i*4 : i*4+2]
	v2 = str2[i*4+2: i*4+4] 
	#print str2[i*4 : i*4+2], ":", str2[i*4+2: i*4+4] 
	map1[v2]=[v1]

result = ""
for i in range(len(str1) // 2):
	# print map1[str1[2*i : 2*i+2]]
	print str1[2*i : 2*i+2], map1[str1[2*i : 2*i+2]][0]
	result = result + chr(int(map1[str1[2*i : 2*i+2]][0],16))

print len(result)
print result[0:8][::-1] + result[8:16][::-1] + result[16:24][::-1] + result[24:32][::-1] + result[32:36][::-1] + result[36]

