import pandas as pd

def runManipulate():
    df = pd.read_csv('./files/names.csv', delimiter=';')

    newDf = df[['ID','NOME', 'URL']].copy()

    dfResult = newDf[['ID', 'NOME']].groupby(['ID']) \
        .size().reset_index(name='VISITAS')

    dfMerge = pd.merge(newDf.drop_duplicates(keep='first'), dfResult, on='ID')

    dfMerge.sort_values(by=['VISITAS'], ascending=False) \
        .to_csv('./files/resultado.csv', sep=';', encoding='utf-8', index=False)
