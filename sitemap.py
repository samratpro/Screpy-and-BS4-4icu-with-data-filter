from bs4 import BeautifulSoup as bs
from requests import get
url= "https://www.4icu.org/reviews/4950.htm"
res = get(url)
html = bs(res.text, "html.parser")

trs = html.findAll("tr")


def idicts(list):
    for a in list:
        if a in dicts.key():
            return dicts[a]
dicts={}
for trs_2 in trs:
    trs_str = str(trs_2).replace("<th", "<td").replace("</th>", "</td>").replace("<th>","<td>").replace("<strong>", "").replace(
        "</strong>", "").strip().encode("utf-8").decode()
    trs_soup = bs(trs_str, "html.parser")
    trs_td = trs_soup.findAll("td")
    if len(trs_td) == 2:
        first_ele = trs_td[0].text
        second_ele = trs_td[1].text
        dicts[first_ele]=second_ele

    trs_td_str = str(trs_td)
    if "Screenshot" in trs_td[0]:
        trs_td_str_soup = bs(trs_td_str, "html.parser")
        screenshort_image = trs_td_str_soup.find("img")["src"]


name = ["amar name", "tomar name", "dimer name"]

def mydicts(list):
    for x in list:
        if x in another_dicts.keys():
            return another_dicts[x]

another_dicts={"baler din":"nothing", "okey":"hba", "amar name":"samrat"}

second_dict={}
second_dict["amar nam holo"]=mydicts(name)

subject_soup = html.findAll("div",{"class":"panel-body"})[-9].find("td").findAll("p")[1].text.replace("   "," | ").strip().replace("Faculty of","Department of")

social_soup = html.findAll("div",{"class":"panel-body"})[-8]
facebook = social_soup.findAll("p")[4].findAll("a")[0]["href"]

wiki = html.findAll("div",{"class":"panel-body"})[-6].find("a")["href"]

#print(subject_soup)

country = html.find("ol",{"class":"breadcrumb"}).findAll("li")[2].text
print(facebook)