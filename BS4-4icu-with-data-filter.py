import requests
from bs4 import BeautifulSoup as bs

#Reading Urls from Text
with open("allurl.txt") as file:
    file.readline()
    urls=[x.strip() for x in file]

for url in urls:
  print(url)
  #Filtering Data
  country_rank =["country rank"]
  world_rank =["world rank"]

  #Data Filtering Function
  def filter_dict(list):
      for x in list:
          if x in td_dicts.keys():
              return td_dicts[x]

  final_dicts = {}
  td_dicts={} # Random All Data Adding Dicts
  response = requests.get(url)
  soup = bs(response.text, 'html.parser')
  trs = soup.find_all('tr')
  for trs_2 in trs:
      trs_str = str(trs_2).replace("<th", "<td").replace("</th>", "</td>").replace("<th>", "<td>").replace("<strong>", "").replace("</strong>", "").strip()
      trs_soup = bs(trs_str, "html.parser")
      trs_td = trs_soup.findAll("td")
      if len(trs_td)==2:
          first_td = trs_td[0].text.strip().encode("utf-8").decode()
          second_td = trs_td[1].text.strip().encode("utf-8").decode()
          td_dicts[first_td] = second_td

      trs_td_str = str(trs_td)
      if "Screenshot" in trs_td[0]:
          trs_td_str_soup = bs(trs_td_str, "html.parser")
          screenshort_image = trs_td_str_soup.find("img")["src"]


  final_dicts["country_rank"] = filter_dict(country_rank)
  final_dicts["world_rank"] = filter_dict(world_rank)
  final_dicts["url"] = url

  print(final_dicts)
