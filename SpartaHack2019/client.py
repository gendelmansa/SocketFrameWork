import sys, time
import socket

BUFSIZE = 1025

def client():
    count = 10
    host = '127.0.0.1'
    port = 666
    testdata = 'x' * (BUFSIZE-1) + '\n'
    t1 = time.time()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    t2 = time.time()
    s.connect((host, port))
    t3 = time.time()
    i = 0
    while i < count:
        i = i+1
        s.send(testdata.encode())
    s.shutdown(1) # Send EOF
    t4 = time.time()
    data = s.recv(BUFSIZE)
    t5 = time.time()
    return [data, 'Raw timers:', t1, t2, t3, t4, t5, 'Intervals:', t2-t1, t3-t2, t4-t3, t5-t4, 'Total:', t5-t1, 'Throughput:', round((BUFSIZE*count*0.001) / (t5-t1), 3), 'K/sec.']

print(client())