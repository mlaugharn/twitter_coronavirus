hashtags = [
    '#코로나바이러스',  # korean
    '#コロナウイルス',  # japanese
    '#冠状病毒',        # chinese
    '#covid2019',
    '#covid-2019',
    '#covid19',
    '#covid-19',
    '#coronavirus',
    '#corona',
    '#virus',
    '#flu',
    '#sick',
    '#cough',
    '#sneeze',
    '#hospital',
    '#nurse',
    '#doctor',
    ]

paths = ['reduced.country', 'reduced.lang']
import os
for path in paths:
    for hashtag in hashtags:
        t = 'country' if path.endswith('country') else 'lang'
        cmd =f'./src/visualize.py --input_path {path} --key "{hashtag}" | head > viz/{hashtag}_{t}' 
        print(cmd)
        os.system(cmd) 
