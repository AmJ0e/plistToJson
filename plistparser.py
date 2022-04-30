import plistlib
import os.path
import json

def getlistfromdict(dict_name):
    for dictkey in dict_name.keys():
        if isinstance(dict_name[dictkey], list):
            return dictkey
    return "None"
        

def getList(dict):
    return dict.keys()

def removebytes(dictname):
    for state in dictname:

        #Code to check if the value of item is type list
        try: 
            if isinstance(dictname[state], list):

            #If Yes, create a empty list
                empty_list=list()

            #Loop through all elements of list
                for allelements in dictname[state]:
                    #And clean bytes for any element in the list which is of type byte
                    empty_list.append(removebytes(allelements))
                    
        except TypeError as e:
            print(dictname[state])
            return dictname[state]
        
            #And assign cleaned list back to dictionary
            dictname[state]=empty_list

        #Code to check if the value of item is type dictionary
        if isinstance(dictname[state], dict):
            #print(dictname[state])
            dictname[state]=removebytes(dictname[state])

        #Code to check if the value of item is type bytes
        if isinstance(dictname[state], bytes):
            try:
                #Try decoding it
                dictname[state]=dictname[state].decode()

            #If decode not successful, put bytes data
            except UnicodeDecodeError as e:
                dictname[state]="SomeBytesData"
                
    return dictname

#Function takes the absolute path of .plist file and return json version
def plistToJson(filename):

    #Check if file exists
    if os.path.exists(filename):
        with open(filename, 'rb') as fp:
            pl = plistlib.load(fp)
            cleandict=removebytes(pl)
            return json.dumps(cleandict,indent=4, sort_keys=True, default=str)

    #If not exists, throw json error :)
    else:
        return json.dumps({"Error":"File not found"})

#If code is run manually
if __name__ == "__main__":
    filename="TopSites.plist"   #Define your filename here
    print(plistToJson(filename))
