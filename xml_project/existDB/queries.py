import xml_project.existDB.config as config


def absolut_votes_by_party_and_district(party, district):
    return f'''
        declare namespace nr19 = "http://nr19.org/nr19_schema";

        let $results:=doc("{config.EXIST_DOCUMENT}")/nr19:root/nr19:result
        let $district:= for $d in $results
        where $d/nr19:BZ = {district}
        return $d
        let $abs_party_votes:= sum(
            for $x in $district
            return $x/{party}
        )
    '''


def relative_result_by_party_and_district(party, district):
    return f'''
        declare namespace nr19 = "http://nr19.org/nr19_schema";

        let $results:= doc("{config.EXIST_DOCUMENT}")/nr19:root/nr19:result
        let $district:= for $d in $results
        where $d/nr19:BZ = {district}
        return $d
        let $abs_party_votes:= sum(
            for $x in $district
            return $x/{party}
        )
       let $abs_participation:= sum(
            for $x in $district
            return $x/nr19:ABG - $x/nr19:UNG
        )
        return $abs_party_votes div $abs_participation
'''


relative_results_all = '''
    declare namespace nr19 = "http://nr19.org/nr19_schema";

    let $results := doc("/db/nr19/nr19_sprengel.xml")/nr19:root/nr19:result
    let $parties := ('OEVP', 'SPOE', 'FPOE', 'NEOS', 'JETZT', 'GRUE', 'KPOE', 'WANDL', 'BIER')
    let $districts := (1 to 23)

    let $results_by_district:= for $district in $districts
    
        let $district_results:= for $d in $results
        where $d/nr19:BZ = $district
        return $d 
    
        (: Total votes = all votes - rejected votes:)
        let $abs_total_votes := sum(
            for $d in $district_results
            return $d/nr19:ABG - $d/nr19:UNG
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

relative_results_all_sorted = '''
    declare namespace nr19 = "http://nr19.org/nr19_schema";

    let $results := doc("/db/nr19/nr19_sprengel.xml")/nr19:root/nr19:result
    let $parties := ('OEVP', 'SPOE', 'FPOE', 'NEOS', 'JETZT', 'GRUE', 'KPOE', 'WANDL', 'BIER')
    let $districts := (1 to 23)

    let $results_by_district:= for $district in $districts
    
        let $district_results:= for $d in $results
        where $d/nr19:BZ = $district
        return $d 
    
        (: Total votes = all votes - rejected votes:)
        let $abs_total_votes := sum(
            for $d in $district_results
            return $d/nr19:ABG - $d/nr19:UNG
        )

        (: Relative votes by Party:)
        let $rel_votes_by_party := for $party in $parties
            let $abs_party_votes := sum(
                for $d in $district_results/*[local-name()=$party]
                return $d
            )
            return element {$party} {format-number((xs:decimal($abs_party_votes div $abs_total_votes * 100)), '0.00')}
        
        let $rel_sorted:= for $x in $rel_votes_by_party order by xs:decimal($x/data()) descending return $x
        return element {concat('district-',$district)} {$rel_sorted}
    
    return $results_by_district
'''

participation = '''
    declare namespace nr19 = "http://nr19.org/nr19_schema";

    let $results := doc("/db/nr19/nr19_sprengel.xml")/nr19:root/nr19:result
    let $districts := (1 to 23)

    
    let $results_by_district:= for $district in $districts
    
    let $district_results:= for $d in $results
    where $d/nr19:BZ = $district
    return $d
    
    let $votes := sum(
        for $d in $district_results
            return $d/nr19:ABG
    )
    
    let $voters := sum(
        for $d in $district_results
            return $d/nr19:WBER
    )
    
    return element {concat('district-',$district)} {format-number((xs:decimal($votes div $voters * 100)), '0.00')}
    return $results_by_district
'''

winner = '''
    declare namespace nr19 = "http://nr19.org/nr19_schema";

    let $results := doc("/db/nr19/nr19_sprengel.xml")/nr19:root/nr19:result
    let $parties := ('OEVP', 'SPOE', 'FPOE', 'NEOS', 'JETZT', 'GRUE', 'KPOE', 'WANDL', 'BIER')
    let $districts := (1 to 23)

    let $results_by_district:= for $district in $districts
    
        let $district_results:= for $d in $results
        where $d/nr19:BZ = $district
        return $d 
    
        (: Total votes = all votes - rejected votes:)
        let $abs_total_votes := sum(
            for $d in $district_results
            return $d/nr19:ABG - $d/nr19:UNG
        )

        (: Relative votes by Party:)
        let $rel_votes_by_party := for $party in $parties
            let $abs_party_votes := sum(
                for $d in $district_results/*[local-name()=$party]
                return $d
            )
            return element {$party} {format-number((xs:decimal($abs_party_votes div $abs_total_votes * 100)), '0.00')}
        
        let $rel_sorted:= for $x in $rel_votes_by_party order by xs:decimal($x/data()) descending return $x
        return element {concat('district-',$district)} {$rel_sorted[1]/name()}
    
    return $results_by_district
'''
