import threading
from multiprocessing import Process

from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import lg
from mininet.node import RemoteController
from bottle import route, run, template, post, request, Bottle
import socket

IP_DATA_FILE = 'ip_data.txt'
SERVER_PORT = 8181


class BottleRunner(Bottle):

    def __init__(self, network):
        super(BottleRunner, self).__init__()
        self.network = network
        self.route('/check_connection/', callback=self.check_connection)
        self.post('/change_setting/', callback=self.change_setting)
        self.route('/stop', callback=self.stop)

    def check_connection(self):
        print("Connection correct.")
        return "<p>Connection correct.</p>"

    def change_setting(self):
        postdata = request.body.read()
        json = request.json
        setting_id = json["setting_id"]
        print("Requested setting_id = " + str(setting_id))

        if setting_id == 1:
            self.network.configLinkStatus(src='h1', dst='s1', status='down')
            self.network.configLinkStatus(src='s1', dst='h2', status='down')
            self.network.configLinkStatus(src='s1', dst='h3', status='up')
            self.network.configLinkStatus(src='s1', dst='h4', status='up')
            print(str(setting_id) + " set successfully.")

        if setting_id == 2:
            self.network.configLinkStatus(src='h1', dst='s1', status='up')
            self.network.configLinkStatus(src='s1', dst='h2', status='up')
            self.network.configLinkStatus(src='s1', dst='h3', status='down')
            self.network.configLinkStatus(src='s1', dst='h4', status='down')
            print(str(setting_id) + " set successfully.")

        if setting_id == 3:
            print(str(setting_id) + " set successfully.")

        if setting_id == 4:
            print(str(setting_id) + " set successfully.")

    def stop(self):
        self.network.stop()
        print("Requested stop.")


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


def read_ip():
    f = open(IP_DATA_FILE, "r")
    my_ip = f.readline().rstrip('\n')

    if is_valid_ipv4_address(my_ip):
        print('Bottle server IP set as = ' + my_ip)
        return my_ip
    else:
        print('Bottle server IP = ' + my_ip + ' invalid, changed to = localhost')
        return 'localhost'


def run_bottle(network):
    br = BottleRunner(network)
    br.run(host=read_ip(), port=SERVER_PORT)
    print('run bottle')
    return


def start_bottle_process(network):
    p = Process(target=run_bottle(network))
    p.run()
    return p


if __name__ == '__main__':
    lg.setLogLevel( 'info')

    net = Mininet(controller=RemoteController)
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')
    h4 = net.addHost('h4')
    # hosts = [h1, h2]

    s1 = net.addSwitch('s1')
#    s2 = net.addSwitch('s2')
    # switches = [s1, s2]

    c0 = net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=8888)

    net.addLink(h1, s1)
    net.addLink(s1, h2)
    net.addLink(s1, h3)
    net.addLink(s1, h4)

    net.start()
    start_bottle_process(network=net)
    CLI(net)
    net.stop()


