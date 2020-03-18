from existApi.ExistApiClient import ExistClient
import existApi.config as config


client = ExistClient()



def get_sum(node):
    return str(f'''
        
        ''')


xquery = f'''
    let $x:= doc("{config.EXIST_DOCUMENT}")
    return $x/Data/result'''


xquery = f'''
    let $x:= doc("{config.EXIST_DOCUMENT}")
    for $k in $x/Data/result
    where $k/SPOE < 10 order by $k/DISTRICT_CODE   
    return $k
'''

xquery = f'''
        let $results:=doc("{config.EXIST_DOCUMENT}")/Data/result
        let $spoe:= sum(
            for $x in $results
            return $x/SPOE
        )
       let $beteiligung:= sum(
            for $x in $results
            return $x/ABG - $x/UNG
        )

        return $spoe div $beteiligung
'''

xquery = f'''

        let $results:=doc("{config.EXIST_DOCUMENT}")/Data/result
        let $bez:= for $b in $results
        where $b/BZ = 8
        return $b


        let $spoe:= sum(
            for $x in $bez
            return $x/SPOE
        )
       let $beteiligung:= sum(
            for $x in $bez
            return $x/ABG - $x/UNG
        )

        return $spoe div $beteiligung
'''


def absolut_votes_by_party_and_district(party, district):
    return f'''
        let $results:=doc("{config.EXIST_DOCUMENT}")/Data/result
        let $district:= for $d in $results
        where $d/BZ = {district}
        return $d
        let $abs_party_votes:= sum(
            for $x in $district
            return $x/{party}
        )
    '''

def relative_result_by_party_and_district(party, district):
    return f'''
        let $results:=doc("{config.EXIST_DOCUMENT}")/Data/result
        let $district:= for $d in $results
        where $d/BZ = {district}
        return $d
        let $abs_party_votes:= sum(
            for $x in $district
            return $x/{party}
        )
       let $abs_participation:= sum(
            for $x in $district
            return $x/ABG - $x/UNG
        )
        return $abs_party_votes div $abs_participation
'''
xquery = relative_result_by_party_and_district('SPOE', 8)

result = client.get(xquery)



print(result[0])