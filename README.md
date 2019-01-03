# ryu-config-switcher


Wszystko uruchamiane z folderu repozytorium.


## Mininet

### Uruchamianie z przykładową topologią:


`sudo python mytopo.py`


## Ryu

### Remote controller: ip='127.0.0.1', port=8888


`ryu-manager --ofp-tcp-listen-port 8888 simple_switch_13.py`

