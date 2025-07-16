# Python 3 TCP server (run on the remote server):
python3 -c "
import socket
s = socket.socket()
s.bind(('0.0.0.0', 5000))
s.listen(1)
print('Listening on port 5000...')
conn, addr = s.accept()
print('Connection from:', addr[0])
conn.send(f'Your IP: {addr[0]}\n'.encode())
conn.close()
"
