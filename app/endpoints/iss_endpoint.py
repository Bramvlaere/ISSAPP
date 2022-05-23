import requests as rqs

def isscheck():
    ''''
    Takes in info through json (guard lastname) request to create new guard and commits it to the database after it checks if there are no duplicates
    :PARAM None
    :RETURN json Succes statement

    ''' 
    try:
        r = rqs.get('http://api.open-notify.org/astros.json')
    except Exception as e:
        raise e
    print(r.json)
    return r.json()