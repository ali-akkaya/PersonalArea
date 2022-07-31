from bs4 import BeautifulSoup
import requests

text = requests.get("https://futurology.life/43-most-innovative-estonia-based-machine-learning-companies/").text
soup = BeautifulSoup(text, 'html.parser')
elements = soup.find_all('div', class_='wp-block-cover alignwide has-black-background-color has-background-dim '
                                       'is-position-center-center')

# Create a function to write line into txt file
def write_to_file(line):
    with open("companies.txt", "a") as f:
        f.write(line)


for element in elements:
    links = element.find('p').find_all('a')
    for index, link in enumerate(links):
        if index == 0:
            print('{} : {}'.format(link.text, link.get('href')))
            write_to_file('{} : {}\n'.format(link.text, link.get('href')))
        if index == 1:
            print('{} : {}'.format(link.text, link.get('href')))
            write_to_file('{} : {}\n'.format(link.text, link.get('href')))
        if index == 2:
            print('{} : {}'.format(link.text, link.get('href')))
            write_to_file('{} : {}\n'.format(link.text, link.get('href')))
        if index == 3:
            print('{} : {}'.format(link.text, link.get('href')))
            write_to_file('{} : {}\n'.format(link.text, link.get('href')))
        if index == 4:
            print('{} : {}'.format(link.text, link.get('href')))
            write_to_file('{} : {}\n\n'.format(link.text, link.get('href')))
            print('\n')


