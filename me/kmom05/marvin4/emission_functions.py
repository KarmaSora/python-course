""" emission functions"""
#import emission_data_small as emdata_small
import emission_data as emdata_small

#def country_data_search(country_name):
def search_country(search_word):
    """
    searches for country data in database
    parameter:
    country_name (string): string to use when searching
    return: list with countries containing searchdata
    """
    countrieslist = emdata_small.country_data
    found_list = []
    for country in countrieslist:
        if search_word.lower() in country.lower():
            #print(country)
            found_list.append(country)
    if len(found_list) ==0:
        raise ValueError("Country does not exist!")
        
    return found_list
#print(emdata_small.country_data['Azerbaijan'])
#print(emdata_small.country_data['Azerbaijan']["id"])

def co2emmision(data):
    """splits users input and prints it out after deviding it"""
    search_data = data.split(",")
    #return country+":"+str(rounded_precentage) + "%"
    if len(search_data) ==3:
        country,year1,year2 = search_data[0],search_data[1],search_data[2]
        result= get_country_change_for_years(country,year1,year2)

    elif len(search_data)==2: 
        #country, year1 == search_data[0],search_data[1]
        result= get_country_year_data_megaton(search_data[0], search_data[1])
    else: 
        print("error, not enough input")

    return search_data[0]+":"+str(result)+"%"

def get_country_year_data_megaton(country, year):
    """
    finds and returns country emmision from selected year
    takes three inputs and process data returning rounded precentage of country emmision between selected years
    paramter:
        country: full name of country, (letter sensitive)
        year: first year
        return: precent for selected year

    """
    year = int(year)   
    country_id = emdata_small.country_data[country]["id"]
    emmision_rate= 0
    if year == 1990:
        for country_num, emmi in enumerate(emdata_small.emission_1990.values()):
            if country_id == country_num:
                emmision_rate += emmi
                #print("called get country function, 1990 working?")


    elif year == 2005:
        for country_num, emmi in enumerate(emdata_small.emission_2005.values()):
            if country_id == country_num:
                emmision_rate += emmi
                #print("called get country function, 2005 working?")


    elif year == 2017:
        for country_num, emmi in enumerate(emdata_small.emission_2017.values()):
            if country_id == country_num:
                emmision_rate += emmi
                #print("called get country function, 2017 working?")

    else: 
        raise ValueError("year not in data range")
        
    return emmision_rate * 1000000

#print(get_country_year_data_megaton("Sweden", 1990))

def get_country_change_for_years(country, year1, year2):
    """
    takes three inputs and process data returning rounded precentage of country emmision between selected years
    paramter:
        country: full name of country, (letter sensitive)
        year1: first year
        year2: sec year 
        return: emmision change precentage
    """
    year1 = int(year1)
    year2 = int(year2)
    if  year1 in [1990, 2005, 2017]:
        #print("first year found!")
        if year2 in [1990, 2005, 2017]:
            #print("sec year found!")
            first=get_country_year_data_megaton(country, year1)
            sec=get_country_year_data_megaton(country, year2)
            change_precent = sec/first
        else: 
            raise ValueError("Wrong year!"+ str(year2)+ "doesnt exist")
    else: 
        raise ValueError("Wrong year!"+ str(year1)+ "doesnt exist")
    
    change_precent -=1
    change_precent *=100
    rounded_precentage = round(change_precent,2)
    return rounded_precentage


#__3---3-3-3--3-3-3-3-qklmekmldaskmdasklmdmaldmasmdasmldmaskmdasmdasmdlkasmdklasmdmaslkdmasklmdHERE
def get_country_data(country_name):
    """
    ahhhhhhhhhhhh
    """
    new_dict = {"name": country_name }
    country_info = emdata_small.country_data
    unknown = 0
    """
    print("")   
    print(country_info[country_name]) 
    print("")
    """
    #popcounter =len(country_info[country_name]["population"])
    pop = country_info[country_name]["population"]

    if pop == []:
        unknown = None
    valid_years= [1990,2005,2017]

    for year in valid_years:
        if unknown is None:
            emmi = get_country_year_data_megaton(country_name, year)
            new_dict[year] = {"emission":emmi, "population": unknown }
        else: 
            unknown = pop[valid_years.index(year)]
            emmi = get_country_year_data_megaton(country_name, year)
            new_dict[year] = {"emission":emmi, "population": unknown }

    first_diff = get_country_change_for_years(country_name, 1990, 2005)
    sec_diff = get_country_change_for_years(country_name, 2005, 2017)    
    new_dict["emission_change"] = (first_diff, sec_diff)

    #print(new_dict)
    return new_dict


def print_country_data(data):
    """
    baahhhahashhidashdikjsajdanhsdjdjkaskjödöjkasafnöoefsijöoafkl
    """
    country_name = data["name"]
    data1990 = data[1990]
    emmi= data1990["emission"]
    firstpop = data[1990]["population"]
    secpop = data[2005]["population"]
    thirdpop = data[2017]["population"]

    if firstpop is None:
        firstpop ="Missing population data!"
    if secpop is None:
        secpop = "Missing population data!"
    if thirdpop is None:
        thirdpop="Missing population data!"

    first_change= data["emission_change"][0]
    sec_change= data["emission_change"][1]

    print(country_name)
    print("Emission: 1990: "+str(emmi)+"  2005: "+str(data[2005]["emission"]) +"  2017: " + str(data[2017]["emission"]))
    print("Emission change   -   1990-2005: "+ str(first_change) +"%         2005-2017: "+ str(sec_change)+"%" )
    print("Population        - 1990: "+str(firstpop)+"       2005: "+str(secpop)+"   2017: "+str(thirdpop))

if __name__ == "__main__":
    #print(emdata_small.emission_1990.values())
    #get_country_year_data_megaton("kae",3)
    #print(get_country_change_for_years("Sweden",1990,2017))
    #print(get_country_change_for_years('China', 1990, 2017))
    #print_country_data(get_country_data("Sweden"))
    #print("--------")
    print("----HelloThere! If read this, you made it this far. congrats!----")

    #get_country_data("Greenland")
