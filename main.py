import os
import json
from datetime import datetime
from crawler import get_patents

num, patents = get_patents(datetime.strptime("2023/4/1", "%Y/%m/%d"), limit = 200)
print(num)
with open("patent_example.json", 'w', encoding="utf-8") as f:
    json.dump([p.__dict__() for p in patents], f, ensure_ascii=False, indent=4)
