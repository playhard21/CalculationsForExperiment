# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 18:11:43 2020

@author: karri
"""

import pandas as pd
import statistics
import os
import matplotlib.pyplot as plt
#Function to Generate peer resistence
def generate_peerResistance(path):
    #Reading file form folder
    file = pd.read_csv(path, sep="\t", header=None, engine='python')

    #Deleting the first for because it has names
    file = file.iloc[1:]

    #Naming the coloums
    file.columns = ['Z', 'K', 'W', 'P'];
    #this is to convert europian system
    file['K'] = file['K'].str.replace(',', '.');
    file['P'] = file['P'].str.replace(',', '.');
    #Changing the required files to float from string
    file['K'] = pd.to_numeric(file['K'],errors='coerce');
    file['P'] = pd.to_numeric(file['P'],errors='coerce');
    
    #taking mean value of Kraft
    Kraft = []
    for i, row in file.iterrows():
        if row['P'] > 20 and row['P'] < 100 :
            Kraft.append(row['K'])
    #calculating peerResistance
    Fmitt = statistics.mean(Kraft);
    
    peerResistence = Fmitt/20
    
    return peerResistence

PeerResistenceForFile = [];
#Iterate over files in the folder
fileLocation = r"C:\Users\karri\Desktop\ObaidThesis\test22"

directory = os.fsencode(fileLocation)

for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if  filename.endswith(".txt"):
         filePath = fileLocation + '\\' + filename
         value = generate_peerResistance(filePath)
         peerForFile = (filename,value)
         PeerResistenceForFile.append(peerForFile)
         continue
     else:
         continue

#Peer resistence arry         
print(PeerResistenceForFile)

#Graph of peer resistence
zip(*PeerResistenceForFile)
plt.plot(*zip(*PeerResistenceForFile))
plt.title('Test Figure')
plt.xlabel('storage time')
plt.ylabel('Peer-Resistence')
result = plt.gcf()
result(figsize=(70, 70));
plt.show()

#this is for figure

result.savefig('result.pdf', format='pdf')
