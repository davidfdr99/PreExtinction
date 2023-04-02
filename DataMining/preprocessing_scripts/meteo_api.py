import csv
import requests
import statistics
import os
from tqdm import tqdm


def api_meteo():
    for species in tqdm(iterable=os.listdir('data/process_data'), desc='meteo'):  # change subset_all to all
        with open(f'data/process_data/{species}', 'r') as file:
            content_species = []
            content = file.readlines()
            for line in content:
                cols = line.strip('\n').split('\t')
                content_species.append(cols)
        content_species_meteo = []
        for line in content_species:
            # print(line)
            temp2max = ''
            temp2min = ''
            temp2mean = ''
            precipit_summean = ''
            latitude = line[5]
            longitude = line[6]
            start_date_annee = line[9]
            if latitude != '' and longitude != '' and start_date_annee != '' :
                URL = 'https://archive-api.open-meteo.com/v1/archive?latitude='+ latitude +'&longitude='+ longitude + '&start_date='+ start_date_annee +'-01-01&end_date='+ start_date_annee +'-12-31&daily=temperature_2m_max,temperature_2m_min,temperature_2m_mean,precipitation_sum&timezone=Europe%2FLondon&temperature_unit=celsius'
                with requests.Session() as s:
                    download = s.get(URL)
                    req = download.json()
                    try:
                        daily_temp2max = req['daily']['temperature_2m_max']
                        daily_temp2min = req['daily']['temperature_2m_min']
                        daily_temp2mean = req['daily']['temperature_2m_mean']
                        daily_precipit_sum = req['daily']['precipitation_sum']
                        temp2max = max(daily_temp2max) #max des températures max journalières
                        temp2min = min(daily_temp2min) #min des températures min journalières
                        temp2mean = statistics.mean(daily_temp2mean) #moyenne des températures moyennes journalières
                        precipit_summean = statistics.mean(daily_precipit_sum) #moyenne des précipitations journalières
                    except:
                        temp2max = ''
                        temp2min = ''
                        temp2mean = ''
                        precipit_summean = ''
            #print(species, float(latitude), float(longitude), int(start_date_annee), temp2max,temp2min,temp2mean,precipit_summean)
            final_line = line + [temp2max,temp2min,temp2mean,precipit_summean]
            content_species_meteo.append(final_line)
        #print(content_species_meteo)
            # parameters
            for species in tqdm(iterable=os.listdir('data/process_data'), desc='meteo'):  # change subset_all to all
                all_year = []
                final_list = []
                with open(f'data/process_data/{species}', 'r') as file:
                    content_species = []
                    content = file.readlines()
                    for line in content:
                        cols = line.strip('\n').split('\t')
                        content_species.append(cols)
                content_species_meteo = []
                for line in content_species:
                    # print(line)
                    temp2max = ''
                    temp2min = ''
                    temp2mean = ''
                    precipit_summean = ''
                    latitude = line[5]
                    longitude = line[6]
                    start_date_annee = line[9]
                    if latitude != '' and longitude != '' and start_date_annee != '':
                        URL = 'https://archive-api.open-meteo.com/v1/archive?latitude=' + latitude + '&longitude=' + longitude + '&start_date=' + start_date_annee + '-01-01&end_date=' + start_date_annee + '-12-31&daily=temperature_2m_max,temperature_2m_min,temperature_2m_mean,precipitation_sum&timezone=Europe%2FLondon&temperature_unit=celsius'
                        with requests.Session() as s:
                            download = s.get(URL)
                            req = download.json()
                            try:
                                daily_temp2max = req['daily']['temperature_2m_max']
                                daily_temp2min = req['daily']['temperature_2m_min']
                                daily_temp2mean = req['daily']['temperature_2m_mean']
                                daily_precipit_sum = req['daily']['precipitation_sum']
                                temp2max = max(daily_temp2max)  # max des températures max journalières
                                temp2min = min(daily_temp2min)  # min des températures min journalières
                                temp2mean = statistics.mean(
                                    daily_temp2mean)  # moyenne des températures moyennes journalières
                                precipit_summean = statistics.mean(
                                    daily_precipit_sum)  # moyenne des précipitations journalières
                            except:
                                temp2max = ''
                                temp2min = ''
                                temp2mean = ''
                                precipit_summean = ''
                    # print(species, float(latitude), float(longitude), int(start_date_annee), temp2max,temp2min,temp2mean,precipit_summean)
                    final_line = line + [temp2max, temp2min, temp2mean, precipit_summean]
                    content_species_meteo.append(final_line)
                # print(content_species_meteo)
                with open(f'data/process_data_meteo/{species}', 'w', newline='') as file:
                    content = csv.writer(file, delimiter='\t')
                    content.writerows(content_species_meteo)
        with open(f'data/process_data_meteo/{species}', 'w', newline='') as file:
            content = csv.writer(file, delimiter='\t')
            content.writerows(content_species_meteo)
    

if __name__ == '__main__':
    print('start')
    api_meteo()
    print('end')






