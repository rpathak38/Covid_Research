import pandas as pd
import requests
import io

popurl = "https://raw.githubusercontent.com/Ali-Kazmi/covid-visualizations/master/mega-population%20by%20age%20(2).xlsx"
deathurl = "https://raw.githubusercontent.com/Ali-Kazmi/covid-visualizations/master/mega-deaths%20by%20age.xlsx"

#download = github_session.get(url).content
# Reading the downloaded content and turning it into a pandas dataframe
PopDF = pd.read_excel(popurl,index_col=0)
DeathsDF = pd.read_excel(deathurl,index_col=0)
print(PopDF)
# Printing out the first 5 rows of the dataframe
#note: 10-19 should have been the second column, but it shows it as a date because excel did something.. oops
print(list(((DeathsDF["50-59"]/PopDF["50-59"])/(DeathsDF["40-49"]/PopDF["40-49"]))))

