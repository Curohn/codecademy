# Starter info included for project:
# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325, 51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]


# write your update damages function here:
# function converts damages in mixed int/text format to float format by using conversion dict
def convert_damages(damages):
    # use below conversion dict to multiply the formatted values in damages list
    conversion = {"M": 1000000, "B": 1000000000}
    updated_damages = []
    for amount in damages:
        if amount == 'Damages not recorded':
            updated_damages.append('Damages not recorded')
        elif "M" in amount:
            updated_damages.append(float(amount.strip("M")) * conversion["M"])
        elif "B" in amount:
            updated_damages.append(float(amount.strip("B")) * conversion["B"])
    return updated_damages
    #print(updated_damages)
updated_damages = convert_damages(damages)


# write your construct hurricane dictionary function here:
# fuction constructs dict based on lists of values given
def dict_constructer(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    hurricanes = {}
    for i in range(len(names)):
        hurricanes[names[i]] = {'Name': names[i], 
                                'Month': months[i], 
                                'Year': years[i], 
                                'Max Sustained Wind': max_sustained_winds[i], 
                                'Areas Affected': areas_affected[i], 
                                'Damage': updated_damages[i], 
                                'Deaths': deaths[i]}
    return hurricanes
    #print(hurricanes.items())
hurricanes_by_name = dict_constructer(names, months, years, max_sustained_winds, areas_affected, damages, deaths)


# write your construct hurricane by year dictionary function here:
# function takes in a previously created dict, and reformats it to {year: {name:name, month:month, ...}} format
def hurricanes_by_year_converter(hurricanes_by_name):
    hurricanes_by_year = {}
    for name, month, year, max_sustained_wind, area_affected, damage, death in zip(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
        dict = {year: {"Name": name, "Month": month, "Year": year, "Max Sustained Wind Speed": max_sustained_wind, "Areas Affected": area_affected, "Damages": damage, "Deaths": death}}
        hurricanes_by_year.update(dict)
    return hurricanes_by_year
    #print(hurricanes_by_year_converter(hurricanes_by_name))


# write your count affected areas function here:
# takes in a list, and creates a dict with area and number of times affected {area: count, ...}
areas_count = {}
def areas_affected_counter(areas_affected):
    for record in areas_affected:
        for area in record:
            if area not in areas_count:
                areas_count[area] = 1
            else:
                areas_count[area] += 1
    return areas_count
    #print(areas_affected_counter(areas_affected))


# write your find most affected area function here:
# iterates through new dict of areas and the number of times they've been affected and returns the most impacted area and count 
def most_affected_area(areas_count):
    most_affected_area = ''
    most_affected_count = 0
    for area in areas_count:
        if areas_count[area] > most_affected_count:
            most_affected_area = area
            most_affected_count = areas_count[area]
        else:
            continue
    
    return most_affected_area, most_affected_count
    #print(most_affected_area(areas_count))


# write your greatest number of deaths function here:
def greatest_number_of_deaths(hurricanes_by_name):
    most_deaths_count = 0
    most_deaths_hurricane = ''
    for hurricane in hurricanes_by_name:
        if hurricanes_by_name[hurricane][deaths] > most_deaths_count:
            most_deaths_count = hurricanes_by_name[hurricane]['Deaths']
            most_deaths_hurricane = hurricane
    return most_deaths_count, most_deaths_hurricane
    #print(most_deaths_count, most_deaths_hurricane)


# write your catgeorize by mortality function here:
def categorize_by_mortality(hurricanes_by_name):
    mortality_scale = {0: 0,
                       1: 100,
                       2: 500,
                       3: 1000,
                       4: 10000}
    hurricanes_by_mortality = {0:[], 1:[], 2:[], 3:[], 4:[]}
    for hurricane in hurricanes_by_name:
        num_deaths = hurricanes_by_name[hurricane]['Deaths']
        if num_deaths == mortality_scale[0]:
            hurricanes_by_mortality[0].append(hurricanes_by_name[hurricane])
        elif num_deaths > mortality_scale[0] and num_deaths <= mortality_scale[1]:
            hurricanes_by_mortality[1].append(hurricanes_by_name[hurricane])
        elif num_deaths > mortality_scale[1] and num_deaths <= mortality_scale[2]:
            hurricanes_by_mortality[2].append(hurricanes_by_name[hurricane])
        elif num_deaths > mortality_scale[2] and num_deaths <= mortality_scale[3]:
            hurricanes_by_mortality[2].append(hurricanes_by_name[hurricane])
        elif num_deaths > mortality_scale[3] and num_deaths <= mortality_scale[4]:
            hurricanes_by_mortality[4].append(hurricanes_by_name[hurricane])
    return hurricanes_by_mortality


# write your greatest damage function here:
def greatest_damage(hurricanes_by_name):
    greatest_damage_cane = ""
    greatest_damage_cost = ""
    for hurricane in hurricanes_by_name:
        if hurricanes_by_name[hurricane]['Damage'] == "Damages not recorded":
            continue
        elif hurricanes_by_name[hurricane]['Damage'] > greatest_damage_cost:
            greatest_damage_cane = hurricanes_by_name[hurricane]['Name']
            greatest_damage_cost = hurricanes_by_name[hurricane]['Damage']


# write your catgeorize by damage function here:
def categorize_by_damage(hurricanes_by_name):
    damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
    hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
    for hurricane in hurricanes_by_name:
        damage_cost = hurricanes_by_name[hurricane]['Damage']
        if hurricanes_by_name[hurricane]['Damage'] == "Damages not recorded":
            continue
        elif damage_cost == damage_scale[0]:
            hurricanes_by_damage[0].append(hurricanes_by_name[hurricane])
        elif damage_cost > damage_scale[0] and damage_cost <= damage_scale[1]:
            hurricanes_by_damage[1].append(hurricanes_by_name[hurricane])
        elif damage_cost > damage_scale[1] and damage_cost <= damage_scale[2]:
            hurricanes_by_damage[2].append(hurricanes_by_name[hurricane])
        elif damage_cost > damage_scale[2] and damage_cost <= damage_scale[3]:
            hurricanes_by_damage[2].append(hurricanes_by_name[hurricane])
        elif damage_cost > damage_scale[3] and damage_cost <= damage_scale[4]:
            hurricanes_by_damage[4].append(hurricanes_by_name[hurricane])
    return hurricanes_by_damage
print(categorize_by_damage(hurricanes_by_name))
