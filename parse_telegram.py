from tqdm import tqdm
from pyquery import PyQuery
import glob
import os

with open("chat/all.txt", "w") as out:

    files = glob.glob("chat/messages*.html")
    files.sort(key=os.path.getmtime)
    for file in tqdm(files, "Parsing html"):
        with open(file) as f:
            html = f.read()
        
        pq = PyQuery(html)
        tags = pq(".message.default.clearfix")
        
        for tag in tags:
            name = pq(tag.find_class("from_name")).text()
            text = tag.find_class("text");
            if len(text)>0:
                text = pq(text).text()
                out.write("{"+name+"}:\t"+text+"\n")
