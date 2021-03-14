# Proof Checker

Dit programma kijkt gevolgtrekkingen in de vorm van opeenvolgingen van `assert`-opdrachten na op geldigheid.

Elke gevolgtrekking moet voorzien zijn van een verantwoording. Dit programma ondersteunt momenteel de volgende
verantwoordingen.

Hieronder gebruiken we het begrip *conjunct* om elk der leden van een *en*-bewering aan te duiden.
Bijvoorbeeld: de bewering `A and B and C` bestaat uit de drie conjuncten `A`, `B`, en `C`. 

Een gevolgtrekking bestaat uit twee opeenvolgende `assert`-opdrachten. De eerste noemen we
het *antecedent* en de tweede het *consequent*.

### Z

De verantwoording `Z` verantwoordt het toevoegen van conjuncten die elk op zich afleidbaar zijn uit de
wetten van de gehele getallen (associativiteit en commutativiteit van de optelling en de vermenigvuldiging, nul is een
neutraal element, de negatie is een tegengestelde, distributiviteit van de vermenigvuldiging over de optelling.)

Bijvoorbeeld:
```python
assert i == 0
assert i == 0 and 1 <= 0 + 1 # Z
```

De conjunct `1 <= 0 + 1` is afleidbaar uit de wetten van de gehele getallen.

### Z op i

De verantwoording `Z op i` verantwoordt het toevoegen van conjuncten die elk afleidbaar zijn
uit de `i`de conjunct van het antecedent met behulp van de wetten van de gehele getallen.

Bijvoorbeeld:
```python
assert i <= n and i < n
assert i + 1 <= n # Z op 2
```
De conjunct `i + 1 <= n` kan afgeleid worden uit de tweede conjunct van het antecedent, nl.
`i < n`, met behulp van
de wetten van de gehele getallen.

### Herschrijven met i in j

De verantwoording `Herschrijven met i in j` is enkel toepasbaar als de `i`de conjunct een gelijkheid `E1 == E2` is.
Ze verantwoordt het toevoegen van conjuncten die bekomen kunnen worden door sommige voorkomens van `E1` in de
`j`de conjunct van het antecedent te vervangen door `E2`, en/of door sommige voorkomens van `E2` te vervangen door `E1`.

Bijvoorbeeld:
```python
assert i == 0 and 1 <= 0 + 1
assert 1 <= i + 1 # Herschrijven met 1 in 2
```
Je kan `1 <= i + 1` bekomen door `0` te vervangen door `i` in `1 <= 0 + 1`.

### wet op i1, i2, ...

Je kan *wetten* declareren. Die kan je dan toepassen om gevolgtrekkingen te verantwoorden.

Een wet associeert een naam met een als-dan-bewering. De conjuncten van de *als*-voorwaarde van de als-dan-bewering
noemen we de *premissen* van de wet. De *dan*-voorwaarde noemen we de *conclusie* van de wet.

Bij het toepassen van een wet moet je voor
elke premisse een conjunct van het antecedent opgeven dat met
die premisse overeenkomt. Je kan met die toepassing dan een overeenkomstige instantiatie van de conclusie verantwoorden.

Bijvoorbeeld:
```python
# Wet LeAntisym: x <= y and y <= x ==> x == y

assert i <= n and n <= i
assert i == n # LeAntisym op 1 en 2
```
In deze verantwoording wordt de eerste conjunct `i <= n` van het antecedent opgegeven als overeenkomstige
conjunct voor de eerste premisse `x <= y` van de wet `LeAntisym`, en de tweede conjunct `n <= i` van het
antecedent wordt opgegeven als overeenkomstige conjunct voor de tweede premisse `y <= x`.
Dit verantwoordt de nieuwe conjunct `i == n`; dit is de overeenkomstige instantiatie van de conclusie van de wet.

### Herschrijven met wet op i1, i2, ... in j

Als de conclusie van een wet een gelijkheid is, kan je het toevoegen van een conjunct overeenkomstig met de conclusie
van de wet, en het herschrijven met die nieuwe conjunct in een andere conjunct, in één stap doen als volgt:

```python
# Wet MaxList2: 1 <= i < len(xs) ==> max(xs[:i + 1]) == max(max(xs[:i]), xs[i])

assert 1 <= i < len(xs) and max_ == max(xs[:i]) and xs[i] == max(max(xs[:i]), xs[i])
assert 1 <= i < len(xs) and max_ == max(xs[:i]) and xs[i] == max(xs[:i + 1]) # Herschrijven met MaxList2 op 1 en 2 in 4
```

## Voorbeelden

Je vindt verantwoordingen voor alle gevolgtrekkingen die voorkomen in het document *Bewijssilhouetten opstellen* en in
de presentaties *Bewijssilhouetten opstellen - Voorbeeld (partiële correctheid)* en
*Bewijssilhouetten opstellen - Voorbeeld (totale correctheid)* in het bestand
`gevolgtrekkingen_uit_voorbeeldsilhouetten.py`.
