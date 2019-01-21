from multiprocessing import Process

from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import lg
from mininet.node import RemoteController
from bottle import request, Bottle
import socket

IP_DATA_FILE = 'ip_data.txt'
SERVER_PORT = 8181


class App:

    def __init__(self):
        self.app = Bottle()
        self.net = Mininet(controller=RemoteController)

        h1 = self.net.addHost('h1')
        h2 = self.net.addHost('h2')
        h3 = self.net.addHost('h3')


        s1 = self.net.addSwitch('s1')
        s2 = self.net.addSwitch('s2')
        s3 = self.net.addSwitch('s3')

        c0 = self.net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=8888)

        self.net.addLink(h1, s1)
        self.net.addLink(s1, s2)
        self.net.addLink(s2, h2)
        self.net.addLink(s1, s3)
        self.net.addLink(s3, s2)
        self.net.addLink(s3, h3)
        pass

    def run(self):
        bp = self.start_bottle_process()
        self.run_mininet()
        bp.terminate()

    def start_bottle_process(self):
        p = Process(target=self.run_bottle)
        p.start()
        return p

    def run_mininet(self):
        self.net.start()
        CLI(self.net)
        self.net.stop()

    def run_bottle(self):
        self.app.route('/check_connection/', callback=self.check_connection)
        self.app.post('/change_setting/', callback=self.change_setting)
        self.app.route('/stop', callback=self.stop)
        self.app.run(host=self.read_ip(), port=SERVER_PORT)

    def read_ip(self):
        f = open(IP_DATA_FILE, "r")
        my_ip = f.readline().rstrip('\n')

        if self.is_valid_ipv4_address(my_ip):
            print('Bottle server IP set as = ' + my_ip)
            print('Set server IP in your RyuPilot app as \'' + my_ip + '\'.')
            return my_ip
        else:
            print('Bottle server IP = ' + my_ip + ' invalid, changed to = localhost.')
            return 'localhost'

    def is_valid_ipv4_address(self, address):
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

    def check_connection(self):
        print("Connection correct.")
        return "<p>Connection correct.</p>"

    def change_setting(self):
        postdata = request.body.read()
        json = request.json
        setting_id = json["setting_id"]
        print("Requested setting_id = " + str(setting_id))

        #for safety remember to always update all links
        #everything off
        if setting_id == 1:
            print('Setting network up.')
            print('Setting h3 to be connected through s3 & disconnecting s1 from s2')
            self.net.configLinkStatus(src='h1', dst='s1', status='up')
            self.net.configLinkStatus(src='s2', dst='h2', status='up')
            self.net.configLinkStatus(src='s1', dst='s2', status='down')
            self.net.configLinkStatus(src='s1', dst='s3', status='up')
            self.net.configLinkStatus(src='s3', dst='h3', status='up')
            self.net.configLinkStatus(src='s3', dst='s2', status='up')
            print(str(setting_id) + " set successfully.")

        if setting_id == 2:
            print('Disconnecting h2.')
            print('Setting links h1-s1 and s1-h2 to status=\'up\'.')
            self.net.configLinkStatus(src='h1', dst='s1', status='up')
            self.net.configLinkStatus(src='s1', dst='s2', status='up')
            self.net.configLinkStatus(src='s2', dst='h2', status='up')
            self.net.configLinkStatus(src='s1', dst='s3', status='down')
            self.net.configLinkStatus(src='s3', dst='s2', status='down')
            self.net.configLinkStatus(src='s3', dst='h3', status='down')
            print(str(setting_id) + " set successfully.")

        if setting_id == 3:
            print('Disconnecting h1.')
            self.net.configLinkStatus(src='h1', dst='s1', status='down')
            self.net.configLinkStatus(src='s2', dst='h2', status='up')
            self.net.configLinkStatus(src='s1', dst='s2', status='down')
            self.net.configLinkStatus(src='s1', dst='s3', status='down')
            self.net.configLinkStatus(src='s3', dst='h3', status='up')
            self.net.configLinkStatus(src='s3', dst='s2', status='up')
            print(str(setting_id) + " set successfully.")

        if setting_id == 4:
            print('Setting network down.')
            print('Setting links h1-s1 and s1-h2 to status=\'down\'.')
            self.net.configLinkStatus(src='h1', dst='s1', status='down')
            self.net.configLinkStatus(src='s2', dst='h2', status='down')
            self.net.configLinkStatus(src='s1', dst='s3', status='down')
            self.net.configLinkStatus(src='s3', dst='s2', status='down')
            self.net.configLinkStatus(src='s3', dst='h3', status='down')
            self.net.configLinkStatus(src='s1', dst='s2', status='down')
            print(str(setting_id) + " set successfully.")

    def stop(self):
        self.net.stop()
        print("Requested stop.")


if __name__ == '__main__':
    lg.setLogLevel( 'info')
    App().run()
