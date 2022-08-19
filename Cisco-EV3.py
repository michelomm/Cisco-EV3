import requests
import json
import conf

sandbox = "https://10.10.20.14"

def obtener_token(usuario, clave):
    url = "https://10.10.20.14/api/aaaLogin.json"
    body = {
        "aaaUser": {
            "attributes": {
                "name": usuario,
                "pwd": clave
            }
        }
    }
    cabecera = {
        "Content-Type": "application/json"
    }
    requests.packages.urllib3.disable_warnings()
    respuesta = requests.post(url, headers=cabecera, data=json.dumps(body), verify=False)
    token = respuesta.json()['imdata'][0]['aaaLogin']['attributes']['token']
    return token

# GET http://apic-ip-address/api/class/topSystem.json
# obtener_token(conf.usuario, conf.clave)
def top_system():
    cabecera = {
        "Content-Type": "application/json"
    }
    clavetoken = {
        "APIC-Cookie": obtener_token(conf.usuario, conf.clave)
    }
    requests.packages.urllib3.disable_warnings()
    respuesta = requests.get(sandbox+"/api/class/topSystem.json", headers=cabecera, cookies=clavetoken, verify=False)

    total_nodos = int(respuesta.json()["totalCount"])

    for i in range(0, total_nodos):
        ip_local = respuesta.json()["imdata"][i]["topSystem"]["attributes"]["address"]
        print(ip_local)

top_system()
