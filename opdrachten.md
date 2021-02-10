# Opdrachten voor Artificial intelligence Minor

- [Opdrachten voor Artificial intelligence Minor](#opdrachten-voor-artificial-intelligence-minor)
- [Week 4](#week-4)
  - [Inductie](#inductie)
    - [Checklist](#checklist)
- [Week 6](#week-6)
  - [Searching](#searching)
    - [Checklist](#checklist-1)
- [Week 9](#week-9)
  - [Logic Programming](#logic-programming)
    - [Checklist](#checklist-2)
  - [Text Classification](#text-classification)
    - [Checklist](#checklist-3)

# Week 4

## Inductie

Werk onderstaande opdrachten uit met inductie. Beschrijf per opdracht:

- de inductiehypothese
- Het algoritme in pseudocode
- Een zelf gekozen voorbeeld en uitwerking hoe het probleem opgelost wordt.
  > Tip: Maak deze (ook) vooraf om het probleem te begrijpen / beschrijven

1. Sorteer een rij van n getallen op 2 manieren:
   1. Decrease and conquer
   2. Divide and conquer
2. Draai een string van s letters om.
3. Gegeven een weegschaal en (een lijst van) n stukken lood van verschillende gewichten. Verdeel de n gewichten zodanig dat de weegschaal (zoveel mogelijk) in balans is.
4. Het spel ‘De torens van Hanoi’ bestaat uit een stapel van N verschillende schijven en drie pinnen: de bron (S), de hulp (A) en de bestemming (D).
   De stapel gesorteerde schijven moet verplaatst worden van S naar D, daarbij kan gebruik gemaakt worden van A. Er mag maar 1 schijf tegelijk verplaatst worden en er mag nooit een grotere schijf op een kleinere schijf geplaatst worden.

### Checklist

- [ ] opdracht 1
- [ ] opdracht 2
- [ ] opdracht 3
- [ ] opdracht 4

# Week 6

## Searching

Kies een van onderstaande mogelijkheden:

- Ontwerp en realiseer een algoritme dat de optimale oplossing geeft voor minimaal 3 verschillende Sokoban levels.
- Ontwerp en realiseer een algoritme dat TicTacToe kan spelen tegen een menselijke speler en daarbij altijd probeert te winnen.

Op te leveren onderdelen:

1. Formele beschrijving van het probleem, in de vorm van de 5 componenten:
   1. initial state
   2. actions
   3. transition model
   4. goal test
   5. path cost
2. Onderbouwde keuze van de gebruikte zoektechniek
   1. Met afweging van alternatieven
   2. Inclusief beschrijving van compleetheid en optimaliteit.
3. Beschrijving van het algoritme in pseudocode
   1. Als een informed zoektechniek gekozen wordt: beschrijf dan ook duidelijk hoe de heuristiek opgebouwd is.
4. Performance van de realisatie
   1. Theoretische performance van het algoritme in tijd en ruimte
   2. Feitelijke performance in grafiekvorm (zowel tijd als ruimte).
5. Realisatie van het algoritme 1. Programmeertaal mag zelf gekozen worden
   Het gekozen en beschreven zoekalgoritme moet duidelijk terugkomen in de realisatie!

### Checklist

- [ ] opdracht 1
- [ ] opdracht 2
- [ ] opdracht 3
- [ ] opdracht 4
- [ ] opdracht 5

# Week 9

## Logic Programming

In de losse pdf “De prinses of de tijger” staan 12 opdrachten die op te lossen zijn met behulp van predicaten- en propositielogica.
Beschrijf per opdracht het volgende:

- Beschrijf met behulp van predicatenlogica de feiten en regels.
- Realiseer de oplossing in [Alloy](http://alloytools.org/)
  > Tip: [Alloy tutorials](http://alloytools.org/tutorials/online/index.html)
- Laat door middel van een screenshot zien dat de oplossing/uitwerking correct is.

### Checklist

- [ ] opdracht 1
- [ ] opdracht 2
- [ ] opdracht 3
- [ ] opdracht 4
- [ ] opdracht 5
- [ ] opdracht 6
- [ ] opdracht 7
- [ ] opdracht 8
- [ ] opdracht 9
- [ ] opdracht 10
- [ ] opdracht 11
- [ ] opdracht 12

## Text Classification

Ontwerp en realiseer een taalherkenningsprogramma (classificatie) met behulp van trigrams (Markov van de 2e orde). Het programma is in staat om minstens 6 verschillende talen te herkennen.

Invoer:  
&emsp;&emsp;Een zin in een bepaalde taal (voorbeeldzinnen mogen voorgeprogrammeerd worden, maar er moet de mogelijkheid bestaan om tijdens het runnen een zin in te kunnen voeren).

Uitvoer:  
&emsp;&emsp;De taal waarin de tekst is geschreven.  
&emsp;&emsp;Daarnaast een lijst van de gekozen talen en het resultaat van de kansberekening van zowel de bi- en trigrammen van de invoerzin.

Op te leveren onderdelen:

1. Beschrijf het programma gedetailleerd op de volgende onderdelen:

   1. Welke dataset(s) zijn gebruikt en waar komen ze vandaan
   2. Hoe is het programma getraind. Beschrijf ook de manier van opslag.
   3. Beschrijf hoe de kansberekening per bi- en trigram plaats vindt.
   4. Hoe is smoothing toegepast?
      > Zie het losse document “trigrams.pdf” voor een toelichting en een voorbeeld.
2. Realiseer het programma
   1. 1 programma waarin zowel de vergelijking wordt gedaan voor bi- en tri-grammen
   2. Programmeertaal mag zelf gekozen worden
3. Evalueer de werking
   1. Vergelijk de bi- en tri-grams op correctheid
   2. Vergelijk de bi- en tri-grams op performance (in tijd)

### Checklist

- [ ] opdracht 1
- [ ] opdracht 2
- [ ] opdracht 3
<!-- The styling of the markdown file -->
<style type="text/css">
    ol ol { list-style-type: upper-alpha; }
</style>