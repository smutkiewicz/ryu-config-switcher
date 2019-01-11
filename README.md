# ryu-config-switcher

## 1. Cel projektu

Implementacja rozwiązania, w którym konfiguracja sieci emulowanej w programie [mininet](http://mininet.org/) może być przełączana w wyniku interakcji aplikacji klienckiej (uruchamianej np. na smartfonie Android) i sterownika sieci SDN.

## 2. Architektura rozwiązania

Aplikacja RyuPilot na system operacyjny Android (napisana w języku Kotlin), kontroler [Ryu](https://osrg.github.io/ryu/) (Python) z mini serwerem HTTP (biblioteka [bottle.py](https://bottlepy.org/docs/dev/)) + mininet, oba pracujące na tej samej maszynie wirtualnej.

## 3. Założenia projektowe

Maksymalnym obrębem pracy pilota jest, dla ułatwienia, lokalna sieć WiFi. Kontroler pracuje na porcie `8888`, zaś serwer HTTP na porcie `8181`. Mobilna aplikacja kliencka ma możliwość ręcznego ustawienia adresu IP komputera/wirtualnej maszyny pod który będzie wysyłała zapytania. Aplikacja będzie dostępna do pobrania ze Sklepu Play w ramach (otwartego programu beta)[https://play.google.com/apps/testing/studios.aestheticapps.ryupilot]. 

Podstawowym zapytaniem kierowanym do kontrolera SDN jest `POST` zawierający `setting_id` - identyfikator ustawienia sieci znanego wewnętrznie przez sterownik. Implementacja bardziej zaawansowanych zapytań nie będzie stanowiło problemu, jako że projekt jest niejako swoistym "Proof Of Concept".

## 4. Scenariusz interakcji

Użytkownik, będąc w obrębie sieci WiFi, w której jest również komputer z maszyną wirtualną z serwerem nasłuchującym żądań typu POST od klientów, ma możliwość przełączenia konfiguracji sieci emulowanej w programie mininet.

## 5. Konfiguracja

### Opis inicjalizacji komunikacji RyuPilot + kontroler:

*Uwaga!* Przed konfiguracją upewnij się, że masz zainstalowanego Pythona (wersja 2.7), kontroler Ryu, Mininet, bibliotekę bottle.py

1. Zainstaluj aplikację [RyuPilot](https://play.google.com/apps/testing/studios.aestheticapps.ryupilot).
2. Jeśli używasz VM, upewnij się, że działa ona w trybie bridge karty sieciowej (w programie VirtualBox: Ustawienia > Sieć > Karta sieciowa podłączona do: "mostkowana karta sieciowa (bridge)").
3. Jeśli używasz VM, znajdź interfejs karty sieciowej widziany przez Twój komputer.
4. Ustaw IP tego interfejsu w skrypcie `simple_switch_13.py` jako wartość stałej `HOST_IP_ADDRESS`.
5. Ustaw to samo IP w swojej aplikacji RyuPilot.
6. Uruchom kontroler komendą: `ryu-manager --ofp-tcp-listen-port 8888 simple_switch_13.py`
7. Uruchom program Mininet z przykładową topologią komendą: `sudo python mytopo.py`
8. Sprawdź, czy terminal printuje przychodzące POST requesty, jeśli tak - konfiguracja zakończona.
9. Sprawdź, czy program Mininet prawidłowo połączył się z zewnętrznym kontrolerem.

## 6. Przykładowa sieć i zmieniane ustawienia

### Sieć

### setting_id=1

### setting_id=2

### setting_id=3

### setting_id=4

