import pandas as pd

# read TopUni and capitals file
university = pd.read_csv('TopUni.csv')
capital = pd.read_csv('capitals.csv')


# use the function to counter the universities
def universitiesCount(university):
    return 'Total number of universities => ' + str(len(university))


# ouput the countries
def availableCountries(university):
    capital = pd.read_csv('capitals.csv')
    countryName = capital.iloc[:, 0]

    return 'Available countries => ' + ', '.join(countryName).upper()


# use function to count the available countries and available continents
def uniCount(university):
    capital['Country Name'] = capital['Country Name'].str.upper()
    capital['Capital'] = capital['Capital'].str.upper()
    # display(capital)

    # duplicate the continent that repeating
    continents = capital.drop_duplicates(['Continent'])
    continent = continents.iloc[:, 5]
    returnstring = 'Available continents => ' + str(continent).upper()
    #print(returnstring)
    return returnstring


# use the function to output the international rank and the university name
def universityInternationalRank(country):
    df2 = university[university['Country'] == country.upper()]
    # display(df2)
    # determine the row of world rank in country
    ind = df2["World Rank"].idxmin()
    #print(ind)
    universityName = df2.loc[ind][1]
    rank = df2.loc[ind][0]
    returnstring = "At international rank => " + str(rank) + ' the university name is => ' + str(universityName).upper()
    return returnstring


# universityInternationalRank('canada')


# use funtion to output the national rank and the university name
def universityNationalRank(country):
    university['Country'] = university['Country'].str.upper()
    df3 = university[university['Country'] == country.upper()]
    # display(df3)
    # determine the row of national rank in country
    ind = df3["National Rank"].idxmin()
    #print(ind)
    universityName = df3.loc[ind][1]
    rank = df3.loc[ind][3]
    returnstring = "At national rank => " + str(rank) + ' the university name is => ' + str(universityName).upper()
    return returnstring


# universityNationalRank('japan')


# use function to output the average score
def avgScore(country):
    df4 = university[university['Country'] == country.upper()]
    # calculate the mean of the score
    averageMean = df4["Score"].mean()
    # print 2 decimal places
    average = round(averageMean, 2)
    #print(returnstring)
    return average


# avgScore("USA")



# use the function to output the relative score
def relativeScore(country):
    average = avgScore(country)
    df6 = capital[capital["Country Name"] == country.upper()]
    continent = df6['Continent'].values
    df7 = capital[capital["Continent"] == continent[0]]
    allCountries = list(df7["Country Name"].values)
    df8 = university[university['Country'].isin(allCountries)]
    # determine the highest one
    highestMark = df8["Score"].max()
    # display(df8)
    #print 2 decimal places
    average = round(average, 2)
    highestMark = round(highestMark, 2)
    relaScore = round(average, 2) / round(highestMark, 2) * 100
    continentName = ", ".join(str(i) for i in continent)
    returnstring = 'The relative score to the top university in ' + str(continentName) + ' is => ' \
                   + str(average) + '/' + str(highestMark) + ' x 100% = ' + str(round(relaScore, 2)) + "% \n"
    return returnstring


# relativeScore("USA")

# relativeScore("USA")

# use the function to output the capital city
def capitalCity(country):
    df10 = capital[capital["Country Name"] == country.upper()]
    cap = df10['Capital'].values
    cap = str(cap[0]).upper()
    returnstring = 'The capital is => ' + cap
    #print(returnstring)
    return cap


# capitalCity("Canada")

# use the function to output the universities that hold the capital name
def holdCapitalCity(country):
    city = capitalCity(country)
    df9 = capital[capital["Capital"] == city.upper()]
    # display(df9)
    country = df9['Country Name'].values
    df10 = university[university['Country'].isin(country)]
    # display(df10)
    institutionList = df10['Institution name'].tolist()
    returnString = ''
    counter = 1
    for i in range(len(institutionList)):
        if city.upper() in institutionList[i].upper():
            returnString += f'    #{counter} ' + institutionList[i].upper() + '\n'
            counter += 1
    return returnString


# holdCapitalCity('Canada')

# main function output everything to output.txt
def getInformation(selectedCountry, rankingFileName, capitalsFileName):
    university = pd.read_csv(rankingFileName)
    university['Country'] = university['Country'].str.upper()
    capital = pd.read_csv(capitalsFileName)
    capital['Country Name'] = capital['Country Name'].str.upper()
    capital['Capital'] = capital['Capital'].str.upper()
    country = selectedCountry.lower()

    with open('output.txt', 'w') as f:
        f.write(universitiesCount(university))
        f.write(availableCountries(university))
        f.write(str(uniCount(university)))
        f.write(universityInternationalRank(country))
        f.write(universityNationalRank(country))
        f.write("The average score => " + str(avgScore(country)) + "%")
        f.write(relativeScore(country))
        f.write('The capital is =>' + capitalCity(country))
        f.write('The universities that contain the capital name => \n' + holdCapitalCity(country))


# recall the function
getInformation("USA", 'TopUni.csv', 'capitals.csv')
