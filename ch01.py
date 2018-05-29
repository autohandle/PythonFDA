# coding: utf-8
import matplotlib.pyplot as plt
import pandas as pd
names1880 = pd.read_csv('yob1880.txt', names=['name', 'sex', 'births'])
names1880
names1880.groupby('sex')['births'].sum()
years=range(1880,2017)
pieces=[]
columns=['name', 'sex', 'births']
for year in years:
    path='yob%d.txt'%year
    frame=pd.read_csv(path, names=columns)
    frame['year']=year
    pieces.append(frame)  
names=pd.concat(pieces,ignore_index=True)
names
total_births = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)
total_births.tail()
total_births.plot(title='total births by sex and year')
total_births.plot(title='total births by sex and year')
total_births.plot(title='total births by sex and year')
get_ipython().system('conda info --envs')
#get_ipython().run_line_magic('save', 'ch01 1-21')
total_births.plot(title='total births by sex and year')
