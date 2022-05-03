import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import streamlit as st
from pandas_datareader import wb

pd.set_option('display.max_rows', 6)
undernourishment="SN.ITK.DEFC.ZS"
mortalityrate_under5="SH.DYN.MORT"
prevalenceunderweight_under5="SH.STA.MALN.ZS"
foodproduction="AG.PRD.FOOD.XD"
countrieslist = ['SOM', 'YEM', 'CAF', 'TCD', 'COD', 'AUT', 'FRA', 'SWE', 'DNK', 'CHE']

df1=wb.download(indicator=undernourishment,country=countrieslist, start="2019",end="2019")
df2=wb.download(indicator=mortalityrate_under5,country=countrieslist, start="2019",end="2019")
df3=wb.download(indicator=prevalenceunderweight_under5,country=countrieslist, start="2019",end="2019")
df4=wb.download(indicator=foodproduction,country=countrieslist, start="2019",end="2019")
df=df1.merge(df2,on="country").merge(df3,on="country").merge(df4,on="country")
df.columns=["Undernourishment %", "Mort Rate U5 per 1000 births", "% children under 5 underweight", "world food production index" ]
metric1 = df["Undernourishment %"]
metric2 = df["Mort Rate U5 per 1000 births"]
metric3 = df["% children under 5 underweight"]
metric4 = df["world food production index"]



