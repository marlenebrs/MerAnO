import json
def check_json(id):
    new=open('try.json')
    load=json.load(new)
    for l in range (len(load)) :
        name=load[l]
        name=name.get('mini')
        if id in name:
            path=load[l].get('max')
            return (path)

id="M00001"
print(verify_json(id))
