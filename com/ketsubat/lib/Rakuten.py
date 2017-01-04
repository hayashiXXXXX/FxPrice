'''
Created on 2016/12/31

@author: o-komuro
'''

# -*- coding: utf-8 -*-
import requests
import re

class Price:
    
    def getPrice(self, url):
        r = requests.get(url)
        result = {}
        
        rowpattern = r".+?\n"
        colpattern = r".+?\t"
        
        matchrowlist = re.findall(rowpattern, r.text)
        
        if matchrowlist:
            for row in matchrowlist:
                matchcollist = re.findall(colpattern, row)
                if matchcollist and len(matchcollist) > 10:
                    #
                    symbol = matchcollist[0].replace("\t", '')
                    value = matchcollist[12].replace("\t", '') + ',' + matchcollist[13].replace("\t", '')
                    if symbol == '1':
                        result['USD/JPY'] = value
                    elif symbol == '2':
                        result['EUR/JPY'] = value
                    elif symbol == '3':
                        result['GBP/JPY'] = value
                    elif symbol == '4':
                        result['AUD/JPY'] = value
                    elif symbol == '5':
                        result['NZD/JPY'] = value
                    elif symbol == '6':
                        result['ZAR/JPY'] = value
                    elif symbol == '7':
                        result['CAD/JPY'] = value
                    elif symbol == '8':
                        result['CHF/JPY'] = value
                    elif symbol == '11':
                        result['EUR/USD'] = value
        
        return result