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
- Oro uosto vartai
- Bilieto numeris

Bilieto duomenys yra išsaugomi į *.txt* failą.

## Kodo analizė

Analizuosiu kodą dalinant jį į keturius pradinius pasirinkimus.

### *Fly*

Pasirinkus *Fly* suveikia klasė **Fly**, kurioje yra iškviečiamos klasės **FlightInformation** ir **TimeInfo** bei visos tu klasių funkcijos.

<img src="img1.png" width="400" height="auto">