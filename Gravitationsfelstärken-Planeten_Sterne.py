import os,sys
import decimal
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime 

daten = {}
t = datetime.now()

def uhrzeit():
    return ("%s:%s:%s"%(t.hour,t.minute,t.second))

def datum():
    return ("%s.%s.%s"%(t.day,t.month,t.year))
        
def sp(msg):
    sys.stdout.write("\r INFO: %s"%(msg))
    sys.stdout.flush()

def get_data(daten_dateiname):
    file = open(daten_dateiname,"r")
    Lines = file.readlines()
    file.close()
    daten['Radien'] = []
    daten['Massen'] = []
    daten['Namen'] = []
    for line in Lines:
        zeile = line.strip()
        if (zeile != "" and zeile != " " and "$NOT$" not in zeile):
            planeten_sterne_args = zeile.split(':')
            planeten_sterne_name = planeten_sterne_args[0]
            planeten_sterne = planeten_sterne_args[1]
            masse_radius_args = planeten_sterne.split(',')
            masse_args = masse_radius_args[0]
            radius_args = masse_radius_args[1]
            masse_argumente_ = masse_args.split('=')
            radius_argumente_ = radius_args.split('=')
            masse = masse_argumente_[1]
            __radius = radius_argumente_[1]
            RADIUS_ARG = __radius.split('}') 
            radius = RADIUS_ARG[0]
            name = planeten_sterne_name
            daten['Massen'].append(masse)
            daten['Radien'].append(radius)
            daten['Namen'].append(name)

def berechnen():
    daten['Gravitationsfeldstärken'] = [] 
    for i in range(0,len(daten['Massen'])):
        masse = daten['Massen'][i]
        radius = daten['Radien'][i]
        G = 6.674079999999999e-11
        m = float(format(float(masse), '.77f')) #Einheit: kg
        r = float(format(float(radius), '.77f')) #Einheit: m
        y = float(format(float(G), '.77f')) #Gravitationsfeldkonstante (G)
        g = ( y * ( (m) / ((r*10**3)**2) ) )
        g = float(format(float(g), '.77f')) #Einheit: m/s^2
        daten['Gravitationsfeldstärken'].append(g)
    daten['anzahl'] = []
    max_len = len(daten['Massen'])
    max_len += 1
    for i in range(1, max_len):
        daten['anzahl'].append(i)
    #print("ABGESCHLOSSEN\n\n")
    #print("Masse:%s, Radius: %s\n\n"%(m,r))

if __name__ == '__main__':
    x = os.system("cls") #Windows -default
    sp("Daten werden berechnet..")
    get_data('daten.00175')
    try:
        berechnen()
        print("ABGESCHLOSSEN")
        sp("Daten werden angezeigt..")
        try:
            pd.set_option('max_columns', 7)
            data_frame = pd.DataFrame(daten,
                              columns=["Namen","Gravitationsfeldstärken","Massen","Radien"],
                              index=daten['anzahl'])
            print("ABGESCHLOSSEN")
            print(data_frame)
            sp("Berechnete Daten werden gespeichert..")
            dateiname = "berechnete_daten_save_00175.csv"
            try:
                data_frame.to_csv(dateiname)
                print("GESPEICHERT")
            except Exception as e:
                print("FEHLGESCHLAGEN!")
            print(" INFO: CSV-Datei: %s"%(dateiname))
        except Exception as e:
            print("FEHLGESCHLAGEN!")
    except:
        print("FEHLGESCHLAGEN")
    input("")
    


