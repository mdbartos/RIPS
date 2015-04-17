import requests
import re
import pandas as pd

h = requests.get('http://www.ferc.gov/docs-filing/forms/form-714/data.asp')
dirs = [re.findall('[a-zA-Z0-9]*\.zip', i) for i in re.split('\d\d\d\d</th>', h.text)]
yrs = [i.replace('</th>', '') for i in re.findall('\d\d\d\d</th>', h.text)]

d = dict(zip(yrs, dirs[1:]))

rlists = {}

for i in range(1993,2000):
    df = pd.read_html('http://www.ferc.gov/docs-filing/forms/form-714/data/%slist.htm' % (i))
    rlists.update({i : df})
