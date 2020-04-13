import socket                  

s = socket.socket()
host = socket.gethostname()
port = 6020                 

s.connect((host, port))
s.send("video".encode('utf8'))
filename='/home/aijax/Desktop/netsec-spyware/videoplayback.mp4'
f = open(filename,'rb')
l = f.read(1024)

while (l):
   s.send(l)
   l = f.read(1024)

s.close()
print('video sent!')



s = socket.socket()             
host = socket.gethostname()     
port = 6020

s.connect((host, port))
s.send("audio".encode())


filename='../astronomia.mp3'
f = open(filename,'rb')
l = f.read(1024)

while (l):
   s.send(l)
   # print('Sent ',repr(l))  
   l = f.read(1024)

f.close()
print('audio sent!')

s.close()
print('connection closed')