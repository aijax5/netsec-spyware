import socket                   

port = 6020                    
s = socket.socket()
host = socket.gethostname()
s.bind((host, port))
s.listen(5)

print( 'Server listening....')

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print ('Got connection from', addr)
    data = conn.recv(1024)
    # print(data)
    if data == 'video'.encode():        
        with open('video.mp4', 'wb') as f:
            print ('receving a video file from ',addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                f.write(data)

    else:
        print("Video file received!\nReceiving a audio file....\n")
        with open('audio.mp3', 'wb') as f:
            print ('receving a audio file from ',addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                f.write(data)

    f.close()
    print('Successfully got the files')
    conn.close()
