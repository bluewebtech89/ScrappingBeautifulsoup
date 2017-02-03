import requests
from bs4 import BeautifulSoup
import time

url_to_scrape = 'http://apps2.polkcountyiowa.gov/inmatesontheweb/'
 
r = requests.get(url_to_scrape)

soup =  BeautifulSoup(r.text, "lxml")

inmates_links = []
 
for table_row in soup.select(".inmatesList tr"):
	table_cells = table_row.findAll('td')

	if len(table_cells) > 0:
		relative_link_to_inmate_details = table_cells[0].find('a')['href']
		absolute_link_to_inmate_details = url_to_scrape + relative_link_to_inmate_details
		inmates_links.append(absolute_link_to_inmate_details)

inmates = []
 
for inmate_link in inmates_links[:10]:
    r = requests.get(inmate_link)
    soup = BeautifulSoup(r.text, "lxml")
	
    inmate_details = {}
	
    inmate_profile_rows = soup.select("#inmateProfile tr")
    inmate_details['age'] = inmate_profile_rows[0].findAll('td')[0].text.strip()
    inmate_details['race'] =  inmate_profile_rows[3].findAll('td')[0].text.strip()
	
    inmate_details['sex'] =  inmate_profile_rows[4].findAll('td')[0].text.strip()
    inmate_name_date_rows = soup.select("#inmateNameDate tr")
	
    inmate_details['name'] =  inmate_name_date_rows[1].findAll('td')[0].text.strip()
    inmate_details['booked_at'] = inmate_name_date_rows[2].findAll('td')[0].text.strip()
    inmate_address_container = soup.select("#inmateAddress")
	
    inmate_details['city'] =  inmate_address_container[0].text.split('\n')[2].strip()
	
    inmates.append(inmate_details)
	
    time.sleep(1)


inmate_cities =  {}
 
for inmate in inmates:
    if inmate['city'] in inmate_cities:	
        inmate_cities[inmate['city']] += 1
    else:
        inmate_cities[inmate['city']] = 1
 
print inmate_cities

inmate_races =  {}
 
for inmate in inmates:
    if inmate['race'] in inmate_races:
        inmate_races[inmate['race']] += 1
    else:
        inmate_races[inmate['race']] = 1
        
print inmate_races
