import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


mhd_co2 = str('Assesment2/Data/mhd_co2.csv')
mhd_n2o = str('Assesment2/Data/mhd_n2o.csv')
mhd_ch4 = str('Assesment2/Data/mhd_ch4.csv')

tac_co2 = str('Assesment2/Data/tac_co2.csv')
tac_n2o = str('Assesment2/Data/tac_n2o.csv')
tac_ch4 = str('Assesment2/Data/tac_ch4.csv')

class Data:
    def __init__(self, pathway):
        self.pathway = pathway
        self.data = pd.read_csv(f"{self.pathway}")
        x = self.data['time']
        y = self.data['mf']

    def __str__(self):
        print(f'{self.data}')

    def average_daily(self):
        raw_data = self.data
        Averages = raw_data.groupby(np.arange(len(raw_data)) // 24).mean()
        Averages.rename(columns = {'mf' : 'Daily Average'}, inplace = True)
        days = list(range(1,366))
        Averages['Day'] = days
        return Averages

    def plot_graph(self):

        plt.plot(self.data['time'], self.data['mf'])
        plt.xlabel('Time')
        plt.ylabel('mf Value ')
        plt.show()

co2_mhd = Data(mhd_co2)
n2o_mhd = Data(mhd_n2o)
ch4_mhd = Data(mhd_ch4)

co2_tac = Data(tac_co2)
n2o_tac = Data(tac_n2o)
ch4_tac = Data(tac_ch4)


species_info = pd.read_csv('Assesment2/species_info.csv')
CO2 = species_info.iloc[0]
CH4 = species_info.iloc[1]
N2O = species_info.iloc[2]
