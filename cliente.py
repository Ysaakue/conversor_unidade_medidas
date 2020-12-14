import os
import switch
import pickle
import platform
import getpass
from time import sleep
from socket import gethostname, socket, SOCK_STREAM, AF_INET

if platform.system() == 'Linux':
    clear_string = 'clear'
else:
    clear_string = 'cls'

def clear():
    os.system(clear_string)

def bar():
    print('_______________________________')

def menu_principal():
    bar()
    print(' 1 - Conversor de comprimento')
    print(' 2 - Conversor de volume')
    print('\n 0 - Sair')
    bar()

def menu_comprimento():
    bar()
    print(' 1 - Metro(m)')
    print(' 2 - Centímetro(cm)')
    print(' 3 - Quilômetro(km)')
    print(' 4 - Decimetro(dm)')
    print(' 5 - Milímetro(mm)')
    print('\n 0 - Voltar')
    bar()

def menu_volume():
    bar()
    print(' 1 - Litro(L)')
    print(' 2 - Mililitro(ml)')
    print(' 3 - Decilitro(dl)')
    print(' 4 - Centiliter(cl)')
    print('\n 0 - Voltar')
    bar()

def fazer_conversao(data):
    HOST = gethostname()
    PORT = 8080
    BUFSIZ = 4096
    ADDR = (HOST, PORT)

    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.connect(ADDR)

    server_socket.send(pickle.dumps(data))
    response = pickle.loads(server_socket.recv(BUFSIZ))
    server_socket.close()
    clear()
    print(response["msg"])
    print("\n\nPrecione enter para continuar")
    getpass.getpass("")
    clear()

def get_option():
    _input = input('Entre com uma opção: ')
    try:
        response = int(_input)
    except:
        response = -1
    return response

def get_value():
    _input = input('Digite o valor a ser convertido: ')
    try:
        response = int(_input)
    except:
        response = -1
    return response

def invalid_option():
    clear()
    print('Opção inválida. Por favor, selecione uma opção válida')
    sleep(5)
    clear()

def good_bye():
    clear()
    print('Uma pena ter que ver você ir embora, espero que tenha aproveitado a experiência e vote sempre.')
    sleep(5)

def hello():
    clear()
    print('Olá, eu sou um sistema de conversão de medidas, siga os menus a seguir para realizar as operações.\n\n')

length_inputs = ["meter","centimeter","kilometer","decimeter","millimeter"]
volume_inputs = ["liter","milliliter","deciliter","centiliter"]

if __name__ == '__main__':
    opc1 = -1
    opc2 = -1
    obj = {}
    hello()
    while opc1 != 0:
        menu_principal()
        opc1 = get_option()
        if opc1 == 1:
            obj["system"] = "length"
            clear()
            while opc2 != 0:
                menu_comprimento()
                opc2 = get_option()
                if opc2 in range(1,6):
                    obj["unit_of_measurement"] = length_inputs[opc2-1]
                    obj["input"] = get_value()
                    fazer_conversao(obj)
                elif opc2 != 0:
                    invalid_option()
            clear()
        elif opc1 == 2:
            obj["system"] = "volume"
            clear()
            while opc2 != 0:
                menu_volume()
                opc2 = get_option()
                if opc2 in range(1,5):
                    obj["unit_of_measurement"] = volume_inputs[opc2-1]
                    obj["input"] = get_value()
                    fazer_conversao(obj)
                elif opc2 != 0:
                    invalid_option()
            clear()
        elif opc1 != 0:
            invalid_option()
    good_bye()