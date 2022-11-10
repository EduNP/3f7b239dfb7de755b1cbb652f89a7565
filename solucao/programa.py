import time, threading, requests, json, os

FLAG = 0

configuration = None

with open("config.json","r") as file_:
    configuration = json.load(file_)

def get_changes(url_):

    info = requests.get(url_)
    return info

def send_changes_Marketplace(name, info, code):

    url_ = configuration[name]["MARKETPLACES_URLS"]["UPDATE"]

    marketplace = info["marketplace"]
    data_ = {
        configuration[name]["MARKETPLACES_PARAMS"]["UPDATE"]["code"]:code,
        configuration[name]["MARKETPLACES_PARAMS"]["UPDATE"]["name"]:info[configuration[marketplace]["MARKETPLACES_PARAMS"]["GET_INFO"]["name"]],
        configuration[name]["MARKETPLACES_PARAMS"]["UPDATE"]["price"]:info[configuration[marketplace]["MARKETPLACES_PARAMS"]["GET_INFO"]["price"]],
        configuration[name]["MARKETPLACES_PARAMS"]["UPDATE"]["qtd"]:info[configuration[marketplace]["MARKETPLACES_PARAMS"]["GET_INFO"]["qtd"]]
    }

    requests.post(url_, data=data_)
    print(f"UPDATE {code} at {name}")

def marketplace_monitor(name):
    
    print(f"---- Monitor at {name} ----")

    url_ = configuration[name]["MARKETPLACES_URLS"]["GET_INFO"]
    
    old_info = None
    new_info = None

    try:
        old_info = json.loads(get_changes(url_).text)
        print(name, "GET Changes")
    except:
        print(name, "GET Error")

    while(True):
        
        print(f"---- Monitor at {name} ----")

        global FLAG

        if FLAG == 1:
            break

        time.sleep(1)

        try:
            new_info = json.loads(get_changes(url_).text)
            print(name, "GET Changes")
        except:
            print(name, "GET Error")

        if old_info != new_info:
            print("Change detected")
            with open("list.json","r+") as file_:
                FLAG = 1

                info = json.loads(file_.read())
                for item in new_info:
                    code = str(item)
                    break
                new_info[code]["marketplace"] = name
                info |= new_info
                file_.seek(0)
                file_.write(json.dumps(info, indent=4))

            old_info = new_info   

        else:
            print(name, "Nothing changed")

def create_threads():

    for shop in configuration:
        thread_ = threading.Thread(target=marketplace_monitor, args=(shop,))
        thread_.start()

def send_data(info, code):

    for shop in configuration:
        try:
            send_changes_Marketplace(shop, info, code)
        except:
            print(shop, f"UPDATE at {code} not done")

if __name__ == "__main__":
    
    while(True):

        FLAG = 0

        with open("list.json","w") as file_:
            file_.write("{}")

        try:
            create_threads()

        except:
            print("Thread Error")

        while(threading.active_count() != 1):
            pass

        with open("list.json","r") as file_:

            info = json.loads(file_.read())

            for code in info:
                try:
                    thread_ = threading.Thread(target=send_data,args=(info[code], code,))
                    thread_.start()

                except:
                    print("Thread Error")
                
        while(threading.active_count() != 1):
            pass
