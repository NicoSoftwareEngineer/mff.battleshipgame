# Anotace projektu – Hra „Lodě“

## Identifikace
- Nicolas Skuček
- NPRG030
- 1.10.2025

## Popis problému
Cílem projektu bude vytvořit konzolovou hru „Lodě“ pro jednoho až dva hráče. Hráči budou chtít hrát klasickou hru, kde se střídají ve střelbě na protivníkovu herní plochu a snaží se potopit všechny jeho lodě. Hlavním problémem bude zajistit logiku hry, správné umístění lodí, střídání tahů a možnost hry proti počítači.

## Formalizace problému
Hra bude probíhat na dvou mřížkách (jedna pro každého hráče), kde každý hráč bude mít čtyři lodě různých velikostí – 2, 3, 4 a 5 políček. Hráči budou zadávat souřadnice políček, kam chtějí umístit lodě, a poté souřadnice, kam chtějí střílet. Hra bude pokračovat střídáním tahů, dokud jeden z hráčů nepotopí všechny lodě soupeře. Pokud hráč zasáhne loď, bude pokračovat ve střelbě; pokud netrefí, tah přejde na soupeře.

## Návrh průbehu hry
1. Inicializace hry a výběr počtu hráčů.  
2. Umístění lodí hráči a počítačem (počítač umístí lodě náhodně).  
3. Střídání tahů hráčů:  
   - Zadání souřadnic střely.  
   - Kontrola zásahu nebo minelu.  
   - Aktualizace herní plochy a stavu lodí.  
4. Kontrola výhry po každém tahu.  
5. Ukončení hry a vyhlášení vítěze.

## Algoritmus pro hráče počítače:
1. Počítač zvolí random políčko na poli.
2. Pokud se trefí tak další políčko zkusí nahoru, dolu, doprava nebo doleva a pak v tom směru pokračuje dokud loď nepotopí.
3. Pokud netrefí, cyklus se opakuje.

## Specifikace vstupů/výstupů
- **Vstupy:**  
  - Počet hráčů (1 nebo 2).  
  - Souřadnice umístění lodí (např. „4B,5B,6B“).  
  - Souřadnice střel (např. „3C“).  

- **Výstupy:**  
  - Zobrazení herní plochy pro každého hráče.  
  - Informace o zásahu, minelu nebo potopení lodi.  
  - Informace o vítězi hry.

## Popis rozhraní
Hra bude realizována v **konzolovém rozhraní**, kde hráči budou zadávat příkazy pomocí klávesnice. Interaktivní funkce budou zahrnovat:  
- Zadávání souřadnic lodí a střel.  
- Zobrazení aktualizované herní plochy po každém tahu.  
- Zobrazení informací o zásahu, minelu nebo potopení lodi.  
- Možnost výběru hry proti počítači nebo druhému hráči.

Projekt bude realizován v Pythonu s využitím **objektově orientovaného programování (OOP)**, což zajistí modulární a přehledný kód.
