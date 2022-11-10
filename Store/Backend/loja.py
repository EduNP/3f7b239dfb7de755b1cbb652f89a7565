from flask import Flask
from flask import request
from flask import make_response
from markupsafe import escape
import json

app = Flask(__name__)

@app.route('/update', methods = ['POST'])
def add():    
    #Abre o arquivo json
    try:
        with open("loja.json", "r") as file:
            data = json.load(file)
    except:
        data = {}
        #branco, arquivo criado ao fim do método
    print(request.form)
    #Recebe as informações via POST e converte para json
    prodcode = request.form.get('code', default = '0', type = int)
    if int(prodcode) <= 0:
        return responseFunc("Error")

    name = request.form.get('name', default = '', type = str)
    if name == '':
        name = data[f"{prodcode}"]['prodName']

    price  = request.form.get('price', default = -1, type = float)
    if price == -1:
        price = data[f"{prodcode}"]['prodPrice']

    qtd = request.form.get('qtd', default = '', type = int)

    data[f"{prodcode}"] = {'prodName' : name, 'prodPrice': price, 'prodQtd': qtd}

    with open("loja.json", "w+") as file:
        json.dump(data, file)
    
    return responseFunc("ok")

@app.route('/remove', methods = ['POST'])
def remove():    
    #Abre o arquivo json
    try:
        with open("loja.json", "r") as file:
            data = json.load(file)
    except:
        return responseFunc("Error")
        #branco, arquivo criado ao fim do método

    #Recebe as informações via POST e converte para json
    prodcode = request.form.get('code', default = '0', type = int)
    if prodcode <= 0:
        return responseFunc("Error")

    try:
        del data[f"{prodcode}"]
    except:
        return responseFunc("Not Found")

    with open("loja.json", "w+") as file:
        json.dump(data, file)

    return responseFunc("OK")


@app.route('/getinfo', methods = ['POST'])
def getInfo():    
    #Abre o arquivo json
    try:
        with open("loja.json", "r") as file:
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


@app.route('/')
def getItens():    
    #Abre o arquivo json
    try:
        with open("loja.json", "r") as file:
            data = json.load(file)
    except:
        return responseFunc("No Item")

    if len(data) == 0:
        return responseFunc("No Item")
        
    return responseFunc(data)

def responseFunc(result):
    response = make_response(result)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response
    

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000) 