# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 16:36:09 2016

@author: Valentin
"""

import numpy as np
import pandas as pd
import pickle


database = pd.DataFrame(columns = ["Wirkstoff","Name","Wirkstoffgehalt","Formulierung","CLP-Verordnung","Anwenderschutz","Gewässerschutz","Bienenschutz","Nutzorganismen","Sonstiges","Zulassungsende","Kultur","Schadorganismus","Anwendungshinweise"])

database.loc[0] = ["Clothianidin","Dantop (025583-00/SPU)","500 g/kg","Wasserdispergierbares Granulat",None,"E0005-1, SB001","NG312, NW263, NW468","NB6611","NN234, NN360, NN370, NN380","VH352-1","31.12.2019","Kartoffel","Blattläuse als Virusvektor","Freiland beim Legen max. Zahl Behandl.: 1, in der Kultur/je Jahr: 1 Pflanzgutbehandlung, spritzen oder sprühen beim Legen, 300 g/ha in 60 bis 100 l Wasser/ha max. Mittelaufwand 0,3 kg/ha (= max. 25 dt Pflanzgut pro ha) Wartezeit: F NW642, WW709, WW720, WW750"]
database.loc[1] = ["Clothianidin","Poncho ungefärbt \(025429-00/BAY\)","600 g/l Clothianidin","Suspensionskonzentrat zur Saatgutbehandlung","Achtung | GHS07, GHS09 | EUH 208-0098, EUH 208-0101, EUH 401, H302, H317, H400, H410, P101, P102, P261, P270, P280, P302+P352, P308+P313, P362+P364, P501","SB001, SB110, SE1201, SF6142, SF6161, SF618, SS1201, SS2203, SS6201","NW263, NW467","NB663","NN400","NH681, NH682, NH6831, NT677, NT679, NT6991, WMI4A","31.12.2017","Futterrübe, Zuckerrübe","Rübenfliege, Moosknopfkäfer, Schnellkäfer -Drahtwurm, Blattläuse","Freiland vor der Saat max. Zahl Behandl.: 1, in der Kultur/je Jahr: 1 pillieren, 100 ml pro Einheit Saatgut max. Mittelaufwand 130 ml/ha (= max. 1,3 Saatgut-Einheiten pro ha) Wartezeit: F"]
database.loc[2] = ["Clothianidin + beta-Cyfluthrin","Janus (025505-00/BAY)","80 g/l beta-Cyfluthrin, 100 g/l Clothianidin","Suspensionskonzentrat zur Saatgutbehandlung","Achtung | GHS07, GHS09 | EUH 208-0101, EUH 208-0111, EUH 401, H302, H332, H400, H410","SB001, SB110, SB193, SE1201, SF613, SF6161, SF618, SF619, SS1201, SS2204, SS6201, ST1202, ST1261, ST1271","NW262, NW264, NW467, NW811","NB663","NN1002, NN3001","NH677, NH679, NH680, NH681, NH682, NH6831, NT694, NT697, NT699, NT6991, NT700, VA265, WMI3A, WMI4A","31.12.2024","Futterrübe, Zuckerrübe","Rübenfliege","Freiland vor der Saat max. Zahl Behandl.: 1, in der Kultur/je Jahr: 1 pillieren, 100 ml pro Einheit Saatgut max. Mittelaufwand 130 ml/ha (= max. 1,3 Saatgut-Einheiten pro ha) Wartezeit: F"]
database.loc[3] = ["Clothianidin + beta-Cyfluthrin","Janus (025505-00/BAY)","80 g/l beta-Cyfluthrin, 100 g/l Clothianidin","Suspensionskonzentrat zur Saatgutbehandlung","Achtung | GHS07, GHS09 | EUH 208-0101, EUH 208-0111, EUH 401, H302, H332, H400, H410","SB001, SB110, SB193, SE1201, SF613, SF6161, SF618, SF619, SS1201, SS2204, SS6201, ST1202, ST1261, ST1271","NW262, NW264, NW467, NW811","NB663","NN1002, NN3001","NH677, NH679, NH680, NH681, NH682, NH6831, NT694, NT697, NT699, NT6991, NT700, VA265, WMI3A, WMI4A","31.12.2024","Futterrübe, Zuckerrübe","Moosknopfkäfer [nur zur Befallsminderung bei schwachem und mittlerem Befall]","Freiland vor der Saat max. Zahl Behandl.: 1, in der Kultur/je Jahr: 1 pillieren, 100 ml pro Einheit Saatgut max. Mittelaufwand 130 ml/ha (= max. 1,3 Saatgut-Einheiten pro ha) Bei hohem Befallsdruck ist die hinreichende Wirksamkeit nicht immer zu erreichen Wartezeit: F"]
database.loc[4] = ["Clothianidin + beta-Cyfluthrin","Mundus (006377-00/BAY)","80 g/l beta-Cyfluthrin, 300 g/l Clothianidin","Suspensionskonzentrat zur Saatgutbehandlung","Achtung | GHS07, GHS09 | EUH 208-0101, EUH 208-0111, EUH 401, H302, H332, H400, H410","SB001, SB110, SB193, SE1201, SF613, SF6161, SF618, SF619, SS1201, SS2204, SS6201, ST1202, ST1261, ST1271","NW262, NW264, NW467, NW811","NB663","NN1002, NN3001","NH677, NH679, NH680, NH681, NH682, NH6831, NT697, NT699, NT6991, NT700, VA265, WMI3A, WMI4A","31.12.2024","Futterrübe, Zuckerrübe","Rübenfliege, Moosknopfkäfer","Freiland max. Zahl Behandl.: 1, in der Kultur/je Jahr: 1 pillieren, Saatgutbehandlung, 100 ml pro Einheit Saatgut max. Mittelaufwand 130 ml/ha (= max. 1,3 Saatgut-Einheiten pro ha) Wartezeit: F"]
database.loc[5] = ["Clothianidin + beta-Cyfluthrin","Mundus (006377-00/BAY)","80 g/l beta-Cyfluthrin, 300 g/l Clothianidin","Suspensionskonzentrat zur Saatgutbehandlung","Achtung | GHS07, GHS09 | EUH 208-0101, EUH 208-0111, EUH 401, H302, H332, H400, H410","SB001, SB110, SB193, SE1201, SF613, SF6161, SF618, SF619, SS1201, SS2204, SS6201, ST1202, ST1261, ST1271","NW262, NW264, NW467, NW811","NB663","NN1002, NN3001","NH677, NH679, NH680, NH681, NH682, NH6831, NT697, NT699, NT6991, NT700, VA265, WMI3A, WMI4A","31.12.2024","Futterrübe, Zuckerrübe","Blattläuse","Freiland max. Zahl Behandl.: 1, in der Kultur/je Jahr: 1 pillieren, Saatgutbehandlung, 100 ml pro Einheit Saatgut max. Mittelaufwand 130 ml/ha (= max. 1,3 Saatgut-Einheiten pro ha) Eine hinreichende Wirksamkeit ist nicht immer bis zum Reihenschluss gegeben Wartezeit: F"]
database.loc[6] = ["Clothianidin + beta-Cyfluthrin","Poncho Beta (025495-00/BAY)","53 g/l beta-Cyfluthrin, 400 g/l Clothianidin","Suspensionskonzentrat zur Saatgutbehandlung","Achtung | GHS07, GHS09 | EUH 401, H302, H400, H410","SB001, SB110, SB193, SF6161, SF618, SF619, SS1201, SS2204, ST1202, ST1261, ST1271","NW262, NW264, NW467, NW811","NB663","NN1002, NN3001","NH677, NH679, NH680, NH681, NH682, NH6831, NT697, NT699, NT6991, NT700, WMI3A, WMI4A","31.12.2024","Futterrübe, Zuckerrübe","Tausendfüßler -Diplopoda, Rübenfliege, Moosknopfkäfer, Schnellkäfer -Drahtwurm, Blattläuse, Blattläuse als Virusvektoren","Freiland vor der Saat max. Zahl Behandl.: 1, in der Kultur/je Jahr: 1 pillieren, 150 ml pro Einheit Saatgut max. Mittelaufwand 195 ml/ha (= max. 1,3 Saatgut-Einheiten pro ha) Wartezeit: F"]
database.loc[7] = ["beta-Cyfluthrin","Contur plus (024215-00/BAY)","125 g/l","Suspensionskonzentrat zur Saatgutbehandlung",None,"SB001, SB110, SB193, SF6102, SS1201, SS2203, ST1202","NW262, NW264, NW467","NB663","NN400","NT677, NT679","31.12.2017","Weizen","Getreidebrachfliege","Freiland vor der Saat max. Zahl Behandl.: 1, in der Kultur/je Jahr: 1 Saatgutbehandlung, 60 ml/dt max. Mittelaufwand 108 ml/ha ( = max. 1,8 dt Saatgut pro ha) Wartezeit: F"]
database.loc[8] = ["Cymoxanil + Fludioxonil + Metalaxyl-M","WAKIL XL (006500-00/SYD)","100 g/kg Cymoxanil, 50 g/kg Fludioxonil, 170 g/kg Metalaxyl-M","Wasserdispergierbares Granulat","Achtung | GHS08, GHS09 | EUH 208-0029, EUH 401, H361d, H411","SB001, SB110, SF6142, SF6161, SF618, SS1201, SS2203, SS610, ST1261","NW467","NB663","NN160, NN165","NH677, NH678, NH6831, NT6971, WMFA1, WMFE2, WMFUN","31.12.2024","Futtererbse","Falscher Mehltau -Peronospora pisi, Brennfleckenkrankheit -Ascochyta pisi, Botrytis cinerea, Pythium-Arten -Pythium spp.","Freiland vor der Saat max. Zahl Behandl.: 1 Saatgutbehandlung, 200 g/dt max. Mittelaufwand 560 g/ha (= max. 2,8 dt Saatgut pro ha) Wartezeit: F"]


database.to_pickle('database.p')

with open('database_python2.p', 'wb') as fp:
    pickle.dump(database, fp, protocol=2)

test=database[database['Kultur'].str.contains("Futterrübe")]

