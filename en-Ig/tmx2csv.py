import os
from bs4 import BeautifulSoup
import pandas as pd

def convert_to_csv(content):
    tu_elements_list = content.find_all('tu')
    output_dict = {'en': [], 'ig': []}
    for tu_element in tu_elements_list:
        tuvs = tu_element.find_all('tuv')
        for tuv in tuvs:
            if tuv['xml:lang'] == 'en':
                output_dict['en'].append(tuv.text)
            else:
                output_dict['ig'].append(tuv.text)
    df = pd.DataFrame(data=output_dict)
    return df

with open('en-ig.tmx', 'r', encoding='utf-8') as f:
    content = BeautifulSoup(f, "html.parser")
    output_df = convert_to_csv(content)
    output_df.to_csv('en-ig.csv', index=None)
