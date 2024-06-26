# Kursinis Darbas

## Įžanga

### Kursinio darbo tikslas

Kursinio darbo tikslas yra parašyti programą naudojant Python programavimo kalbą, išmokti panaudoti objektinio programavimo bei SOLID principus ir taisyklingai pritaikyti programai tinkančius dizaino šablonus.

### Kursinio darbo tema

Kursinio darbo tema yra *Skrydžių bilietų rezervavimo sistema*. Pasirinkau šią temą kad suprasčiau valdymo sistemų pagrindus bei veikimą.

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

## Pilna kodo analizė

### Skaitymas iš failo

Skaitymas iš failo yra apdorojamas klasės **ImportFromFile**. Klasė yra sukurta pasinaudojantis *Singleton* dizaino šablonu. *Singleton* yra panaudotas užtikrinti, kad informacija yra nuskaitoma tik vieną kartą iš tik vieno failo.

Failas *input.txt*, iš kurio yra skaitoma informacija, susideda iš daugiau kaip 2000 visų Europos sostinių kombinacijų. Informacija faile yra išdestyta tokiu būdu:

<img src="images/inputtext.png" width="400" height="auto">

Metodas **__load_city_to_airline** skaito kiekvieną eilutę ir išskiria kiekvieną žodį atskirtą kableliu priskiriant jį objektui.

- *city_from* - pirmas žodis; išvykimo miestas
- *city_to* - antras žodis; atvykimo miestas
- *airline* - trečias žodis; oro linijų bendrovė
- *gate* - ketvirtas žodis; vartai

<img src="images/importfromfile.png" width="400" height="auto">

### *Fly*

Pasirinkus *Fly* suveikia klasė **Fly**, kurioje yra iškviečiamos klasės **FlightInformation** ir **TimeInfo** bei visi klasių metodai.

<img src="images/img1.png" width="400" height="auto">

#### *name & surname*

Metodai **name** ir **surname** prašo vartotojo įvesti duomenis bei tikrina, ar įvestų duomenų tipas yra *string*. 

![name & surname](images/img23.png)

#### *starting_point & city_and_airline*

Metodai **starting_point** ir **city_and_airline** iškviečia inkapsuliuotus metodus *__validate_starting_point*, *__get_first_gate* ir *__get_airline*, prašo vartotojo įvesti norimus miestus ir patikrina, ar tokie egzistuoja.
Metodas *city_and_airline* taip pat priskiria *airline* ir *gate* atributus.

<img src="images/cityairlinecode.png" width="400" height="auto">

<img src="images/validcityairline.png" width="400" height="auto">

#### *select_flight_class*

Metodas *select_flight_class* yra skirtas skrydžio klasei pasirinkti. Vartotojas įrašo pageidaujama klasę, o metodas patikrina, ar tokia klasė egzistuoja ir iškviečia metodą **self._baggage_allowance** iš užklausai atitinkančios paveldančios klasės.

<img src="images/selectflightclass.png" width="400" height="auto">

<img src="images/childclassclass.png" width="400" height="auto">

#### *select_meal_preference*

Metodas **select_meal_preference** yra skirtas pageidaujamam maistui pasirinkti. Vartotojas įrašo pageidaujamą maisto rūšį, metodas patikrina, ar toks pasirinkimas egzistuoja ir iškviečia metodą **get_description** iš abstrakčios klasės **MealPreference**

<img src="images/selectmealpreference.png" width="400" height="auto">

<img src="images/abstract.png" width="200" height="auto">

#### seat

Metodas **seat** leidžia vartotojui pasirinkti norimą vietą lėktuve. Metodas tikrina, ar vartotojas įrašė tinkamą skaičių ir naudojant *try - except* išskyria *ValueError* jei buvo įrašyti netinkamo (ne *int*) tipo duomenys.

<img src="images/seat.png" width="400" height="auto">

#### ticket_number

Metodas **ticket_number** naudoja biblioteką **random** kad atsitiktinai parinktų bilieto numerį bei pakeičia jį į *string* duomenų tipą.

<img src="images/ticketnumber.png" width="400" height="auto">

#### date

Klasėje **TimeInfo** metodas **date** yra atsakingas už tinkamos datos parinkimą. Metodas užtikrina, kad vartotojo pasirinkta data būtų taisyklinga bei nebūtų praeityje. Tai yra padaryta naudojant *if - else* ir *try - except **ValueError***.

Datos formatavimui yra panaudota **datetime** biblioteka.

<img src="images/date.png" width="450" height="auto">

#### boarding_time

Taip pat klasėje **TimeInfo** yra metodas **boarding_time**, kuris atsako už tinkamo ir taisyklingo laiko parinkimą. Laikas yra įvedamas AM/PM formatu ir patikrinamas naudojant *if - else* bei *try - except **ValueError*** pagalba.

Laiko formatavimui yra panaudota **datetime** biblioteka.

<img src="images/boarding_time.png" width="450" height="auto">

### Rašymas į failą

Klasės **Fly** metodas **execute** ne tik iškviečia visus **FlightInformation** klasės metodus, bet taip pat įrašo visus duomenis į *output.txt* failą.

