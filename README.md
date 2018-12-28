# ryu-config-switcher

Uruchamianie topologii o nazwie `topo1`:


`sudo mn --custom topo.py --topo topo1 --mac --controller remote --switch ovsk`


Remote controller: ip='127.0.0.1', port=8888


`cd /home/ubuntu/ryu && ./bin/ryu-manager --verbose ryu/app/simple_switch_13.py`

http://mininet.org/walkthrough/#custom-topologies
