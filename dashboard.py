import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import hunger_data
import education_data

st.title('UN SDGs Dashboard')
st.markdown('The United Nations adopted the Sustainable Development Goals (SDGs), also known as the Global Goals, in 2015 as a universal call to action to end poverty, protect the environment, and ensure that by 2030, all people enjoy peace and prosperity.')
st.markdown('This dashboard will help us visualize the status of each SDGs around the world.')
st.header('Hunger')
st.markdown('Despite the fact that more than enough food is produced to support the world\'s population, up to 811 million people go hungry. After dropping gradually for a decade, global hunger is on the rise, impacting 9.9 percent of the world\'s population. Between 2019 and 2020, the number of undernourished people increased by up to 161 million, owing mostly to conflict, climate change, and the COVID-19 pandemic.')
st.markdown('We used the following indicators to access the hunger data around the world:')
st.subheader('Undernourishment by % in 2019')
st.bar_chart(hunger_data.metric1)
st.markdown('The most important most direct measurement of hunger is undernourishment. Undernourishment is measured by the % of the population who receive enough food and nutrients to have healthy bodies.')
st.subheader('Mortality Rate Children Under 5 per 1000 births in 2019')
st.bar_chart(hunger_data.metric2)
st.markdown('Mortality rate under 5 % is another fairly good metric because access to food is often a major reason for child mortality along with clean water.')
st.subheader('% children under 5 underweight in 2019')
st.bar_chart(hunger_data.metric3)
st.markdown('Prevalence under weight of 5 year olds is the next best measure because access to food is almost entirely the culprit for this metric. A society that can provide food to all its little children is a sign the society can use resources to grow and develop those who cannot help themselves (and are in a family situation that is healthy). A high under weight metric means there is not enough food and that can be connected to the socioeconomic status of the vast majority of citizens in a country.')
st.subheader('World Food Production Index in 2019')
st.bar_chart(hunger_data.metric4)
st.markdown('The last indicator used is food production, which can be a good measurement of whether a country can feed its citizens. It may also be misleading because there may be propserous countries that import their food. Thus, we see little difference between developed countries and developing countries when it comes to food supply. This drives the message that even a country producing enough food supply still may not be able to feed itself and shows how much global supply chains are relied upon to feed the world. ')


st.header('Quality Education')
st.markdown('Quality education enables people to escape the cycle of poverty, reduces inequities, and achieves gender equality. It also enables people to live a healthier and more sustainable existence, and it is critical for the development of tolerance and peaceful society.')
st.markdown('We used the following indicators to access the quality education data around the world:')
st.subheader('Literacy rate of youth')
st.bar_chart(education_data.metric1)
st.markdown('The most important most direct measurement of quality education is the literacy rate of the youth. ')
st.subheader('Secondary School Enrolment')
st.bar_chart(education_data.metric2)
st.markdown('The % of people who enrol in secondary school ensures that the population has received basic education.')
st.subheader('CPIA gender equality rating')
st.bar_chart(education_data.metric3)
st.markdown('A country with low gender equality tend to have less opportunities for women to receive education so it is also a great secondary indicator')
