Projekt: Scraper výsledků voleb z roku 2017
Autor: Roman Kremser
Email: rkremser@seznam.cz
Discord: chimera #+9734

Popis projektu
Tento projekt je scraper výsledků voleb z roku 2017. Cílem je extrahovat data o výsledcích hlasování pro všechny obce v daném územním celku.
nstalace
Vytvořte virtuální prostředí pro tento projekt:
python3 -m venv volby-env
Aktivujte virtuální prostředí:
Windows:
shell
volby-env\Scripts\activate
Nainstalujte potřebné knihovny ze souboru requirements.txt:
shell
Copy code
pip install -r requirements.txt
Soubor volby.py musí být spuštěn s dvěma argumenty:
Odkaz na územní celek, který chcete scrapovat. Například: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2102
Jméno výstupního souboru, do kterého budou uloženy výsledky. Například: vysledky.csv
