import socket

confiaveis = ['www.google.com.br', 'www.netflix.com', 'www.github.com']

def check_hostname():
    global confiaveis
    for host in confiaveis:
        a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        a.settimeout(.5)
    try:
        b=a.connect_ex((host,80))
        if b==0: #ok, conectado
            return True
        except:
            pass
        a.close()
    return False
print(check_hostname() and "Conexão Ativa" or "Conexão Inativa")