import json
import pickle


__locations = None
__data_columns = None
__model= None


def get_location_names():
    return __locations


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    
    with open("./artifacts/columns.json",'r') as f:
        __data_columns=datajson.load(f)["data_columns"]
        __locations=__data_columns[3:]


    with open("./artifacts/BHP_model.pickle",'rb') as f:
        __model= pickle.load(f)
    print("loading saved artifacts... dome")

if __name__ == '__name__':
    load_saved_artifacts()
    print(get_location_names())
    