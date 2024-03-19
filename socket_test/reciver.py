import socket
import json

test_dic = {
    "dick": 1
}


s = socket.socket()
s.bind(("127.0.0.1", 11451))
s.listen(1024)
while True:
    c, addr = s.accept()
    got = c.recv(1024).decode('utf-8')
    print(got)
    c.send(json.dumps(test_dic).encode("utf-8"))
