from multiprocessing import Process

from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import lg
from mininet.node import Controller, RemoteController, OVSKernelSwitch, UserSwitch, OVSSwitch
from mininet.link import Link, TCLink
from bottle import route, run, template, post, request, Bottle
import threading
import socket

IP_DATA_FILE = 'ip_data.txt'
HOST_IP_ADDRESS = 'localhost'
SERVER_PORT = 8181

app = Bottle()
links = []


def read_ip():
    f = open(IP_DATA_FILE, "r")
    my_ip = f.readline()

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
    app.run(host=HOST_IP_ADDRESS, port=SERVER_PORT)
    return


def start_bottle_process():
    p = Process(target=run_bottle)
    p.start()
    return p


@app.post('/change_setting/')
def change_link_bandwidth():
    postdata = request.body.read()
    json = request.json
    setting_id = json["setting_id"]
    print("Requested setting_id = " + str(setting_id))


@app.route('/stop')
def stop():
    net.stop()
    print("Requested stop.")


if __name__ == '__main__':
    lg.setLogLevel( 'info')

    p = start_bottle_process()

    net = Mininet(controller=RemoteController, link=TCLink, switch=OVSSwitch)

    h1 = net.addHost('h1')
    h2 = net.addHost('h2')

    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')
    s4 = net.addSwitch('s4')
    s5 = net.addSwitch('s5')

    c0 = net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=8888)

    links = [net.addLink(h1, s1, bw=10), net.addLink(s1, s2, bw=10), net.addLink(s2, s4, bw=10),
             net.addLink(s4, h2, bw=10), net.addLink(s1, s5, bw=10), net.addLink(s5, s4, bw=10),
             net.addLink(s1, s3, bw=10), net.addLink(s3, s4, bw=10)]

    net.start()
    CLI(net)
    net.stop()
    p.terminate()
