import json

with open('SearchShowAction.json','r',encoding = 'utf-8-sig') as f:
    show = json.load(f)
    print(json.dumps(show, indent=4,ensure_ascii=False))