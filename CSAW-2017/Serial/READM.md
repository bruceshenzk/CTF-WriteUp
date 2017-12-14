#Serial Writeup
Connecting to the port would get us the following result.
'''
nc localhost 8000
8-1-1 even parity. Respond with '1' if you got the byte, '0' to retransmit.
00110111001
'''
After googling the 8-1-1 even parity, we find out the format of the 11 bits is as following

start_bit [0] | 8_bit_data | parity_bit | end_bit[1]

If the number of 1 in 8_bit_data is even, parity_bit should be 0.
Otherwise, the number should be 1.
Our job is to find if the parity_bit is corret for the data. If so, we accept the data and request a new byte. Otherwise, we send "0" and let the server resend the data.

The final flag is the string value of the bytes received. 