<img src="images/writetofile.png" width="450" height="auto">

### *DeleteBooking*

Klasė **DeleteBooking** yra skirta bilieto pašalinimui iš *output.txt* failo. Metodas **execute** šiuo atveju skaito visas eilutės ir skaičiuoja jų kiekį. Vartotojas įrašo vardą, kuris yra skirtas bilieto atpažinimui. Naudojant *while* ciklą yra skaičiuojamos eilutės nuo vardo eilutės iki pirmos tuščios eilutės (visi bilietai yra atskirti tuščia eilute). Kai ciklas pasiekia tuščia eilutę, informacija yra ištrinama ir visi bilietai eina atgal į ištrinto bilieto poziciją (jeigu ištrintas bilietas buvo tarp kitų bilietų).

<img src="images/deletebooking.png" width="400" height="auto">

### *ClearBooking*

Klasė **ClearBookingData** yra skirta visų bilietų ištrynimui iš *output.txt* failo. Metodas **execute** išrtina visą informaciją ir palieka tuščią failą.

<img src="images/cleardata.png" width="450" height="auto">

### Initialization

Klasė **Initialization** yra atsakinga už programos paleidimą ir pirmą vartotojo pasirinkimą. Priklausomai nuo įvesties, metodas **run_code** iškviečia metodą **execute** iš tinkamos klasės.

<img src="images/initialization.png" width="400" height="auto">

## OOP principai

1. **Abstrakcija**
    - Abstrakcija kode yra pasiekta naudojant abstrakčius metodus abstrakčioje klasėje **MealPreference**. Klasės **VegetarianMeal**, **KosherMeal** ir **RegularMeal** pateikia konkrečius abstračiojo metodo **get_description** implementacijas bei paslėpia metodų įgyvendinimo informaciją.
    
    <img src="images/abstract.png" width="300" height="auto">

2. **Inkapsuliacija**
    - Inkapsuliacija programoje yra panaudota tam, kad surinktumėme metodus vienoje vietoje ir apribotumėme prieigą prie svarbių kodo komponentų. Šiuo atveju, inkapsuliuojami yra metodai **FlightInformation** klasėje.

    <img src="images/encapsulation.png" width="400" height="auto">

3. **Paveldėjimas**
    - Paveldėjimas programoje yra panaudotas tam, kad klasė **FlightInformation** galėtų pasinaudoti informacija iš klasių **EconomyClass**, **BusinessClass** ir **FirstClass**. Tai leidžia lengvai keisti paveldinčių klasių vidinę informaciją tuo pačiu nekaičiant kodo tėvinėje klasėje.

    <img src="images/childclassclass.png" width="400" height="auto">

4. **Polimorfizmas**
    - Polimorfizmas leidžia panaudoti tuos pačius metodus skirtingoms operacijoms. Programoje jis yra panaudotas perrašant metodą **get_baggage_allowance** klasėse **EconomyClass**, **BusinessClass** ir **FirstClass**. Kiekviena klasė turi kitokį bagažo tipą ir priklausomai nuo pasirinkto skrydžio klasės metodas parodys kitokią informaciją iškviečiant jį **FlightInformation** klasėje metode **select_flight_class**.

    <img src="images/selectflightclass.png" width="400" height="auto">

## Dizaino šablonai

- **Singleton Pattern**
    
    *Singleton* yra panaudotas užtikrinti, kad informacija yra nuskaitoma tik vieną kartą iš tik vieno failo. *Singleton* kiekvieną kartą tikrina, ar jau egzistuoja iškvietimas ir neleidžia pakartotinai iškviesti metodo.

    <img src="images/importfromfile.png" width="400" height="auto">

- **Factory Method Pattern**

    Metodas **select_flight_class** išsiskiria kaip **Factory Method Pattern**. Jis deleguoja objektų konstrukciją paveldančioms klasėms **EconomyClass**, **BusinessClass** ir **FirstClass**, kas leidžia laisvai pridėti naujas subklasės prie programos nekeičiant kodo struktūros.

    <img src="images/selectflightclass.png" width="400" height="auto">

## Rezultatai ir apibendrinimas

- Pavyko sukurti programą, kurioje yra parodomi objektinio programavimo principai, panaudoti dizaino šablonai bei nėra paneigti SOLID principai

- Išmokau dirbti su *.txt* failais naudojant Python programavimo kalbą

- Daug sunkumų sukelė inkapsuliacija - norint ją užtikrinti pasunkėjo kodas ir sunku jį buvo suprasti

- Testai sukelė daug problemų, bet panaudojant *mocking* pavyko jas išspręsti

Apibendrindamas galiu teigti, kad pavyko sukurti veikiančią programą ir paversti savo pirminę viziją tikrove. Šis darbas padėjo man patobulėti programavimo srityje ir išmokė mane daug naujų įgūdžių.

Programą galima būtų patobulinti pridėdant daugiau skrydžių galimybių, bilietų kainas, pakeičiant laiko pasirinkimą bei labiau laikytis SOLID principų.
