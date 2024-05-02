# Kursinis Darbas

## Įžanga

### Kursinio darbo tikslas

Kursinio darbo tikslas yra parašyti programą naudojant Python programavimo kalbą, išmokti panaudoti objektinio programavimo bei SOLID principus ir taisyklingai pritaikyti programai tinkančius dizaino šablonus.

### Kursinio darbo tema

Kursinio darbo tema yra *Skrydžių bilietų rezervavimo sistema*. Pasirinkau šią temą kad suprasti valdymo sistemų pagrindus bei veikimą.

### Kaip naudotis programa?

Programos veikimas remiasi vartotojo pasirinkimais: nuo vartotojo priklauso, ką darys programa.
Paleidus programą vartotojas gali pasirinkti tokius veiksmus:
- *Fly* - rezervuoti bilietą
- *Delete* - pašalinti vieną iš išsaugotų bilietų
- *Clear* - pašalinti visus išsaugotus bilietus
- *Exit* - nutraukti programą

### Programos veikimas

Pasirinkus *Fly*, vartotojas žingsnis po žingsnio įrašo visą reikalingą informaciją:
- Vardas
- Pavardė
- Išvykimo miestas
- Atvykimo miestas
- Skrydžio klasė
- Pageidaujamas maistas
- Sėdimos vietos numeris
- Išvykimo data ir laiką

Priklausomai nuo vartotojo pasirinkimų automatiškai prie bilieto yra priskiriami:
- Bagažo norma
- Oro linijų bendrovė
- Vartai
- Bilieto numeris

Bilieto duomenys yra išsaugomi į *.txt* failą.

## Kodo analizė

### Skaitymas iš failo

Skaitymas iš failo yra apdorojamas klasės **ImportFromFile**. Klasė yra sukūrta pasinaudojant *Singleton* dizaino šablonu. *Singleton* yra panaudotas užtikrinti, kad informacija yra nuskaitoma tik vieną kartą iš tik vieno failo.

Failas *input.txt*, iš kurio yra skaitoma informacija, susideda iš daugiau kaip 2000 visų Europos sostinių kombinacijų. Informacija faile yra išdestyta tokiu būdu:

<img src="inputtext.png" width="400" height="auto">

Funkcija **__load_city_to_airline** skaito kiekvieną eilutę ir išskiria kiekvieną žodį atskirta kableliu priskiriant jį objektui.

- *city_from* - pirmas žodis; išvykimo miestas
- *city_to* - antras žodis; atvykimo miestas
- *airline* - trečias žodis; oro linijų bendrovė
- *gate* - ketvirtas žodis; vartai

<img src="importfromfile.png" width="400" height="auto">

### *Fly*

Pasirinkus *Fly* suveikia klasė **Fly**, kurioje yra iškviečiamos klasės **FlightInformation** ir **TimeInfo** bei visos tu klasių funkcijos.

<img src="img1.png" width="400" height="auto">

#### *name & surname*

Funkcijos **name** ir **surname** prašo vartotojo įvesti duomenis bei tikrina, ar įvestų duomenų tipas yra *string*. 

Abi funkcijos yra inkapsuliuotos.

![name & surname](img23.png)

#### *starting_point & city_and_airline*

Funkcijos **starting_point** ir **city_and_airline** iškviečia inkapsuliotus metodus *__validate_starting_point*, *__get_first_gate* ir *__get_airline*, prašo vartotojo įvesti norimus miestus ir patikrina, ar tokie egzistuoja.
Funkcija *city_and_airline* taip pat priskiria *airline* ir *gate*.

Abi funkcijos yra inkapsuliotos.

<img src="cityairlinecode.png" width="400" height="auto">

<img src="validcityairline.png" width="400" height="auto">
