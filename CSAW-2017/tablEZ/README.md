# tablEZ Write Up
By running the binary file on a linux machine, we see the following output.
```
root@kali:~/Workspace/CTF/CSAW-2017# ./tablez 
Please enter the flag:
flag{I_dont_know}
WRONG
```
The executable requires us to give an input, the flag. Then it give us an output depends on wheter we entered the correct flag.

Thus, we infer that the flag is stored in the bianry file somehow. 

Take a look of the binary.
The main function:
![alt text][tablez-1]
![alt text][tablez-2]
We can see that [rbp-0x90] is the address of input, and [rbp-0xc8] is the length of input.

We see a compare between [rbp-0xc8] and 0x25, which means the length of input is 37.

At the bottom, there is a comparison between [rbp-0xc0] and [rbp-0x90]. 

[rbp-0xc0] is defined earlier in the main function. 
![alt text][tablez-5]
Thus [rbp-0xc0] is "b1e711f59d73b32730f4f9f9b399beb3b19965237399711bf9279923be11116565059923ce". (Notice that we ignored the endian here)

Thus, we need [rbp-0x90] == [rbp-0xc0]
On the left part of the main function, we can seea loop. Every byte of the input is passed to another function get_tbl_entry. The input might have been modified there. 
![alt text][tablez-3]
The structure of the control flow graph, we see a while loop, with [rbp-0x8] < 0xfe as the premise. Also, byte[rbp-0x14] would be the byte passed in from input.

```
b = input
index = 0
while(index < 0xfe) {
	if(trans_tbl[i*2] == b) {
		return data_201281[i*2]
	}
	index++
}
```
Actually, trans_tbl is addr 0x201280, and data_201281 is addr 0x201281. Thus we can assume that data at 201280 is like the following.
(key1,value1),(key2,value2),...
![alt text][tablez-4]

Thus we copy down the table for the use of translation.

Since we need [rbp-0x90] equal to [rbp-0xc0], we create a map which can translate value to key. Therefore, we can reverse the string to get the flag.

Finally, in the code, we need to correct the endian, by using the following print.
```
print result[0:8][::-1] + result[8:16][::-1] + result[16:24][::-1] + result[24:32][::-1] + result[32:36][::-1] + result[36]
```
By running the provided script, we can see the flag is ```flag{t4ble_l00kups_ar3_b3tter_f0r_m3}```




[tablez-1]: https://github.com/bruceshenzk/CTF-WriteUp/blob/master/CSAW-2017/tablEZ/img/tablez-1.png
[tablez-2]: https://github.com/bruceshenzk/CTF-WriteUp/blob/master/CSAW-2017/tablEZ/img/tablez-2.png
[tablez-3]: https://github.com/bruceshenzk/CTF-WriteUp/blob/master/CSAW-2017/tablEZ/img/tablez-3.png
[tablez-4]: https://github.com/bruceshenzk/CTF-WriteUp/blob/master/CSAW-2017/tablEZ/img/tablez-4.png
[tablez-5]: https://github.com/bruceshenzk/CTF-WriteUp/blob/master/CSAW-2017/tablEZ/img/tablez-5.png
