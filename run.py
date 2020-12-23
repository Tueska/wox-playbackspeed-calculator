# -*- coding: utf-8 -*-

import re
from wox import Wox

class HelloWorld(Wox):

    def query(self, query):
        results = []

        rhh = re.findall('\d*h', query)
        rmm = re.findall('\d*m', query)
        rmultiplier = re.findall('\d*\.?\d{1,}x', query)

        hh = float(rhh[0].replace('h', '')) if (len(rhh) != 0) else 0
        mm = float(rmm[0].replace('m', '')) if (len(rmm) != 0) else 0
        multiplier = float(rmultiplier[0].replace('x', '')) if (len(rmultiplier) != 0) else 1        

        timeInMinutes = (hh*60) + mm
        newTimeInMinutes = timeInMinutes / multiplier
        savedMinutes = timeInMinutes - newTimeInMinutes

        results.append({
            "Title": "Playback Time: {}h {}m".format(int(newTimeInMinutes/60), int(newTimeInMinutes%60)),
            "SubTitle": "Saved Time: ~{}h {}m".format(int(savedMinutes/60), int(savedMinutes%60)),
            "IcoPath":"clock.png",
            "ContextData": "ctxData"
        })
        
        return results

if __name__ == "__main__":
    HelloWorld()
