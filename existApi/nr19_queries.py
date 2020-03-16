from existApi.ExistApiClient import ExistClient
import existApi.config as config


client = ExistClient()


xquery = f'''
    let $x:= doc("{config.EXIST_DOCUMENT}")
    return $x/Data/result'''

result = client.get(xquery)





print(result)