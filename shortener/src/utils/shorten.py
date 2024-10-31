from urllib.parse import urlparse 
import string
import hashlib
import os

def shorten(link: str):
    parsed_url = urlparse(link)
    
    domain, path = parsed_url.netloc.split('.')[0], parsed_url.path
    
    return generate_random_short_url(user_url_domain=domain, path=path)




def generate_random_short_url(user_url_domain: str, path: str, length: int = 5):
    """Генерирую токен из path + соль. Соль должна быть в переменных среды"""
    
    salted_path = path + "mySalt"
    
    token = hashlib.shake_256(salted_path.encode()).hexdigest(length)
    
    return f"{user_url_domain}-{token}"