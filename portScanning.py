import socket

def port_scanner(target,ports):
    clcoding=socket.gethostbyname(target)
    print(f"Scanning {target} ({clcoding})")

    for port in ports:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result=sock.connect_ex((clcoding,port))
        if result==0:
            print(f"Port {port}: OPEN")
        sock.close()


target="clcoding.com"
ports=[22,80,443,8080]
port_scanner(target,ports)            
