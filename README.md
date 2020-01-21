# electircScootersDataCollector
Open notebook online click badge :)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marwin1991/electircScootersDataCollector/master)

To explor data use https://robomongo.org/download

If you use Linux make changes in docker-compose.yml

----------------------------------------------------------
###Ogólny opis:
Projekt polegał na pobraniu danych z api firm Bird, która udostępnia
hulajnogi w Krakowie oraz analizie tych danych.

###Zależność
W projekcie korzystaliśmy z:
* Python3 (zależności w pliku requirements.txt)
* Notebooków jupyter - komenda startująca notebook: start-jupyter.bat
* Docker

###Baza danych

Baza danych to MongoDB.
Można ją pobrać i zainstalować lub korzystająć z dockera postawić 
kontener, który tą bazę będzie hostować pod domyslnym portem dla 
MongoDB (:27017).

Wykorzystując docker baze startuje się poleceniem: 
```
docker-compose up
```

Do przegladania bazy danych można skorzystać z darmowego: https://robomongo.org/download
Lub jeśli chcemy zaimportować dane z CSV i miec wiecej opcji
to przez miesiąc można korzystac z https://studio3t.com/download/

W projekcie można znaleść dane:
* db.electric_scooters.csv - kolejne rekordy z skryptu pobierajacego dane
* db.travels_dis2.csv - dane uzyskane po przetowrzeniu danych z electric_scooters i
zapisanie w bazie inforamcji tylko o wypożyczeniach.
* weather_data.txt - dane dotyczace pogody, przerobić skrypt pobierajacy 
dane pogodowe, aby też wpisywał do bazy danych

Dwa pierwsze zbiory można zaimportować do MongoDB korzystując z Studio3T

###Pobieranie danych

Folder: gather_data

Należy uruchomić skrypty: (można dodać też wersje bashowe tych skryptów)
* job.bat
* weather.bat

W tym katalogu znajduje się plik:
```
test_get_scooters.ipynb
```

Który opisuje jak przetestować działanie API z PostMana oraz z Pythona


W tym katalogu znajduje się plik:
```
reorder_data.ipynb
```

W tym pliku znajduje się kod odpowiedzialny za przeanalizowanie
pobranych danych i storzenie pośredniej tabeli, która będzie zawierać
już tylko rekordy dotyczące wypożyczeń.

Warto sobie np po jednym dniu odpalić ten kod i wyczyścić tabele z 
danymi o połeniach hulajnóg co minutę. Można ten skrypt przerobić w taki sposób,
aby był można go odpalić np o 4 rano w czasie działania skryptu pobierającego dane o hulajnogach.

W tym pliku na końcu są też dwa wykresy, jednak są one nie optymalne bo opierają swoje działanie
na tabeli o położeniach hulajnóg a nie na tabeli z konkretnymi wypożyczeniami.

###Wykresy

Folder: charts_visualization

Zawiera nieoptymalne rysowanie wykresu na podstawie danych o połżeniach,
a nie z wykorzystaniem danych o konkretnych wypożyczeniach.

Niektóre wykresy można wygenerowac przeprowadzając analize danych w narzędziu
Studio3T. 

###Wizualizacje na mapach

Folder: maps_visualization

Zawiera rysowanie map z wykorzystaniem Google Maps, API key jest tam wpisany
na sztywno, znalezłem go na GitHubie wieć może być juz nie aktualny. Warto przeszukać 
GitHub/Google wpisując: gmaps.configure(api_key="AI
albo jakąś podobną frazę.


##Wizualizacje pogody

Folder: weather

Zawiera rysowanie wykresów pogodowych, sposób obliczania oceny pogody i wykresy.
