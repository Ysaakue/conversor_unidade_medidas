import pickle
from socket import socket, gethostname, SOCK_STREAM, AF_INET

HOST = gethostname()
PORT = 8080
BUFSIZ = 4096
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

SERVER.listen(10)

print('Servidor iniciado.\n Aguardando conexão... ')

while True:
    client_socket, client_address = SERVER.accept()
    print('%s:%s está conectado. ' % client_address)

    data = pickle.loads(client_socket.recv(BUFSIZ))
    response = {}
    if data["system"] == "length":
        if data["unit_of_measurement"] == "meter":
            dc = data["input"] * 10
            cm = data["input"] * 100
            km = data["input"] / 1000
            mm = data["input"] * 1000
            response["msg"] = "{m}m é equivalente a {km}km, {dc}dc, {cm}cm ou {mm}mm.".format(m=data["input"],dc=dc,cm=cm,km=km,mm=mm)
        elif data["unit_of_measurement"] == "centimeter":
            mm = data["input"] * 10
            dc = data["input"] / 10
            m = data["input"]  / 100
            km = data["input"] / 100000
            response["msg"] = "{cm}cm é equivalente a {km}km, {dc}dc, {m}m ou {mm}mm.".format(cm=data["input"],dc=dc,m=m,km=km,mm=mm)
        elif data["unit_of_measurement"] == "kilometer":
            m = data["input"]  * 1000
            dc = data["input"] * 10000
            cm = data["input"] * 100000
            mm = data["input"] * 1000000
            response["msg"] = "{km}km é equivalente a  {dc}dc, {m}m, {cm}cm ou {mm}mm.".format(km=data["input"],dc=dc,m=m,cm=cm,mm=mm)
        elif data["unit_of_measurement"] == "decimeter":
            m = data["input"]  / 10
            cm = data["input"] * 10
            mm = data["input"] * 100
            km = data["input"] / 10000
            response["msg"] = "{dc}dc é equivalente a {km}km, {m}m, {cm}cm ou {mm}mm.".format(dc=data["input"],cm=cm,m=m,km=km,mm=mm)
        elif data["unit_of_measurement"] == "millimeter":
            cm = data["input"] / 10
            dc = data["input"] / 100
            m = data["input"]  / 1000
            km = data["input"] / 1000000
            response["msg"] = "{mm}mm é equivalente a {km}km, {dc}dc, {m}m ou {cm}cm.".format(mm=data["input"],dc=dc,m=m,km=km,cm=cm)
        else:
            response["msg"] = "a operação solicitada é invalidade, verifique seus dados e tente novamente."
    elif data["system"] == "volume":
        if data["unit_of_measurement"] == "liter":
            dl = data["input"] * 10
            cl = data["input"] * 100
            ml = data["input"] * 1000
            response["msg"] = "{l}L é equivalente a {dl}dl, {cl}cl ou {ml}ml.".format(l=data["input"],dl=dl,cl=cl,ml=ml)
        elif data["unit_of_measurement"] == "milliliter":
            cl = data["input"] / 10
            dl = data["input"] / 100
            l = data["input"]  / 1000
            response["msg"] = "{ml}ml é equivalente a {dl}dl, {l}L ou {cl}cl.".format(ml=data["input"],dl=dl,cl=cl,l=l)
        elif data["unit_of_measurement"] == "deciliter":
            l = data["input"]  / 10
            cl = data["input"] * 10
            ml = data["input"] * 100
            response["msg"] = "{dl}dl é equivalente a {l}L, {cl}cl ou {ml}ml.".format(dl=data["input"],l=l,cl=cl,ml=ml)
        elif data["unit_of_measurement"] == "centiliter":
            ml = data["input"] * 10
            dl = data["input"] / 10
            l = data["input"]  / 100
            response["msg"] = "{cl}cl é equivalente a {dl}dl, {l}L ou {ml}ml.".format(cl=data["input"],dl=dl,l=l,ml=ml)
        else:
            response["msg"] = "a operação solicitada é invalidade, verifique seus dados e tente novamente."
    else:
        response["msg"] = "a operação solicitada é invalidade, verifique seus dados e tente novamente."
    
    client_socket.send(pickle.dumps(response))