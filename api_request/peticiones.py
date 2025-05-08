# import requests


# def get_all(data_inicial,url_extencion):

#     url = f"https://apiribsburger.netlify.app/v1-api/{url_extencion}"

#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # Esto lanza una excepción si la respuesta tiene un error

#         data = response.json()  # Convierte la respuesta en formato JSON
#         return data["msg"]
#     except requests.exceptions.RequestException as e:
#         print(f"Error al hacer la solicitud: {e}")
#         return data_inicial
