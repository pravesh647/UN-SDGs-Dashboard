import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from pandas_datareader import wb
pd.set_option('display.max_rows', 15)
literacyRate="SE.ADT.1524.LT.ZS"
secondary_enrolment="SE.SEC.NENR"
gender_equality="IQ.CPA.GNDR.XQ"
countrieslist = ['BDI', 'SOM', 'MOZ', 'MDG', 'SLE', 'USA', 'CHN', 'DEU', 'JPN', 'GBR']
df1=wb.download(indicator=literacyRate,country=countrieslist, start="2019",end="2019")
df2=wb.download(indicator=secondary_enrolment,country=countrieslist, start="2019",end="2019")
df3=wb.download(indicator=gender_equality,country=countrieslist, start="2019",end="2019")
df=df1.merge(df2,on="country").merge(df3,on="country")
df.columns=["% of Literacy rate of youth", "Secondary School Enrolment", "CPIA gender equality rating"]
metric1 = df["% of Literacy rate of youth"]
metric2 = df["Secondary School Enrolment"]
metric3 = df["CPIA gender equality rating"]
