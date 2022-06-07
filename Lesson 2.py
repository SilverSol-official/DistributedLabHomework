import struct

def reverse_string1(s):
    return s[::-1]
#50 yf 50 tut popravit
def LittleOrder(b):
    scale = 16  ## equals to hexadecimal
    d = int((len(b)) / 2)
    e = bin(int(b, scale))[2:].zfill(d);
    re = reverse_string1(e);
    q=int(re,2);
    return q

def BigOrder(b):
    d=int(b, 16)
    return d

b=input('I Value: 0x');
print('II Number of bytes :',int((len(b))/2));
print('III Little endian order :',LittleOrder(b));
print('IV Big endian order: ',BigOrder(b));

