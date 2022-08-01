from pprint import PrettyPrinter
from requests import get
'''
Code gets the head coaches from all NBA teams from an API
'''
#better way to print json
printer = PrettyPrinter()

def get_links(second_key, base_url = 'https://data.nba.net/',
         all_json ='/prod/v1/today.json' , fist_key = 'links',):
    '''getting the URL for the desired info'''
    response = get(base_url + all_json).json()
    final_url = response[fist_key][second_key]
    return base_url + final_url

def get_info (final_url):
    '''getting info from the final json'''
    my_info = get(final_url).json()
    return my_info

def get_hc(my_info):
    '''print all HC'''
    my_coaches = my_info['league']['standard']
    for coach in my_coaches:
        if coach['isAssistant'] is False:
            print(f"{coach['teamSitesOnly']['displayName']} Team: {coach['teamSitesOnly']['teamCode']}")

coaches_url = get_links('leagueRosterCoaches')

coach_info = get_info(coaches_url)

get_hc(coach_info)
'''
HELPS TO VISUALIZE THE JSON DATA
printer.pprint(my_info['displayName'])
YOU CAN CALL TO SEE THE KEYS
printer.pprint(data.keys())
'''