from existApi.ExistApiClient import ExistClient
import existApi.config as config


client = ExistClient()


xquery = f'''
    let $x:= doc("{config.EXIST_DOCUMENT}")
    return $x/Data/result'''


xquery = f'''
    let $x:= doc("{config.EXIST_DOCUMENT}")
    for $k in $x/Data/result
    where $k/SPOE < 10 order by $k/DISTRICT_CODE   
    return $k
'''

result = client.get(xquery)



print(result)