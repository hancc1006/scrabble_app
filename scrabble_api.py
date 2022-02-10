import json as js

def json_load(score):
    string1={"score":score}
    storedata=js.dumps(string1)
    return storedata