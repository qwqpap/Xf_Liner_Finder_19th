import json
import socket

sent = socket.socket()
sent.connect(("127.0.0.1", 11451))
sent.send("qwq".encode("utf-8"))

got = sent.recv(1024).decode("utf-8")
got = json.loads(got)
print(got["dick"])