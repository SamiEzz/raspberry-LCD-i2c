
import json

def read_js(line=1):
        with open('data.json') as json_file:
                data= json.load(json_file)

                for p in data['read']:
                        if(line==1):
                                return(p['msg1'])
                        elif(line==2):
                                return(p['msg2'])
"""
Testing code :
"""
#output=read_js()
#print(output)
#output=read_js(2)
#print(output)
