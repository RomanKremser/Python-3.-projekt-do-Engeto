Autor: Roman Kremser
Email: rkremser@seznam.cz
Discord: chimera #+9734

Popis projektu
Tento projekt je scraper výsledků voleb z roku 2017. Cílem je extrahovat data o výsledcích hlasování pro všechny obce v daném územním celku.

Instalace
Vytvořte virtuální prostředí pro tento projekt:
Příkaz pro vytvoření virtuálního prostředí
python3 -m venv volby-env
Aktivujte virtuální prostředí:
Windows:
volby-env\Scripts\activate
Nainstalujte potřebné knihovny ze souboru requirements.txt:
pip install -r requirements.txt
Poznámka: Pro správné fungování scraperu je třeba mít nainstalované knihovny requests a beautifulsoup4. Knihovny sys a csv jsou součástí standardní knihovny Pythonu a nemusí být instalovány zvlášť.

Použití
Soubor volby.py musí být spuštěn s dvěma argumenty:

Odkaz na územní celek, který chcete scrapovat. Například:

https://www.volby.cz/pls/ps2017nss/ps31?xjazyk=CZ&xkraj=14&xnumnuts=8105
Jméno výstupního souboru, do kterého budou uloženy výsledky. Například:

vysledky.csv




Výsledný soubor vysledky.csv obsahuje výsledky hlasování pro jednotlivé obce v daném územním celku. Každý řádek v souboru obsahuje následující informace:

Kód obce: Kód obce.
Název obce: Název obce.
Voliči v seznamu: Počet voličů v seznamu.
Vydáné obálky: Počet vydaných obálek.
Platné hlasy: Počet platných hlasů.
Kandidující strany: Počet hlasů pro jednotlivé kandidující strany.

Ukázka obsahu výstupního souboru vysledky-Opava.csv:
code,location,registered,envelopes,valid,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Česká národní fronta,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,Česká strana národně sociální,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů
512974,Bělá,559,379,375,22,0,0,27,1,9,15,3,8,5,1,1,18,0,1,15,150,0,1,30,0,3,0,1,63
506192,Bohuslavice,1 380,908,905,48,3,1,48,0,20,32,3,6,9,1,2,82,0,1,47,349,0,0,141,0,3
