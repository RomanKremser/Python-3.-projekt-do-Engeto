# projekt_3.py: první projekt do Engeto Online Python Akademie
# author: Ŕoman Kremser
# email: rkremser@seznam.cz
# discord: chimera #+9734
# projekt_3.py: první projekt do Engeto Online Python Akademie
# author: Ŕoman Kremser
# email: rkremser@seznam.cz
# discord: chimera #+9734
import sys
import csv
import requests # pip install requests
import bs4      # pip install beautifulsoup4


voters = []
attendance = []
valid_ones = []

if len(sys.argv) != 3:
    print('Zadal jsi nesprávný počet argumentů. ')
    quit()

get_link = requests.get(sys.argv[1])

html_code = bs4.BeautifulSoup(get_link.text, 'html.parser')
csv_file = sys.argv[2]

header = ['code', 'location', 'registered', 'envelopes', 'valid']

urls_uzemni_celky = [] 

kody_obci = []
nazvy_obci = []
all_voters = []
all_envelopes = []
all_valid_votes = []
parties = []
hlasy_all = []

link_search = html_code.find_all("td","cislo")

for town in link_search:
    link_town = town.find("a")
    if link_town is not None:
        href_town = link_town["href"]
        kody_obci.append(link_town.text)
        urls_uzemni_celky.append(f"https://volby.cz/pls/ps2017nss/{href_town}")
    zeby = town.find_next("td")
    nazvy_obci.append(zeby.text)

seznam_stran_nacten = False

for uzemni_celek in urls_uzemni_celky:
    html_path = requests.get(uzemni_celek)
    html_uc = bs4.BeautifulSoup(html_path.text, 'html.parser')

    voters = html_uc.find("td", headers="sa2")
    envelopes = html_uc.find("td", headers="sa3")
    valid_votes = html_uc.find("td", headers="sa6")
    
    all_voters.append(voters.text)
    all_envelopes.append(envelopes.text)
    all_valid_votes.append(valid_votes.text)
    
    hlasy = []

    parties_temp = html_uc.find_all("td","overflow_name")
    for party in parties_temp:
         zeby_podruhe = party.find_next("td")
         number_temp = zeby_podruhe.text
         number_temp_number = number_temp.replace('\xa0', ' ')
         hlasy.append(number_temp_number)
    
    hlasy_all.append(hlasy)

    if not seznam_stran_nacten:
        for party in parties_temp:
             parties.append(party.text)
        seznam_stran_nacten = True
        header += parties

with open(csv_file, 'w', newline='',encoding='utf-8') as f:
        f_writer = csv.writer(f)
        f_writer.writerow(header)
        
        index = 0
        for x in range(len(kody_obci)):
            temp = []
            temp.append(kody_obci[index])
            temp.append(nazvy_obci[index])
            temp.append(all_voters[index])
            temp.append(all_envelopes[index])
            temp.append(all_valid_votes[index])
            temp += hlasy_all[index]
            f_writer.writerow(temp)
            index += 1
