from requests import request
from flask import Flask
from flask import request
from flask import make_response
from markupsafe import escape
import time
import json

#Var global para nome do json do bd
dbFile = "erp_db.json"
histFile = "historico.json"

app = Flask(__name__)

@app.route('/remove', methods = ['POST'])
def remove():    
    #Abre o arquivo json
    try:
        with open(dbFile, "r") as file:
            data = json.load(file)
    except:
        return responseFunc("Error")

    #Recebe o código via post, e a quantidade de vendidos
    prodcode = request.form.get('code', default = '0', type = int)
    prodquant= request.form.get('qtd', default = '0', type = int)

    if int(prodcode) <= 0:
        return responseFunc("Error")

    try:
        newValue = data[f"{prodcode}"]["prodQtd"] - prodquant
        if newValue < 0:
            return responseFunc("Error: Estoque indisponível")

        data[f"{prodcode}"]["prodQtd"] = newValue
    except:
        return responseFunc("Not Found")

    with open(dbFile, "w+") as file:
        json.dump(data, file)

    
    try:
        with open(histFile, "r") as fileHist:
            hist = json.load(fileHist)
    except:
        hist = {}

    hist[f"{time.time()}"] = {'prodCod' : prodcode, 'prodQtd': prodquant}
    with open(histFile,"w") as fileHist:
        json.dump(hist, fileHist)

    return responseFunc("OK")
#info de prod

@app.route('/getinfo', methods = ['POST'])
def getInfo():    
    #Abre o arquivo json
    try:
        with open(dbFile, "r") as file:
            data = json.load(file)
    except:
        return responseFunc("Error")
        

    #Recebe as informações via POST e converte para json
    prodcode = request.form.get('code', default = '0', type = int)
    if prodcode <= 0:
        return responseFunc("Error")

    try:
        result = data[f"{prodcode}"]    
    except:
        return responseFunc("Not Found")

    return responseFunc(result)

#update rp

@app.route('/update', methods = ['POST'])
def add():    
    #Abre o arquivo json
    try:
        with open(dbFile, "r") as file:
            data = json.load(file)
    except:
        data = {}

    #Recebe as informações via POST e converte para json
    prodcode = request.form.get('code', default = '0', type = int)
    if int(prodcode) <= 0:
        return responseFunc("Error")

    name = request.form.get('name', default = '', type = str)
    price  = request.form.get('price', default = '', type = float)
    qtd = request.form.get('qtd', default = '', type = int)
    data[f"{prodcode}"] = {'prodName' : name, 'prodPrice': price, 'prodQtd': qtd}

    with open(dbFile, "w+") as file:
        json.dump(data, file)
    
    return responseFunc("ok")

def responseFunc(result):
    response = make_response(result)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response
    

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=6000) 