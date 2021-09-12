from pymongo import MongoClient

uri = 'mongodb://root:123mudar@localhost:27017/'

client = MongoClient(uri)
database = client['teste']
collection = database['tb_teste']

def insert(**args):
    collection.insert(args)

def getAll():
    print('GET ALL >>>', list(collection.find()))

def getByName(operador, valor):
    print(list(collection.find(
        {
            'nome':{
                operador:valor
            }
        }
    )))

def update():
    #collection.update para somente 1
    #collection.update_many para mais de 1
    collection.update_many(
        {'nome':'XPTO'},
        {
            '$set':{'telefone':'888'}
        }
    )

def remove(operador, valor):
    #collection.remove para somente 1
    #collection.delete_many para mais de 1
    (collection.delete_many(
        {
            'nome':{
                operador:valor
            }
        }
    ))    



if __name__ == "__main__":
    insert(nome="fulano", telefone='3499999')
    getAll()
    getByName('$eq','XPTO')
    update()
    getByName('$eq','XPTO')
    remove('$eq','fulano')
    getAll()