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


all = '''
    let $results := doc("/db/nr19/nr19_sprengel.xml")/Data/result
    let $parties := ('OEVP', 'SPOE', 'FPOE', 'NEOS', 'JETZT', 'GRUE', 'KPOE', 'WANDL', 'BIER')
    let $districts := (1 to 23)
    
    let $results_by_district:= for $district in $districts
    
    let $district_results:= for $d in $results
    where $d/BZ = $district
    return $d 
    
    (: Total votes = all votes - rejected votes:)
    let $abs_total_votes := sum(
        for $d in $district_results
            return $d/ABG - $d/UNG
    )   

    (: Relative votes by Party:)
    let $rel_votes_by_party := for $party in $parties
        let $abs_party_votes := sum(
            for $d in $district_results/*[local-name()=$party]
                return $d
        )
        return element {$party} {format-number((xs:decimal($abs_party_votes div $abs_total_votes * 100)), '0.00')}
        
    return element {concat('district-',$district)} {$rel_votes_by_party}
    
    return $results_by_district
'''


xquery = relative_result_by_party_and_district('SPOE', 8)


result = client.get(all)



print(result[0])