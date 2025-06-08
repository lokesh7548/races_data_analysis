import pandas as pd

import seaborn as sns

import os

df = pd.read_csv("/home/lokesh/Downloads/archive/TWO_CENTURIES_OF_UM_RACES.csv")

#cleaning up data 
#We only want USA Races, 50km or 50mi, 2018 

#step 1 show only 50k and 50mi races done in 2018 and remove event name

df_50 = df[(df['Event distance/length'].isin(['50km','50mi']))   &   (df['Year of event'] == 2018) & (df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0) == 'USA') ]

df_50['Event name'] = df_50['Event name'].str.split('(').str.get(0)


#cleaning up athelete age

df_50['athlete_age'] = 2018 - df_50['Athlete year of birth']


#remove h from athelete performance

df_50['Athlete performance'] = df_50['Athlete performance'].str.split(' ').str.get(0)


#drop columns:  Athlete  club,Athlete country, athlete year of birth,athlete age category

df_50 = df_50.drop(['Athlete club','Athlete country','Athlete year of birth', 'Athlete age category'], axis = 1)


#cleaning up null values

df_50 = df_50.dropna()


#reset index

df_50.reset_index(drop = True)


#fix data types
df_50['athlete_age'] = df_50['athlete_age'].astype(int)
df_50['Athlete average speed'] = df_50['Athlete average speed'].astype(float)


#rename columns

df_50 = df_50.rename(columns = {'Year of event': 'year' ,
                                'Event dates': 'race_day',
                                'Event name': 'race_name',
                                'Event distance/length': 'race_length',
                                'Event number of finishers': 'race_number_of_finishers',
                                'Athlete performance': 'athlete_performance',
                                'Athlete gender': 'athlete_gender',
                                'Athlete average speed': 'athlete_average_speed',
                                'Athlete ID':'athlete_id'
                               })


#reorder columns

df_51 = df_50[['race_day', 'race_name', 'race_length', 'race_number_of_finishers', 'athlete_id', 'athlete_gender', 'athlete_performance', 'athlete_average_speed', 'year']]


#export

# Get desktop path (works on Windows/Mac/Linux)
desktop = os.path.join(os.path.expanduser('~'), 'Desktop')


#Visualization of cleanded data

#charts and graphs
sns.histplot(df_51, x = 'race_length', hue = 'athlete_gender',) 

sns.displot(df_51[df_51['race_length'] == '50mi']['athlete_average_speed'])   


#questions in data i want to find out
#Difference in speed for the 50km,50mi male to female

df_51.groupby(['race_length','athlete_gender'])['athlete_average_speed'].mean()

