import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import urllib.request, urllib, json 

@st.cache
def getDepData(path='/',**kargs):
    path = 'https://dadosabertos.camara.leg.br/api/v2/%s'%path
    queryPairs = ['%s=%s'%i for i in kargs.items()]
    path = '%s?%s'%(path,'&'.join(queryPairs))

    print(path)

    request = urllib.request.Request(path,headers={'content-type':'application/json;charset=UTF-8'})
    
    with urllib.request.urlopen(request) as u:
        body = u.read()
        data = json.loads(body)
        df = pd.read_json(json.dumps(data['dados']))
        return df

"""
Os mandatos são organizados em legislaturas e cada uma representa um intervalo de 4 anos.
"""
allLegislaturas = getDepData('legislaturas').copy()
if 'uri' in allLegislaturas.columns:
    del allLegislaturas['uri']
allLegislaturas = allLegislaturas.set_index('id')

st.table(allLegislaturas)

