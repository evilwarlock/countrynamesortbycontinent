import pycountry as pc
import pycountry_convert as pcc
import re

def sortbyContinent(input_country_names):
    """This is to sort the county names by continent"""
    input_country_names_list = re.split("[, ]+", input_country_names)

    print(input_country_names_list)
    
    continents = {'NA': 'North America', 'SA': 'South America', 'AS': 'Asia', 'OC': 'Australia', 'AF': 'Africa', 'EU': 'Europe'}

    for cont in continents:
        print(continents[cont])
        print('===============')
        output_countries = []
        for country_name in input_country_names_list:
            country_alpha2 = pcc.country_name_to_country_alpha2(country_name)
            country_continent_code = pcc.country_alpha2_to_continent_code(country_alpha2)
            country_continent_name = pcc.convert_continent_code_to_continent_name(country_continent_code)
            
            if country_continent_name == continents[cont]:
                output_countries.append(country_name)
            # return country_continent_name
            # for country in pc.countries:
            #     # print(type(country))
            #     continent_name = pc.country_alpha2_to_continent_code(country.alpha_2)
            #     print(continent_name)
            #     # contname = pcc.convert_country_alpha2_to_continent_code.country_alpha2_to_continent_code(country.alpha_2)
            #     if cont == contname and cname.lower() == country.name.lower():
            #         # print(country.name)
            #         try:
            #             # output_countries.append([continents[pcc.convert_country_alpha2_to_continent_code.country_alpha2_to_continent_code(c.alpha_2)], country.name])
            #             output_countries.append(country.name)
            #         except:
            #             continue
        if output_countries:
            for cname in sorted(output_countries):
                print(cname)
                print('\n')
        else:
            print('\n')
            
test = 'Nigeria, Canada,Japan'
sortbyContinent(test)