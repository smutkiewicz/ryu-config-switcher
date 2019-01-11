from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import lg
from mininet.node import Controller, RemoteController, OVSKernelSwitch, UserSwitch, OVSSwitch
from mininet.link import Link, TCLink


if __name__ == '__main__':
    lg.setLogLevel( 'info')

    net = Mininet(controller=RemoteController, link=TCLink, switch=OVSSwitch)

    h1 = net.addHost('h1')
    h2 = net.addHost('h2')

    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')
    s4 = net.addSwitch('s4')
    s5 = net.addSwitch('s5')

    c0 = net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=8888)

    net.addLink(h1,s1, bw =10)
    net.addLink(s1, s2, bw =10)
    net.addLink(s2, s4, bw =10)
    net.addLink(s4, h2, bw =10)
    net.addLink(s1, s5, bw =10)
    net.addLink(s5, s4, bw =10)
    net.addLink(s1,s3, bw =10)
    net.addLink(s3,s4, bw =10)

    net.start()
    CLI( net )
    net.stop()

