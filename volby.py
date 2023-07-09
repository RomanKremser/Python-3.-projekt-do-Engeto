import sys
import csv
import requests
import bs4

def scrape_data(url):
    get_link = requests.get(url)
    html_code = bs4.BeautifulSoup(get_link.text, 'html.parser')
    
    voters = []
    attendance = []
    valid_ones = []

    header = ['code', 'location', 'registered', 'envelopes', 'valid']

    urls_uzemni_celky = [] 

    kody_obci = []
    nazvy_obci = []
    all_voters = []
    all_envelopes = []
    all_valid_votes = []
    parties = []
    hlasy_all = []

    link_search = html_code.find_all("td", "cislo")

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

        parties_temp = html_uc.find_all("td", "overflow_name")
        for party in parties_temp:
            zeby_podruhe = party.find_next("td")
            number_temp = zeby_podruhe.text
            number_temp_number = number_temp.replace('\xa0', '').replace(' ', '')
            hlasy.append(number_temp_number)

        hlasy_all.append(hlasy)

        if not seznam_stran_nacten:
            for party in parties_temp:
                parties.append(party.text)
            seznam_stran_nacten = True
            header += parties

    data = []
    for i in range(len(kody_obci)):
        temp = []
        temp.append(kody_obci[i])
        temp.append(nazvy_obci[i])
        temp.append(all_voters[i])
        temp.append(all_envelopes[i])
        temp.append(all_valid_votes[i])
        temp += hlasy_all[i]
        data.append(temp)

    return header, data

def save_data(header, data, csv_file):
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        f_writer = csv.writer(f)
        f_writer.writerow(header)
        f_writer.writerows(data)

def print_summary(header, data):
    print("Hlavička:")
    print(header)
    print("První řádek dat:")
    print(data[0])

def get_total_votes(data):
    total_votes = sum([int(row[2].replace('\xa0', '')) for row in data])
    return total_votes

def get_winner(data):
    max_valid_votes = 0
    winner = None
    for row in data:
        valid_votes = int(row[4].replace('\xa0', '').replace(' ', ''))
        if valid_votes > max_valid_votes:
            max_valid_votes = valid_votes
            winner = row[1]
    return winner

def main():
    if len(sys.argv) != 3:
        print('Zadal jsi nesprávný počet argumentů.')
        quit()

    url = sys.argv[1]
    csv_file = sys.argv[2]

    header, data = scrape_data(url)
    save_data(header, data, csv_file)
    print_summary(header, data)
    total_votes = get_total_votes(data)
    print("Celkový počet voličů:", total_votes)
    winner = get_winner(data)
    print("Vítězná obec:", winner)

if __name__ == '__main__':
    main()
