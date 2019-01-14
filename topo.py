from multiprocessing import Process

from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import lg
from mininet.node import Controller, RemoteController, OVSKernelSwitch, UserSwitch, OVSSwitch
from mininet.link import Link, TCLink
from bottle import route, run, template, post, request, Bottle
import socket

IP_DATA_FILE = 'ip_data.txt'
SERVER_PORT = 8181

app = Bottle()
links = []


def read_ip():
    f = open(IP_DATA_FILE, "r")
    my_ip = f.readline().rstrip('\n')

    if is_valid_ipv4_address(my_ip):
        print('Bottle server IP set as = ' + my_ip)
        return my_ip
    else:
        print('Bottle server IP = ' + my_ip + ' invalid, changed to = localhost')
        return 'localhost'


def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:
        return False

    return True


def run_bottle():
    app.run(host=read_ip(), port=SERVER_PORT)
    return


def start_bottle_process():
    p = Process(target=run_bottle)
    p.start()
    return p


@app.get('/check_connection/')
def check_connection():
    print("Connection correct.")
    return "<p>Connection correct.</p>"


@app.post('/change_setting/')
def change_setting():
    postdata = request.body.read()
    json = request.json
    setting_id = json["setting_id"]
    print("Requested setting_id = " + str(setting_id))

    if setting_id == 1:
        # net.configLinkStatus()
        print(str(setting_id) + " set successfully.")

    if setting_id == 2:
        # net.configLinkStatus()
        print(str(setting_id) + " set successfully.")

    if setting_id == 3:
        # net.configLinkStatus()
        print(str(setting_id) + " set successfully.")

    if setting_id == 4:
        # net.configLinkStatus()
        print(str(setting_id) + " set successfully.")


@app.route('/stop')
def stop():
    net.stop()
    print("Requested stop.")


if __name__ == '__main__':
    lg.setLogLevel( 'info')

    p = start_bottle_process()

    net = Mininet(controller=RemoteController)

    h1 = net.addHost('h1')
    h2 = net.addHost('h2')

    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')

    c0 = net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=8888)

    links = [net.addLink(h1, s1), net.addLink(s1, h2),
             net.addLink(h1, s2), net.addLink(s2, h2)]

    net.start()
    CLI(net)
    net.stop()
    p.terminate()


