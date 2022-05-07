import scrapy
from ..items import IcuItem
from bs4 import BeautifulSoup as bs

with open("allurl.txt") as file:
    file.readline()
    urls=[x.strip() for x in file]

#To Scrap Unique Data.........
country_rank =["country rank"]
world_rank =["world rank"]
name=["Name"]
Acronym =["Acronym"]
Founded =["Founded"]
Motto =["Motto"]
Address =["Address"]
Tel =["Tel"]
Fax=["Fax"]
Local_students=["Local students"]
International_students=["International students"]
Gender=["Gender"]
International_Students_admission=["International Students"]
Selection_Type=["Selection Type"]
Admission_Rate=["Admission Rate"]
Admission_Office=["Admission Office"]
Student_Enrollment=["Student Enrollment"]
Academic_Staff=["Academic Staff"]
Control_Type=["Control Type"]
Entity_Type=["Entity Type"]
Academic_Calendar=["Academic Calendar"]
Campus_Setting=["Campus Setting"]
Religious_Affiliation=["Religious Affiliation"]
Library=["Library"]
Housing=["Housing"]
Sport_Facilities=["Sport Facilities"]
Financial_Aids=["Financial Aids"]
Study_Abroad=["Study Abroad"]
Distance_Learning=["Distance Learning"]
Academic_Counseling=["Academic Counseling"]
Career_Services=["Career Services"]
Institutional_Hospital=["Institutional Hospital"]
other_locations=["Other locations"]



class IcubotSpider(scrapy.Spider):
    name = 'icubot'
    start_urls = urls

    def parse(self, response):
        items = IcuItem()

        def filter_dict(list):
            for x in list:
                if x in td_dicts.keys():
                    return td_dicts[x]

        td_dicts={}
        trs=response.css("tr").getall()
        for trs_2 in trs:
            trs_html = bs(trs_2, "html.parser")
            trs_str = str(trs_html).replace("<th", "<td").replace("</th>", "</td>").replace("<th>", "<td>").replace(
                "<strong>", "").replace(
                "</strong>", "").strip()
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


        html_css = response.css("div.panel-body").getall()[-9]
        html_soup = bs(html_css, "html.parser")
        subject = html_soup.find("td").findAll("p")[1].text.replace("   "," | ").strip().replace("Faculty of", "Department of")


        wiki_css = response.css("div.panel-body").getall()[-6]
        wiki_soup = bs(wiki_css, "html.parser")
        wiki = wiki_soup.find("a")["href"]

        social_css = response.css("div.panel-body").getall()[-8]
        social_soup = bs(social_css, "html.parser")
        facebook = social_soup.findAll("p")[0].findAll("a")[1]["href"]
        twitter = social_soup.findAll("p")[1].findAll("a")[1]["href"]
        linkedin = social_soup.findAll("p")[2].findAll("a")[0]["href"]
        youtube = social_soup.findAll("p")[3].findAll("a")[1]["href"]
        instagram = social_soup.findAll("p")[4].findAll("a")[0]["href"]



        country = response.css("ol.breadcrumb").get()
        country_html = bs(country, "html.parser")
        country_name = country_html.findAll("li")[2].text

        url = response.url
        university_name= response.css("h1::text").get()

        items["country_name"] = country_name
        items["university_name"] = university_name
        items["url"] = url
        items["country_rank"] = filter_dict(country_rank)
        items["world_rank"] = filter_dict(world_rank)
        items["name"] = filter_dict(name)
        items["name_t"] = filter_dict(name)
        items["name_t_t"] = filter_dict(name)
        items["Acronym"] = filter_dict(Acronym)
        items["Founded"] = filter_dict(Founded)
        items["Motto"] = filter_dict(Motto)
        items["Address"] = filter_dict(Address)
        items["Tel"] = filter_dict(Tel)
        items["Fax"] = filter_dict(Fax)
        items["Local_students"] = filter_dict(Local_students)
        items["International_students"] = filter_dict(International_students)
        items["Selection_Type"] = filter_dict(Selection_Type)
        items["Admission_Rate"] = filter_dict(Admission_Rate)
        items["Admission_Office"] = filter_dict(Admission_Office)
        items["Student_Enrollment"] = filter_dict(Student_Enrollment)
        items["Academic_Staff"] = filter_dict(Academic_Staff)
        items["Control_Type"] = filter_dict(Control_Type)
        items["Entity_Type"] = filter_dict(Entity_Type)
        items["Academic_Calendar"] = filter_dict(Academic_Calendar)
        items["Campus_Setting"] = filter_dict(Campus_Setting)
        items["Religious_Affiliation"] = filter_dict(Religious_Affiliation)
        items["Library"] = filter_dict(Library)
        items["Housing"] = filter_dict(Housing)
        items["Sport_Facilities"] = filter_dict(Sport_Facilities)
        items["Financial_Aids"] = filter_dict(Financial_Aids)
        items["Study_Abroad"] = filter_dict(Study_Abroad)
        items["Distance_Learning"] = filter_dict(Distance_Learning)
        items["Academic_Counseling"] = filter_dict(Academic_Counseling)
        items["Career_Services"] = filter_dict(Career_Services)
        items["Institutional_Hospital"] = filter_dict(Institutional_Hospital)
        items["other_locations"] = filter_dict(other_locations)
        items["flag_img"] = "https://www.4icu.org/"+str(response.css("img::attr(src)").getall()[2])
        items["uni_logo"] = "https://www.4icu.org/"+str(response.css("img::attr(src)").getall()[3])
        items["screenshort"] = "https://www.4icu.org/"+str(screenshort_image)
        items["subject"] = subject
        items["wiki"] = wiki
        items["facebook"] = facebook
        items["twitter"] = twitter
        items["linkedin"] = linkedin
        items["youtube"] = youtube
        items["instagram"] = instagram
        yield items
