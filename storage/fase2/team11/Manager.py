from storage.avl import avlMode as avl
from storage.b import BMode as b
from storage.bplus import BPlusMode as bPlus
from storage.dict import DictMode as diccionario
from storage.isam import ISAMMode as isam
from storage.hash import HashMode as hash
from storage.json import jsonMode as json
from Binary import verify_string

mode_list = list()


class Mode:
    def __init__(self, name_database, mode, enconding):
        self.__name_database = name_database
        self.__mode = mode
        self.__enconding = enconding

    def set_name_database(self, name_database):
        self.__name_database = name_database

    def get_name_database(self):
        return self.__name_database

    def set_mode(self, mode):
        self.__mode = mode

    def get_mode(self):
        return self.__mode

    def set_encondig(self, encondig):
        self.__enconding = encondig

    def get_encondig(self):
        return self.__enconding


def save_mode(database, mode, encondig):
    new_mode = Mode(database, mode, encondig)
    mode_list.append(new_mode)


def exist(database: str):
    for mode in mode_list:
        if mode.get_name_database() == database:
            return True
    return False


def createDatabase(database: str, mode: str, encoding: str):
    if verify_string(database):
        if exist(database): return 2
        if encoding.lower().strip() is "ascii" or encoding.lower().strip() is "iso-8859-1" \
                or encoding.lower().strip() is "utf8":
            status = -1
            if mode.lower().strip() is "avl":
                status = avl.createDatabase(database)
            elif mode.lower().strip() is "b":
                status = b.createDatabase(database)
            elif mode.lower().strip() is "bplus":
                status = bPlus.createDatabase(database)
            elif mode.lower().strip() is "dict":
                status = diccionario.createDatabase(database)
            elif mode.lower().strip() is "isam":
                status = isam.createDatabase(database)
            elif mode.lower().strip() is "json":
                status = json.createDatabase(database)
            elif mode.lower().strip() is "hash":
                status = hash.createDatabase(database)
            else:
                return 3
            if status == 0:
                save_mode(database, mode, encoding)
            return status
        else:
            return 4
    else:
        return 1

def exist_Alter(database: str):
    indice=0
    for mode in mode_list:          
        if mode.get_name_database() == database:            
            return mode,indice
        indice+=1
    return None



def alterDatabaseMode(database: str, mode: str):
    ModeDB,indexDB = exist_Alter(database)
    mode_list.pop(indexDB)     
    createDatabase(database,mode,ModeDB.get_encondig())
    if ModeDB:
       
        oldMode = ModeDB.get_mode()
        if oldMode.lower().strip() == "avl":           
            tables=avl.showTables(database)     
            for tabla in tables:       
                listaDatos = get_Data(database,tabla,oldMode)
                numberColumns=len(listaDatos[0])
                insertAlter(database,tabla,numberColumns,mode,listaDatos)   
            avl.dropDatabase(database)        
        elif oldMode.lower().strip() == "b":           
            tables=b.showTables(database)     
            for tabla in tables:       
                listaDatos = get_Data(database,tabla,oldMode)
                numberColumns=len(listaDatos[0])
                insertAlter(database,tabla,numberColumns,mode,listaDatos)   
            b.dropDatabase(database)
        elif oldMode.lower().strip() == "bplus":           
            tables=bplus.showTables(database)     
            for tabla in tables:       
                listaDatos = get_Data(database,tabla,oldMode)
                numberColumns=len(listaDatos[0])
                insertAlter(database,tabla,numberColumns,mode,listaDatos)   
            bplus.dropDatabase(database)
        elif oldMode.lower().strip() == "dict":           
            tables=diccionario.showTables(database)     
            for tabla in tables:       
                listaDatos = get_Data(database,tabla,oldMode)
                numberColumns=len(listaDatos[0])
                insertAlter(database,tabla,numberColumns,mode,listaDatos)   
            diccionario.dropDatabase(database)
        elif oldMode.lower().strip() == "isam":           
            tables=isam.showTables(database)     
            for tabla in tables:       
                listaDatos = get_Data(database,tabla,oldMode)
                numberColumns=len(listaDatos[0])
                insertAlter(database,tabla,numberColumns,mode,listaDatos)   
            isam.dropDatabase(database)
        elif oldMode.lower().strip() == "hash":           
            tables=hash.showTables(database)     
            for tabla in tables:       
                listaDatos = get_Data(database,tabla,oldMode)
                numberColumns=len(listaDatos[0])
                insertAlter(database,tabla,numberColumns,mode,listaDatos)   
            hash.dropDatabase(database)
        elif oldMode.lower().strip() == "json":           
            tables=json.showTables(database)     
            for tabla in tables:       
                listaDatos = get_Data(database,tabla,oldMode)
                numberColumns=len(listaDatos[0])
                insertAlter(database,tabla,numberColumns,mode,listaDatos)   
            json.dropDatabase(database)

            
def insertAlter(database,tabla,numberColumns,mode,listaDatos):
    if mode.lower().strip() =="avl":
        avl.createTable(database,tabla,numberColumns)
        for data in listaDatos:                      
            avl.insert(database,tabla,data)
    elif mode.lower().strip() =="b":
        b.createTable(database,tabla,numberColumns)
        for data in listaDatos:                      
            b.insert(database,tabla,data)
    elif mode.lower().strip() =="bplus":
        bplus.createTable(database,tabla,numberColumns)
        for data in listaDatos:                      
            bplus.insert(database,tabla,data)
    elif mode.lower().strip() =="dict":
        diccionario.createTable(database,tabla,numberColumns)
        for data in listaDatos:                      
            diccionario.insert(database,tabla,data)
    elif mode.lower().strip() =="isam":
        isam.createTable(database,tabla,numberColumns)
        for data in listaDatos:                      
            isam.insert(database,tabla,data)
    elif mode.lower().strip() =="hash":
        hash.createTable(database,tabla,numberColumns)
        for data in listaDatos:                      
            hash.insert(database,tabla,data)
    elif mode.lower().strip() =="json":
        json.createTable(database,tabla,numberColumns)
        for data in listaDatos:                      
            json.insert(database,tabla,data)


            
            
def get_Data(database:str,table:str,mode:str):
    if mode.lower().strip() =="avl":
        return avl.extractTable(database,table)
    elif mode.lower().strip() =="b":
        return b.extractTable(database,table)
    elif mode.lower().strip() =="bplus":
        return bplus.extractTable(database,table)
    elif mode.lower().strip() =="dict":
        return diccionario.extractTable(database,table)
    elif mode.lower().strip() =="isam":
        return isam.extractTable(database,table)
    elif mode.lower().strip() =="hash":
        return hash.extractTable(database,table)
    elif mode.lower().strip() =="json":
        return json.extractTable(database,table)
