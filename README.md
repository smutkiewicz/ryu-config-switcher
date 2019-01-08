# ryu-config-switcher


Wszystko uruchamiane z folderu repozytorium.


## Mininet

### Uruchamianie z przykładową topologią:


`sudo python mytopo.py`


## Ryu

### Remote controller: ip='127.0.0.1', port=8888


`ryu-manager --ofp-tcp-listen-port 8888 simple_switch_13.py`


Serwer z REST działa na porcie 8181. IP na którym powinien działać serwer jest ip interfejsu enp0s3. Karta sieciowa VM powinna działać w trybie bridge.


## Opis inicjalizacji komunikacji RyuPilot + kontroler:

1. Zainstaluj aplikację [RyuPilot](https://play.google.com/apps/testing/studios.aestheticapps.ryupilot).
2. Upewnij się, że twoja VM działa w trybie bridge karty sieciowej (Ustawienia > Sieć > Karta sieciowa podłączona do: "motkowana karta sieciowa (bridge)").
3. Znajdź interfejs enp0s3 (pierwszy, który zawiera adres IP typu 198... a nie 10.0.0 ...).
4. Ustaw IP tego interfejsu w skrypcie `simple_switch_13.py` jako wartość stałej `HOST_IP_ADDRESS`.
5. Ustaw to samo IP w swojej aplikacji RyuPilot.
6. Uruchom kontroler komendą `ryu-manager --ofp-tcp-listen-port 8888 simple_switch_13.py`
7. Sprawdź, czy terminal printuje przychodzące POST requesty, jeśli tak - konfiguracja zakończona.
