from __future__ import print_function
import httplib2
import os
import time
from plotGraph import trace_graph
from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def main():
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '1gCzjBwVzXZ7Gdvs2QN4INrtTguvRB29tR7szQXh1_Vw'
    rangeName = 'Sheet1!A4:AG369'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])

    budget = {}

    if not values:
        print('No data found.')
    else:
        print('Worked - creating graph')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            #print('%s, %s, %s' % (row[2], str(float(row[18][1:].replace(',', ''))+float(row[19][1:].replace(',', ''))+float(row[20][1:].replace(',', ''))+float(row[21][1:].replace(',', ''))+float(row[22][1:].replace(',', ''))), str(float(row[18][1:].replace(',', '')))))
            budget[row[2]] = [str(float(row[13][1:].replace(',', ''))+float(row[14][1:].replace(',', ''))+float(row[15][1:].replace(',', ''))+float(row[16][1:].replace(',', ''))+float(row[17][1:].replace(',', ''))), str(float(row[13][1:].replace(',', '')))]


    # do the same for last year figures from same google sheets (sheet2)

    rangeName = 'Sheet2!A4:W368'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])

    lastYear = {}

    if not values:
        print('No data found.')
    else:
        # print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            #print('%s, %s, %s' % (row[2], str(float(row[18][1:].replace(',', ''))+float(row[19][1:].replace(',', ''))+float(row[20][1:].replace(',', ''))+float(row[21][1:].replace(',', ''))+float(row[22][1:].replace(',', ''))), str(float(row[18][1:].replace(',', '')))))
            lastYear[row[2]] = [str(float(row[18][1:].replace(',', ''))+float(row[19][1:].replace(',', ''))+float(row[20][1:].replace(',', ''))+float(row[21][1:].replace(',', ''))+float(row[22][1:].replace(',', ''))), str(float(row[18][1:].replace(',', '')))]


    #print(budget)
    return budget, lastYear

if __name__ == '__main__':
    main()


def spa_main():
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '1gCzjBwVzXZ7Gdvs2QN4INrtTguvRB29tR7szQXh1_Vw'
    rangeName = 'Sheet1!A4:AG369'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])

    budget = {}


    if not values:
        print('No data found.')
    else:
        print('Worked - creating graph')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            #print('%s, %s, %s' % (row[2], str(float(row[18][1:].replace(',', ''))+float(row[19][1:].replace(',', ''))+float(row[20][1:].replace(',', ''))+float(row[21][1:].replace(',', ''))+float(row[22][1:].replace(',', ''))), str(float(row[18][1:].replace(',', '')))))
            budget[row[2]] = [str(float(row[18][1:].replace(',', ''))+float(row[19][1:].replace(',', ''))+float(row[20][1:].replace(',', ''))+float(row[21][1:].replace(',', ''))+float(row[22][1:].replace(',', ''))), str(float(row[19][1:].replace(',', '')))]


    # do the same for last year figures from same google sheets (sheet2)

    rangeName = 'Sheet2!A4:W368'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])

    lastYear = {}

    if not values:
        print('No data found.')
    else:
        # print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            #print('%s, %s, %s' % (row[2], str(float(row[18][1:].replace(',', ''))+float(row[19][1:].replace(',', ''))+float(row[20][1:].replace(',', ''))+float(row[21][1:].replace(',', ''))+float(row[22][1:].replace(',', ''))), str(float(row[18][1:].replace(',', '')))))
            lastYear[row[2]] = [str(float(row[18][1:].replace(',', ''))+float(row[19][1:].replace(',', ''))+float(row[20][1:].replace(',', ''))+float(row[21][1:].replace(',', ''))+float(row[22][1:].replace(',', ''))), str(float(row[14][1:].replace(',', '')))]


    #print(budget)
    return budget, lastYear

if __name__ == '__main__':
    spa_main()


def exp_main():
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '1gCzjBwVzXZ7Gdvs2QN4INrtTguvRB29tR7szQXh1_Vw'
    rangeName = 'Sheet1!A4:AG369'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])

    budget = {}


    if not values:
        print('No data found.')
    else:
        print('Worked - creating graph')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            #print('%s, %s, %s' % (row[2], str(float(row[18][1:].replace(',', ''))+float(row[19][1:].replace(',', ''))+float(row[20][1:].replace(',', ''))+float(row[21][1:].replace(',', ''))+float(row[22][1:].replace(',', ''))), str(float(row[18][1:].replace(',', '')))))
            budget[row[2]] = [str(float(row[18][1:].replace(',', ''))+float(row[19][1:].replace(',', ''))+float(row[20][1:].replace(',', ''))+float(row[21][1:].replace(',', ''))+float(row[22][1:].replace(',', ''))), str(float(row[20][1:].replace(',', '')))]


    # do the same for last year figures from same google sheets (sheet2)

    rangeName = 'Sheet2!A4:W368'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])

    lastYear = {}

    if not values:
        print('No data found.')
    else:
        # print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            #print('%s, %s, %s' % (row[2], str(float(row[18][1:].replace(',', ''))+float(row[19][1:].replace(',', ''))+float(row[20][1:].replace(',', ''))+float(row[21][1:].replace(',', ''))+float(row[22][1:].replace(',', ''))), str(float(row[18][1:].replace(',', '')))))
            lastYear[row[2]] = [str(float(row[18][1:].replace(',', ''))+float(row[19][1:].replace(',', ''))+float(row[20][1:].replace(',', ''))+float(row[21][1:].replace(',', ''))+float(row[22][1:].replace(',', ''))), str(float(row[15][1:].replace(',', '')))]


    #print(budget)
    return budget, lastYear

if __name__ == '__main__':
    exp_main()