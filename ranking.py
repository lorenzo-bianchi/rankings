import requests
import pandas as pd
import re

url = 'http://1x2stats.com/it/ITA/Serie-B/classifica-casa-trasferta/'
dfs = pd.read_html(url)
series = re.findall("Serie-(.)",url)
series = series[0]

home = dfs[0]
away = dfs[1]

d_home = {}
for index, row in home.iterrows():
    d_home[row['Squadra']] = {'tx' : row['G'], 'tzx' : 19-row['G'], 'Punti' : row['Punti'], 'mpc' : float(row['Punti'])/float(row['G'])}
    
d_away = {}
for index, row in away.iterrows():
    d_away[row['Squadra']]  = {'tx' : row['G'], 'tzx' : 19-row['G'], 'Punti' : row['Punti'], 'mpf' : float(row['Punti'])/float(row['G'])}
    d_tot = {}
    
for team in d_home.keys():
    P = d_home[team]['Punti'] + d_away[team]['Punti']
    mpc = d_home[team]['mpc']
    mpf = d_away[team]['mpf']
    c = d_home[team]['tzx']
    f = d_away[team]['tzx']
    d_tot[team] = P + mpc*c + mpf*f
    
rank = sorted(d_tot.items(), key=lambda kv: kv[1], reverse=True)

rk = 1
print(f"Classifica Serie {series}\n")
for team in rank:
    if len(team[0]) > 10:
        if rk < 10:
            print(f" {rk}) {team[0]} \t {team[1]:.4f}")
        else:
            print(f"{rk}) {team[0]} \t {team[1]:.4f}")
    else:
        if rk < 10:
            print(f" {rk}) {team[0]} \t\t {team[1]:.4f}")
        else:
            print(f"{rk}) {team[0]} \t\t {team[1]:.4f}")
    rk += 1
