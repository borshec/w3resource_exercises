import struct
st = "qwerty".encode()
i = 9
i1 = 1
c = b"x"
h = 8
s1 = struct.Struct('6s')
s2 = struct.Struct('6sI')
s3 = struct.Struct('6si')
s4 = struct.Struct('6sic')
s5 = struct.Struct('6sici')
s6 = struct.Struct('6sicxi')
s7 = struct.Struct('6sicxih')
p1 = s1.pack(st)
p1r = s1.unpack(p1)
p2 = s2.pack(st, i)
p2r = s2.unpack(p2)
p3 = s3.pack(st, i)
p3r = s3.unpack(p3)
p4 = s4.pack(st, i, c)
p4r = s4.unpack(p4)
p5 = s5.pack(st, i, c, i1)
p5r = s5.unpack(p5)
p6 = s6.pack(st, i, c, i1)
p6r = s6.unpack(p6)
p7 = s7.pack(st, i, c, i1, h)
p7r = s7.unpack(p7)
print(p1)
print(p1r)
print(p2)
print(p2r)
print(p3)
print(p3r)
print(p4)
print(p4r)
print(p5)
print(p5r)
print(p6)
print(p6r)
print(p7)
print(p7r)
print(ord("-"))
