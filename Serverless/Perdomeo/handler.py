import json

def ApiOne(event, context):
    data = {
        "name": "John",             
        "age": 30,                  
        "city": "New York",         
        "profession": "Engineer",   
        "active": True              
    }
    
    return {
        "statusCode": 200,
        "body": json.dumps(data)  # Convertimos el diccionario en JSON string
    }

def ApiTwo(event, context):
    data = {
        "name": "Perdomeo",              
        "age": 28,                    
        "city": "Armenia",      
        "profession": "Enginer",     
        "active": False,              
        "country": "Colombia",             
        "email": "soyelmejor@agarrate.com", 
        "phone": "3145515589",      
        "company": "EAM",       
        "salary": 15000000              
    }
    
    return {
        "statusCode": 200,
        "body": json.dumps(data)  
    }
