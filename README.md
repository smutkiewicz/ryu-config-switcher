# ryu-config-switcher


Wszystko uruchamiane z folderu repozytorium.


## Mininet

### Uruchamianie z topologią o nazwie `topo1`:


`sudo mn --custom topo.py --topo topo1 --mac --controller remote --switch ovsk`


## Ryu

### Remote controller: ip='127.0.0.1', port=8888


`ryu-manager simple_switch_13.py`

