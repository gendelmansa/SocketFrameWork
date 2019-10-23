import socket # for socket 
import sys  


try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print("Socket successfully created")
except socket.error as err: 
    print ("socket creation failed with error %s" %(err)) 
  
# default port for socket 
port = 666


try: 
    host_ip = "25.56.70.127"
except socket.gaierror: 
  
    # this means could not resolve the host 
    print ("there was an error resolving the host")
    sys.exit() 
  
# connect ing to the server 
s.connect((host_ip, port)) 
  
print("the socket has successfully connected to mitch on port == {0} : {1}".format( port, host_ip ))

sent = "fuck you"
s.send(sent.encode())

message = s.recv(1024)

# results = throughput.client()

print(message.decode())
