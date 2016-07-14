from __future__ import print_function
import httplib2
import os
import time

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

def main(items):
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


    data = {'properties': {'title': 'LS Orders [%s]' % time.ctime()}}

    result = service.spreadsheets().create(body=data).execute()

    SHEET_ID = result['spreadsheetId']
    print('Created "%s"' % result['properties']['title'])

    data = {'values': [i for i in items]}

    service.spreadsheets().values().update(spreadsheetId=SHEET_ID,
    range='A1', body=data, valueInputOption='RAW').execute()

    spreadsheetId = '19dvS9Vhbv09wKQ4UQtBFJZqWfcwpnn4nTSpk_4c7hzg'
    rangeName = 'A2:A4'

    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()


if __name__ == '__main__':

    mylist = [['ID', 'Date', 'Performance', 'Total Price', 'Booking Fee', 'Commission Amount', 'No of Tickets', 'Meal Deal', 'Restaurant Price PP', 'Discounts', 'Platform', 'Restoration Levy'], [600552031, '2016-06-04 00:18', u'How the Other Half Loves', 16.75, 0.54, 1.75, 1, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552046, '2016-06-04 04:58', u'The Play That Goes Wrong', 89.0, 5.43, 0.0, 2, 'False', 'False', u'No Booking Fee', u'GT Play:Enta', 1.0], [600552064, '2016-06-04 06:48', u'Beautiful', 24.5, 1.93, 0.0, 1, 'False', 'False', u'Show of the Month', u'GT Play:Enta', 1.25], [600552069, '2016-06-04 07:03', u'The Fringe Comedy Awards Show', 110.0, 0.0, 0.0, 4, 'False', 'False', '', u'GT Play:Enta', 1.0], [600552077, '2016-06-04 07:08', u'Whose Line Is It Anyway?...Liv', 99.0, 0.0, 0.0, 2, u'M2C', u'10', u'Meal Deal Sale', u'GT Play:Enta', 1.5], [600552084, '2016-06-04 07:23', u'Sunny Afternoon', 84.5, 1.21, 4.25, 2, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552091, '2016-06-04 07:33', u'Les Mis\xe9rables', 176.5, 2.6, 8.75, 2, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552096, '2016-06-04 07:43', u'Beautiful', 94.5, 1.37, 4.75, 2, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552100, '2016-06-04 07:48', u'Stomp', 128.0, 2.3, 6.5, 2, 'False', 'False', '', u'GT Play:Enta', 0.0], [600552101, '2016-06-04 07:48', u'Beautiful', 49.0, 1.93, 0.0, 2, 'False', 'False', u'Show of the Month', u'GT Play:Enta', 1.25], [600552103, '2016-06-04 07:58', u'Jersey Boys', 55.0, 1.6, 5.5, 1, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552106, '2016-06-04 08:03', u'Matilda', 167.0, 0.0, 11.0, 2, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552109, '2016-06-04 08:08', u'The Lion King', 182.0, 0.0, 6.0, 4, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552111, '2016-06-04 08:08', u'Beautiful', 49.0, 1.93, 0.0, 2, 'False', 'False', u'Show of the Month', u'GT Play:Enta', 1.25], [600552113, '2016-06-04 08:13', u'Beautiful', 49.0, 1.93, 0.0, 2, 'False', 'False', u'Show of the Month', u'GT Play:Enta', 1.25], [600552117, '2016-06-04 08:18', u'Motown The Musical', 65.5, 0.94, 3.25, 2, 'False', 'False', '', u'GT Play:Enta', 1.2], [600552119, '2016-06-04 08:23', u'Titanic', 59.0, 3.68, 0.0, 2, 'False', 'False', u'No Added Fees +  Free Programme & Drink!', u'GT Play:Enta', 0.0], [600552120, '2016-06-04 08:23', u'Disney On Ice - Frozen ', 163.2, 0.0, 4.3, 4, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552121, '2016-06-04 08:28', u'Whose Line Is It Anyway?...Liv', 36.5, 0.0, 6.5, 1, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552122, '2016-06-04 08:28', u'Titanic', 35.0, 1.74, 0.0, 2, 'False', 'False', u'No Booking Fee', u'GT Play:Enta', 0.0], [600552124, '2016-06-04 08:33', u'The Book of Mormon', 199.0, 1.2, 4.25, 4, u'MD', u'8', u'Show Ticket +  Meal', u'GT Play:Enta', 1.25], [600552130, '2016-06-04 08:38', u'Aladdin', 121.0, 0.0, 8.0, 2, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552132, '2016-06-04 08:38', u'Kinky Boots', 37.25, 0.0, 4.75, 1, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552135, '2016-06-04 08:38', u'Mrs Henderson Presents', 34.5, 0.0, 2.25, 2, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552140, '2016-06-04 08:48', u'Sunny Afternoon', 100.0, 1.45, 5.0, 2, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552141, '2016-06-04 08:48', u'The Railway Children', 55.5, 0.96, 2.75, 2, 'False', 'False', '', u'GT Play:Enta', 1.0], [600552146, '2016-06-04 08:48', u'Ideal Home Show', 15.0, 1.37, 0.0, 1, 'False', 'False', '', u'GT Play:Enta', 0.0], [600552149, '2016-06-04 08:53', u'How the Other Half Loves', 20.0, 1.7, 0.0, 2, 'False', 'False', u'Special Offer', u'GT Play:Enta', 1.5], [600552162, '2016-06-04 09:08', u'The Railway Children', 55.5, 0.96, 2.75, 2, 'False', 'False', '', u'GT Play:Enta', 1.0], [600552165, '2016-06-04 09:13', u'The Railway Children', 83.25, 0.96, 2.75, 3, 'False', 'False', '', u'GT Play:Enta', 1.0], [600552166, '2016-06-04 09:13', u'West End Comedy Club Grace', 56.0, 0.0, 3.0, 7, 'False', 'False', u'Exclusive: \xa37 off', u'GT Play:Enta', 0.0], [600552175, '2016-06-04 09:23', u'Jersey Boys', 70.0, 3.35, 0.0, 2, 'False', 'False', u'Fathers Day Sale', u'GT Play:Enta', 1.5], [600552177, '2016-06-04 09:23', u'Sunny Afternoon', 40.0, 0.55, 2.0, 2, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552180, '2016-06-04 09:23', u'Funny Girl', 82.5, 0.78, 2.5, 3, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552181, '2016-06-04 09:28', u'The Play That Goes Wrong', 44.8, 0.63, 2.4, 2, 'False', 'False', '', u'GT Play:Enta', 1.0], [600552182, '2016-06-04 09:28', u'Show Boat \t\t\t\t\t\t', 39.0, 3.0, 0.0, 2, 'False', 'False', u'No Booking Fee', u'GT Play:Enta', 1.5], [600552188, '2016-06-04 09:28', u'Beautiful', 49.0, 1.93, 0.0, 2, 'False', 'False', u'Show of the Month', u'GT Play:Enta', 1.25], [600552189, '2016-06-04 09:33', u'Marvel Universe LIVE!', 72.2, 0.0, 4.6, 2, 'False', 'False', '', u'GT Play:Enta', 0.0], [600552195, '2016-06-04 09:33', u'Charlie Chocolate Factory', 150.0, 7.37, 0.0, 2, 'False', 'False', u'No Booking Fee', u'GT Play:Enta', 1.25], [600552197, '2016-06-04 09:43', u'Beautiful', 122.5, 1.93, 0.0, 5, 'False', 'False', u'Show of the Month', u'GT Play:Enta', 1.25], [600552205, '2016-06-04 09:38', u'Mrs Henderson Presents', 20.0, 1.09, 0.0, 2, 'False', 'False', u'May Fever Sale', u'GT Play:Enta', 1.25], [600552210, '2016-06-04 09:43', u'The Lion King', 152.0, 2.27, 6.5, 2, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552223, '2016-06-04 09:48', u'In the Heights', 65.0, 3.25, 0.0, 2, u'MD', u'7', u'Show + Free Meal', u'GT Play:Enta', 0.0], [600552225, '2016-06-04 09:53', u'Merchants of Bollywood', 40.5, 1.68, 0.0, 3, 'False', 'False', u'Special Offer', u'GT Play:Enta', 0.0], [600552231, '2016-06-04 09:58', u'Guys & Dolls - Phoenix Theatre', 110.0, 1.6, 5.5, 2, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552233, '2016-06-04 10:03', u'Wicked', 35.0, 2.36, 0.0, 2, 'False', 'False', u'No Booking Fee', u'GT Play:Enta', 1.75], [600552234, '2016-06-04 09:58', u'Sunny Afternoon', 62.0, 0.88, 3.0, 2, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552236, '2016-06-04 10:03', u'Aladdin', 224.0, 0.0, 14.5, 2, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552245, '2016-06-04 10:08', u'Beautiful', 73.5, 1.93, 0.0, 3, 'False', 'False', u'Show of the Month', u'GT Play:Enta', 1.25], [600552246, '2016-06-04 10:13', u'1984 The Play', 66.0, 0.73, 2.16, 3, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552248, '2016-06-04 10:13', u'Mamma Mia!', 79.0, 3.18, 0.0, 2, u'MD', u'7', u'Meal Deal', u'GT Play:Enta', 1.25], [600552249, '2016-06-04 10:13', u'The Lion King', 364.0, 1.54, 4.5, 7, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552250, '2016-06-04 10:13', u'Beautiful', 49.0, 1.93, 0.0, 2, 'False', 'False', u'Show of the Month', u'GT Play:Enta', 1.25], [600552251, '2016-06-04 10:13', u'The Book of Mormon', 83.0, 1.2, 4.0, 2, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552253, '2016-06-04 10:23', u'Beautiful', 49.0, 1.93, 0.0, 2, 'False', 'False', u'Show of the Month', u'GT Play:Enta', 1.25], [600552254, '2016-06-04 10:13', u'Merchants of Bollywood', 45.0, 2.81, 0.0, 2, 'False', 'False', u'Special Offer', u'GT Play:Enta', 0.0], [600552256, '2016-06-04 10:18', u'The Book of Mormon', 124.5, 1.2, 4.0, 3, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552259, '2016-06-04 10:23', u'Curious Incident Dog Nighttime', 18.0, 2.79, 0.0, 1, 'False', 'False', u'No Booking Fee', u'GT Play:Enta', 1.25], [600552265, '2016-06-04 10:23', u'Kinky Boots', 111.75, 0.0, 4.75, 3, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552269, '2016-06-04 10:33', u'Sunny Afternoon', 80.0, 0.55, 2.0, 4, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552270, '2016-06-04 10:33', u'Beautiful', 49.0, 1.93, 0.0, 2, 'False', 'False', u'Show of the Month', u'GT Play:Enta', 1.25], [600552274, '2016-06-04 10:38', u'Charlie Chocolate Factory', 150.0, 7.37, 0.0, 2, 'False', 'False', u'No Booking Fee', u'GT Play:Enta', 1.25], [600552275, '2016-06-04 10:43', u'The Book of Mormon', 94.5, 0.0, 4.75, 2, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552276, '2016-06-04 10:38', u'Titanic', 59.0, 3.68, 0.0, 2, 'False', 'False', u'No Added Fees +  Free Programme & Drink!', u'GT Play:Enta', 0.0], [600552281, '2016-06-04 10:48', u'Wicked', 114.0, 0.0, 7.5, 2, 'False', 'False', '', u'GT Play:Enta', 1.75], [600552286, '2016-06-04 10:58', u'Guys & Dolls - Phoenix Theatre', 49.0, 2.3, 0.0, 2, 'False', 'False', u'No Added Fees', u'GT Play:Enta', 1.5], [600552289, '2016-06-04 10:58', u'Show Boat \t\t\t\t\t\t', 78.0, 3.0, 0.0, 4, 'False', 'False', u'No Booking Fee', u'GT Play:Enta', 1.5], [600552290, '2016-06-04 10:58', u'HMS Pinafore', 52.0, 1.76, 0.0, 4, 'False', 'False', u'Discounted Ticket', u'GT Play:Enta', 1.25], [600552292, '2016-06-04 11:03', u'Jersey Boys', 108.0, 0.76, 2.5, 4, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552293, '2016-06-04 11:03', u'The Play That Goes Wrong', 130.0, 7.99, 0.0, 2, 'False', 'False', u'No Booking Fee', u'GT Play:Enta', 1.0], [600552296, '2016-06-04 11:08', u'Covent Garden Comedy Club', 160.0, 0.0, 2.0, 8, u'MD', u'8', u'Show Ticket + Meal', u'GT Play:Enta', 0.0], [600552298, '2016-06-04 11:08', u'Sunny Afternoon', 100.0, 0.55, 2.0, 5, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552299, '2016-06-04 11:08', u'Charlie Chocolate Factory', 118.5, 3.82, 0.0, 3, 'False', 'False', u'No Booking Fee', u'GT Play:Enta', 1.25], [600552300, '2016-06-04 11:08', u'Udderbelly - Closer by Circa ', 110.4, 0.0, 3.6, 4, 'False', 'False', '', u'GT Play:Enta', 0.0], [600552302, '2016-06-04 11:13', u'The Railway Children', 55.5, 0.96, 2.75, 2, 'False', 'False', '', u'GT Play:Enta', 1.0], [600552304, '2016-06-04 11:18', u'How the Other Half Loves', 33.5, 0.54, 1.75, 2, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552307, '2016-06-04 11:18', u'Jersey Boys', 241.5, 2.36, 8.0, 3, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552309, '2016-06-04 11:18', u'The Book of Mormon', 105.5, 1.54, 5.25, 2, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552313, '2016-06-04 11:23', u'Doctor Faustus', 130.0, 12.7, 0.0, 2, 'False', 'False', u'No Booking Fee', u'GT Play:Enta', 1.5], [600552319, '2016-06-04 11:33', u'Show Boat \t\t\t\t\t\t', 39.0, 3.0, 0.0, 2, 'False', 'False', u'No Booking Fee', u'GT Play:Enta', 1.5], [600552321, '2016-06-04 11:28', u'No Villain', 66.5, 0.96, 3.25, 2, 'False', 'False', '', u'GT Play:Enta', 1.0], [600552329, '2016-06-04 11:38', u'The 99 Club', 41.0, 0.0, 2.5, 2, 'False', 'False', '', u'GT Play:Enta', 0.0], [600552331, '2016-06-04 11:43', u'Merchants of Bollywood', 67.5, 1.68, 0.0, 5, 'False', 'False', u'Special Offer', u'GT Play:Enta', 0.0], [600552336, '2016-06-04 11:43', u'Guys & Dolls - Phoenix Theatre', 136.25, 0.76, 2.75, 5, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552338, '2016-06-04 11:48', u'Wicked', 91.0, 0.0, 6.0, 2, 'False', 'False', '', u'GT Play:Enta', 1.75], [600552341, '2016-06-04 11:48', u'Wicked', 35.0, 2.36, 0.0, 2, 'False', 'False', u'No Booking Fee', u'GT Play:Enta', 1.75], [600552346, '2016-06-04 11:53', u'Phantom of the Opera', 239.25, 0.0, 10.25, 3, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552349, '2016-06-04 11:58', u'Wicked', 136.5, 0.0, 6.0, 3, 'False', 'False', '', u'GT Play:Enta', 1.75], [600552350, '2016-06-04 11:53', u'Mrs Henderson Presents', 10.0, 1.09, 0.0, 1, 'False', 'False', u'May Fever Sale', u'GT Play:Enta', 1.25], [600552353, '2016-06-04 11:58', u'American Idiot', 50.0, 2.5, 0.0, 2, u'MD', u'10', u'Show Ticket + Free Meal', u'GT Play:Enta', 0.0], [600552354, '2016-06-04 11:58', u'Wicked', 160.0, 0.0, 10.5, 2, 'False', 'False', '', u'GT Play:Enta', 1.75], [600552355, '2016-06-04 12:03', u'The Comedy About A Bank Robber', 33.5, 0.46, 1.75, 2, 'False', 'False', '', u'GT Play:Enta', 1.0], [600552357, '2016-06-04 11:58', u'Charlie Chocolate Factory', 17.5, 1.62, 0.0, 1, 'False', 'False', u'No Booking Fees!', u'GT Play:Enta', 1.25], [600552359, '2016-06-04 12:03', u'The Dreamboys Cardiff', 45.0, 6.75, 0.0, 1, 'False', 'False', u'2 for 1', u'GT Play:Enta', 0.0], [600552360, '2016-06-04 12:03', u'Guys & Dolls - Phoenix Theatre', 211.0, 3.11, 10.5, 2, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552361, '2016-06-04 12:08', u'Beautiful', 157.5, 4.27, 0.0, 3, 'False', 'False', u'Show of the Month: No Booking Fee', u'GT Play:Enta', 1.25], [600552362, '2016-06-04 12:08', u'Disney On Ice - Frozen ', 81.6, 0.0, 4.3, 2, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552363, '2016-06-04 12:08', u'Mrs Henderson Presents', 20.0, 1.09, 0.0, 2, 'False', 'False', u'May Fever Sale', u'GT Play:Enta', 1.25], [600552365, '2016-06-04 12:08', u'Mrs Henderson Presents', 20.0, 1.09, 0.0, 2, 'False', 'False', u'May Fever Sale', u'GT Play:Enta', 1.25], [600552366, '2016-06-04 12:13', u'Mrs Henderson Presents', 20.0, 1.09, 0.0, 2, 'False', 'False', u'May Fever Sale', u'GT Play:Enta', 1.25], [600552369, '2016-06-04 12:18', u'Wicked', 17.5, 2.36, 0.0, 1, 'False', 'False', u'No Booking Fee', u'GT Play:Enta', 1.75], [600552371, '2016-06-04 12:28', u'Kinky Boots', 22.5, 0.0, 3.0, 1, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552372, '2016-06-04 12:23', u'Whose Line Is It Anyway?...Liv', 73.0, 0.0, 6.5, 2, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552373, '2016-06-04 12:28', u'Kinky Boots', 45.0, 0.0, 3.0, 2, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552379, '2016-06-04 12:28', u'The Book of Mormon', 83.5, 1.2, 4.25, 2, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552381, '2016-06-04 12:33', u'Motown The Musical', 65.5, 0.94, 3.25, 2, 'False', 'False', '', u'GT Play:Enta', 1.2], [600552386, '2016-06-04 12:38', u'Wicked', 135.0, 6.57, 0.0, 2, u'MD', u'7', u'Show +  Free Meal', u'GT Play:Enta', 1.75], [600552390, '2016-06-04 12:48', u'Beautiful', 73.5, 1.93, 0.0, 3, 'False', 'False', u'Show of the Month', u'GT Play:Enta', 1.25], [600552394, '2016-06-04 12:48', u'Guys & Dolls - Phoenix Theatre', 54.5, 0.76, 2.75, 2, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552395, '2016-06-04 12:48', u'Beautiful', 105.0, 4.27, 0.0, 2, 'False', 'False', u'Show of the Month: No Booking Fee', u'GT Play:Enta', 1.25], [600552397, '2016-06-04 12:58', u'Mamma Mia!', 55.5, 0.79, 2.75, 2, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552399, '2016-06-04 13:03', u'Matilda', 131.0, 0.0, 7.0, 2, u'MD', u'11', u'Show Ticket +  Meal', u'GT Play:Enta', 1.5], [600552400, '2016-06-04 12:58', u'Show Boat \t\t\t\t\t\t', 114.0, 0.0, 7.5, 2, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552402, '2016-06-04 12:58', u'Kinky Boots', 74.5, 0.0, 4.75, 2, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552406, '2016-06-04 13:03', u'Matilda', 172.0, 0.0, 5.5, 4, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552420, '2016-06-04 13:13', u'Crack Comedy Club - SB', 20.0, 3.0, 0.0, 2, 'False', 'False', '', u'GT Play:Enta', 0.0], [600552423, '2016-06-04 13:18', u'Beautiful', 105.0, 4.27, 0.0, 2, 'False', 'False', u'Show of the Month: No Booking Fee', u'GT Play:Enta', 1.25], [600552425, '2016-06-04 13:18', u'Funny Girl', 315.0, 2.33, 7.25, 4, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552428, '2016-06-04 13:23', u'Moscow State Circus', 60.0, 0.0, 1.0, 4, 'False', 'False', u'Save \xa315', u'GT Play:Enta', 0.0], [600552431, '2016-06-04 13:23', u'Covent Garden Comedy Club', 36.0, 0.0, 2.0, 2, 'False', 'False', '', u'GT Play:Enta', 0.0], [600552432, '2016-06-04 13:28', u'Whose Line Is It Anyway?...Liv', 84.5, 0.0, 7.25, 2, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552434, '2016-06-04 13:28', u'Boat Show The Tattershall ', 51.0, 0.0, 2.0, 2, u'MD', u'7', u'Show Ticket plus Meal', u'GT Play:Enta', 0.0], [600552435, '2016-06-04 13:33', u'Aladdin', 308.0, 2.27, 7.5, 4, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552437, '2016-06-04 13:38', u'Wicked', 91.0, 0.0, 6.0, 2, 'False', 'False', '', u'GT Play:Enta', 1.75], [600552442, '2016-06-04 13:43', u'The Book of Mormon', 60.0, 3.59, 0.0, 2, 'False', 'False', u'No Booking Fee', u'GT Play:Enta', 1.25], [600552444, '2016-06-04 13:48', u'The Lion King', 166.5, 0.0, 10.75, 2, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552446, '2016-06-04 13:48', u'Kinky Boots', 139.0, 8.5, 0.0, 2, 'False', 'False', u'No Booking Fee', u'GT Play:Enta', 1.5], [600552451, '2016-06-04 13:58', u'The View from The Shard', 99.8, 3.98, 0.0, 4, 'False', 'False', '', u'GT Play:Enta', 0.0], [600552452, '2016-06-04 13:53', u'The Lion King', 186.0, 1.37, 4.0, 4, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552454, '2016-06-04 13:53', u'Wicked', 91.0, 0.0, 6.0, 2, 'False', 'False', '', u'GT Play:Enta', 1.75], [600552455, '2016-06-04 13:58', u'The Lion King', 232.5, 1.37, 4.0, 5, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552459, '2016-06-04 14:08', u'Moscow State Circus', 45.0, 0.0, 1.0, 3, 'False', 'False', u'Save \xa315', u'GT Play:Enta', 0.0], [600552461, '2016-06-04 13:58', u'Charlie Chocolate Factory', 130.0, 3.12, 0.0, 4, 'False', 'False', u'No Booking Fees!', u'GT Play:Enta', 1.25], [600552464, '2016-06-04 14:08', u'Beautiful', 49.0, 1.93, 0.0, 2, 'False', 'False', u'Show of the Month', u'GT Play:Enta', 1.25], [600552466, '2016-06-04 14:08', u'Kinky Boots', 74.5, 0.0, 4.75, 2, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552467, '2016-06-04 14:08', u'Kinky Boots', 22.5, 0.0, 3.0, 1, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552474, '2016-06-04 14:13', u'Merchants of Bollywood', 27.0, 1.68, 0.0, 2, 'False', 'False', u'Special Offer', u'GT Play:Enta', 0.0], [600552475, '2016-06-04 14:18', u'Boat Show The Tattershall ', 234.0, 0.0, 2.0, 9, u'MD', u'8', u'Show Ticket plus Meal', u'GT Play:Enta', 0.0], [600552476, '2016-06-04 14:18', u'Beautiful', 49.0, 1.93, 0.0, 2, 'False', 'False', u'Show of the Month', u'GT Play:Enta', 1.25], [600552477, '2016-06-04 14:18', u'How the Other Half Loves', 20.0, 1.7, 0.0, 2, 'False', 'False', u'Special Offer', u'GT Play:Enta', 1.5], [600552481, '2016-06-04 14:23', u'The Spoils', 119.0, 11.55, 0.0, 2, 'False', 'False', u'No Booking Fee', u'GT Play:Enta', 1.75], [600552482, '2016-06-04 14:23', u'Charlie Chocolate Factory', 17.5, 1.62, 0.0, 1, 'False', 'False', u'No Booking Fees!', u'GT Play:Enta', 1.25], [600552484, '2016-06-04 14:33', u'Sunny Afternoon', 80.0, 0.55, 2.0, 4, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552485, '2016-06-04 14:33', u'Jersey Boys', 99.0, 3.16, 2.0, 2, u'MD', u'8', u'Show tickets plus Meal!', u'GT Play:Enta', 1.5], [600552486, '2016-06-04 14:33', u'Wicked', 35.0, 2.36, 0.0, 2, 'False', 'False', u'No Booking Fee', u'GT Play:Enta', 1.75], [600552490, '2016-06-04 14:48', u'Beautiful', 49.0, 1.93, 0.0, 2, 'False', 'False', u'Show of the Month', u'GT Play:Enta', 1.25], [600552491, '2016-06-04 14:43', u'Mamma Mia!', 79.0, 3.18, 0.0, 2, u'MD', u'7', u'Meal Deal', u'GT Play:Enta', 1.25], [600552493, '2016-06-04 14:48', u'Udderbelly - Brainiac Live!', 45.0, 2.25, 0.0, 3, 'False', 'False', u'Discounted Ticket', u'GT Play:Enta', 0.0], [600552494, '2016-06-04 14:48', u'Les Mis\xe9rables', 155.0, 2.27, 8.0, 2, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552500, '2016-06-04 14:58', u'Wicked', 35.0, 2.36, 0.0, 2, 'False', 'False', u'No Booking Fee', u'GT Play:Enta', 1.75], [600552507, '2016-06-04 15:08', u'The Lion King', 155.0, 2.54, 0.0, 2, u'MD', u'8', u'Show Ticket + Free Meal', u'GT Play:Enta', 1.25], [600552508, '2016-06-04 15:13', u'Beautiful', 49.0, 1.93, 0.0, 2, 'False', 'False', u'Show of the Month', u'GT Play:Enta', 1.25], [600552511, '2016-06-04 15:08', u'Covent Garden Comedy Club', 80.0, 0.0, 2.0, 4, 'False', 'False', '', u'GT Play:Enta', 0.0], [600552512, '2016-06-04 15:13', u'Motown The Musical', 259.5, 3.96, 9.75, 2, 'False', 'False', '', u'GT Play:Enta', 1.2], [600552519, '2016-06-04 15:28', u'Wicked', 55.0, 3.86, 0.0, 2, 'False', 'False', u'No Booking Fee', u'GT Play:Enta', 1.75], [600552527, '2016-06-04 15:43', u'Motown The Musical', 65.5, 0.94, 3.25, 2, 'False', 'False', '', u'GT Play:Enta', 1.2], [600552529, '2016-06-04 15:43', u'Wicked', 270.0, 6.57, 0.0, 4, u'M2C', u'12', u'Meal Deal', u'GT Play:Enta', 1.75], [600552530, '2016-06-04 15:48', u'The Bodyguard', 155.0, 0.0, 10.0, 2, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552532, '2016-06-04 15:53', u'Merchants of Bollywood', 45.0, 2.81, 0.0, 2, 'False', 'False', u'Special Offer', u'GT Play:Enta', 0.0], [600552539, '2016-06-04 15:58', u'Les Mis\xe9rables', 176.5, 2.6, 8.75, 2, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552541, '2016-06-04 16:08', u'Beautiful', 290.0, 5.93, 0.0, 4, 'False', 'False', u'Show of the Month: No Booking Fee', u'GT Play:Enta', 1.25], [600552543, '2016-06-04 16:08', u'Funny Girl', 27.5, 0.78, 2.5, 1, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552556, '2016-06-04 16:23', u'Curious Incident Dog Nighttime', 60.0, 0.55, 2.0, 3, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552559, '2016-06-04 16:28', u'In the Heights', 25.25, 0.9, 2.75, 1, 'False', 'False', '', u'GT Play:Enta', 0.0], [600552560, '2016-06-04 16:28', u'Wicked', 91.0, 0.0, 6.0, 2, 'False', 'False', '', u'GT Play:Enta', 1.75], [600552564, '2016-06-04 16:33', u'Covent Garden Comedy Club', 40.0, 0.0, 2.0, 2, u'MD', u'8', u'Show Ticket + Meal', u'GT Play:Enta', 0.0], [600552575, '2016-06-04 16:48', u'Merchants of Bollywood', 27.0, 1.68, 0.0, 2, 'False', 'False', u'Special Offer', u'GT Play:Enta', 0.0], [600552576, '2016-06-04 16:58', u'Jersey Boys', 139.0, 4.83, 2.0, 2, u'MD', u'8', u'Show tickets plus Meal!', u'GT Play:Enta', 1.5], [600552579, '2016-06-04 16:53', u'Motown The Musical', 84.0, 0.94, 3.25, 2, u'MD', u'9', u'Show Ticket + Meal', u'GT Play:Enta', 1.2], [600552580, '2016-06-04 16:53', u'The Lion King', 260.0, 1.54, 4.5, 5, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552581, '2016-06-04 16:53', u'The Lion King', 155.0, 2.54, 0.0, 2, u'MD', u'8', u'Show Ticket + Free Meal', u'GT Play:Enta', 1.25], [600552583, '2016-06-04 16:58', u'Thriller Live', 126.0, 5.12, 0.0, 3, 'False', 'False', u'Special Offer', u'GT Play:Enta', 1.0], [600552591, '2016-06-04 17:08', u'In the Heights', 65.0, 3.25, 0.0, 2, u'MD', u'7', u'Show + Free Meal', u'GT Play:Enta', 0.0], [600552592, '2016-06-04 17:03', u'Kinky Boots', 148.5, 6.0, 0.0, 3, 'False', 'False', u'No Booking Fee', u'GT Play:Enta', 1.5], [600552595, '2016-06-04 17:08', u'Show Boat \t\t\t\t\t\t', 45.0, 0.0, 3.0, 2, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552596, '2016-06-04 17:03', u'Mrs Henderson Presents', 20.0, 1.09, 0.0, 2, 'False', 'False', u'May Fever Sale', u'GT Play:Enta', 1.25], [600552599, '2016-06-04 17:08', u'Funny Girl', 27.5, 0.78, 2.5, 1, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552601, '2016-06-04 17:08', u'The Lion King', 55.5, 4.0, 2.75, 2, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552605, '2016-06-04 17:13', u'Beautiful', 130.0, 0.0, 0.0, 4, u'MD', u'9', u'Show Ticket + Free Meal', u'GT Play:Enta', 1.25], [600552609, '2016-06-04 17:23', u'Moscow State Circus', 30.0, 0.0, 1.0, 2, 'False', 'False', u'Save \xa315', u'GT Play:Enta', 0.0], [600552612, '2016-06-04 17:33', u'The Dreamboys Brighton', 90.0, 6.75, 0.0, 2, 'False', 'False', u'lastminute.com 2 for 1 OFFER PRICE', u'GT Play:Enta', 0.0], [600552613, '2016-06-04 17:33', u'Mamma Mia!', 79.0, 3.18, 0.0, 2, u'MD', u'8', u'Meal Deal', u'GT Play:Enta', 1.25], [600552614, '2016-06-04 17:38', u'The Suicide', 30.0, 2.25, 0.0, 2, 'False', 'False', u'Discounted Ticket', u'GT Play:Enta', 0.0], [600552616, '2016-06-04 17:33', u'How the Other Half Loves', 62.5, 1.06, 3.25, 2, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552622, '2016-06-04 17:38', u'Motown The Musical', 65.5, 0.94, 3.25, 2, 'False', 'False', '', u'GT Play:Enta', 1.2], [600552628, '2016-06-04 17:48', u'Jackie The Musical', 61.5, 3.1, 1.25, 2, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552629, '2016-06-04 17:48', u'Les Mis\xe9rables', 156.8, 1.12, 4.2, 4, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552632, '2016-06-04 17:48', u'Show Boat \t\t\t\t\t\t', 39.5, 2.28, 0.0, 2, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552634, '2016-06-04 17:53', u'Funny Girl', 87.0, 1.26, 4.0, 2, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552635, '2016-06-04 17:53', u'Curious Incident Dog Nighttime', 94.5, 1.37, 4.75, 2, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552641, '2016-06-04 17:58', u'The Book of Mormon', 99.5, 1.2, 4.25, 2, u'MD', u'8', u'Show Ticket +  Meal', u'GT Play:Enta', 1.25], [600552645, '2016-06-04 17:58', u'Jersey Boys', 70.0, 3.35, 0.0, 2, 'False', 'False', u'Fathers Day Sale', u'GT Play:Enta', 1.5], [600552648, '2016-06-04 18:03', u'Motown The Musical', 44.0, 0.61, 2.5, 2, 'False', 'False', '', u'GT Play:Enta', 1.2], [600552649, '2016-06-04 18:13', u'Jersey Boys', 53.0, 0.76, 2.0, 2, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552650, '2016-06-04 18:08', u'Jersey Boys', 70.0, 3.35, 0.0, 2, 'False', 'False', u'Fathers Day Sale', u'GT Play:Enta', 1.5], [600552652, '2016-06-04 18:13', u'Disney On Ice - Frozen ', 96.75, 0.0, 4.25, 3, 'False', 'False', '', u'GT Play:Enta', 0.0], [600552653, '2016-06-04 18:13', u'In the Heights', 65.0, 3.25, 0.0, 2, u'MD', u'7', u'Show + Free Meal', u'GT Play:Enta', 0.0], [600552656, '2016-06-04 18:18', u'Kinky Boots', 51.5, 0.0, 3.25, 2, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552659, '2016-06-04 18:18', u"Hobson's Choice", 55.5, 0.95, 2.75, 2, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552661, '2016-06-04 18:28', u'Mrs Henderson Presents', 10.0, 1.09, 0.0, 1, 'False', 'False', u'May Fever Sale', u'GT Play:Enta', 1.25], [600552662, '2016-06-04 18:33', u'Mamma Mia!', 88.0, 1.27, 4.5, 2, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552663, '2016-06-04 18:33', u'In the Heights', 50.5, 0.9, 2.75, 2, 'False', 'False', '', u'GT Play:Enta', 0.0], [600552664, '2016-06-04 18:33', u'Jackie The Musical', 168.75, 3.43, 1.25, 5, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552665, '2016-06-04 18:38', u'Impossible', 80.0, 2.34, 0.0, 4, 'False', 'False', u'No Booking Fee', u'GT Play:Enta', 1.25], [600552670, '2016-06-04 18:38', u'Wicked', 272.5, 0.0, 7.0, 5, 'False', 'False', '', u'GT Play:Enta', 1.75], [600552671, '2016-06-04 18:38', u'Les Mis\xe9rables', 176.5, 2.6, 8.75, 2, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552673, '2016-06-04 18:43', u'Show Boat \t\t\t\t\t\t', 45.0, 0.0, 3.0, 2, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552674, '2016-06-04 18:48', u'How the Other Half Loves', 20.0, 1.7, 0.0, 2, 'False', 'False', u'Special Offer', u'GT Play:Enta', 1.5], [600552680, '2016-06-04 18:53', u'The Book of Mormon', 55.0, 3.28, 0.0, 2, 'False', 'False', u'No Booking Fee', u'GT Play:Enta', 1.25], [600552685, '2016-06-04 18:58', u'Curious Incident Dog Nighttime', 40.0, 0.0, 2.0, 2, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552686, '2016-06-04 18:58', u"Hobson's Choice", 55.0, 2.62, 0.0, 2, u'MD', u'11', u'Show Ticket + Free Meal!', u'GT Play:Enta', 1.25], [600552687, '2016-06-04 19:08', u'The Play That Goes Wrong', 89.6, 0.63, 2.4, 4, 'False', 'False', '', u'GT Play:Enta', 1.0], [600552690, '2016-06-04 19:03', u'Charlie Chocolate Factory', 47.0, 2.22, 0.0, 2, 'False', 'False', u'No Booking Fee', u'GT Play:Enta', 1.25], [600552693, '2016-06-04 19:13', u'Charlie Chocolate Factory', 70.0, 1.62, 0.0, 4, 'False', 'False', u'No Booking Fees!', u'GT Play:Enta', 1.25], [600552695, '2016-06-04 19:18', u'Charlie Chocolate Factory', 17.5, 1.62, 0.0, 1, 'False', 'False', u'No Booking Fees!', u'GT Play:Enta', 1.25], [600552700, '2016-06-04 19:28', u'Aladdin', 150.0, 2.2, 7.5, 2, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552701, '2016-06-04 19:28', u'Wicked', 35.0, 2.36, 0.0, 2, 'False', 'False', u'No Booking Fee', u'GT Play:Enta', 1.75], [600552703, '2016-06-04 19:38', u"Hobson's Choice", 25.0, 2.37, 0.0, 1, u'MD', u'8', u'Show Ticket + Free Meal!', u'GT Play:Enta', 1.25], [600552711, '2016-06-04 19:43', u'The Book of Mormon', 111.0, 1.62, 5.5, 2, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552730, '2016-06-04 20:08', u'Wicked', 82.5, 3.86, 0.0, 3, 'False', 'False', u'No Booking Fee', u'GT Play:Enta', 1.75], [600552736, '2016-06-04 20:03', u'The Lion King', 223.5, 4.88, 0.0, 3, u'MD', u'8', u'Show Ticket + Free Meal!', u'GT Play:Enta', 1.25], [600552737, '2016-06-04 20:08', u'Jersey Boys', 161.0, 2.36, 8.0, 2, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552739, '2016-06-04 20:08', u'The Dreamboys Brighton', 90.0, 6.75, 0.0, 2, 'False', 'False', u'lastminute.com 2 for 1 OFFER PRICE', u'GT Play:Enta', 0.0], [600552741, '2016-06-04 20:18', u'The Dreamboys Bournemouth', 180.0, 6.75, 0.0, 4, 'False', 'False', u'2 for 1', u'GT Play:Enta', 0.0], [600552743, '2016-06-04 20:18', u'Charlie Chocolate Factory', 50.0, 2.37, 0.0, 2, 'False', 'False', u'No Booking Fees!', u'GT Play:Enta', 1.25], [600552745, '2016-06-04 20:18', u'Beautiful', 73.5, 1.93, 0.0, 3, 'False', 'False', u'Show of the Month', u'GT Play:Enta', 1.25], [600552751, '2016-06-04 20:23', u'Wicked', 40.0, 0.63, 2.5, 2, 'False', 'False', '', u'GT Play:Enta', 1.75], [600552753, '2016-06-04 20:23', u'The Book of Mormon', 111.0, 1.62, 5.5, 2, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552760, '2016-06-04 20:28', u'Sh*t-faced Shakespeare', 63.0, 0.0, 2.5, 3, 'False', 'False', '', u'GT Play:Enta', 0.0], [600552763, '2016-06-04 20:38', u'Aladdin', 104.0, 0.0, 7.0, 2, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552770, '2016-06-04 20:48', u'Kinky Boots', 74.5, 0.0, 4.75, 2, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552773, '2016-06-04 20:58', u'Thriller Live', 115.5, 0.88, 3.0, 3, u'MD', u'8', u'Show Ticket +  Meal', u'GT Play:Enta', 1.0], [600552784, '2016-06-04 21:08', u'Kinky Boots', 148.5, 6.0, 0.0, 3, 'False', 'False', u'No Booking Fee', u'GT Play:Enta', 1.5], [600552798, '2016-06-04 21:23', u'Whose Line Is It Anyway?...Liv', 99.0, 0.0, 0.0, 2, u'MD', u'7', u'Meal Deal Sale', u'GT Play:Enta', 1.5], [600552804, '2016-06-04 21:28', u'Wicked', 35.0, 2.36, 0.0, 2, 'False', 'False', u'No Booking Fee', u'GT Play:Enta', 1.75], [600552808, '2016-06-04 21:33', u'Kinky Boots', 91.0, 0.0, 6.0, 2, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552811, '2016-06-04 21:33', u'Whose Line Is It Anyway?...Liv', 99.0, 0.0, 0.0, 2, u'MD', u'10', u'Meal Deal Sale', u'GT Play:Enta', 1.5], [600552813, '2016-06-04 21:33', u'The Play That Goes Wrong', 70.0, 4.24, 0.0, 2, 'False', 'False', u'No Booking Fee', u'GT Play:Enta', 1.0], [600552814, '2016-06-04 21:38', u'Buckingham Palace Gallery', 20.6, 1.71, 0.0, 2, 'False', 'False', '', u'GT Play:Enta', 0.0], [600552817, '2016-06-04 21:43', u'Jack the Ripper - WT5', 14.0, 1.75, 0.0, 2, 'False', 'False', '', u'GT Play:Enta', 0.0], [600552826, '2016-06-04 21:53', u'Wicked', 17.5, 2.36, 0.0, 1, 'False', 'False', u'No Booking Fee', u'GT Play:Enta', 1.75], [600552828, '2016-06-04 21:58', u'Aladdin', 95.0, 1.37, 5.0, 2, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552831, '2016-06-04 22:03', u'Curious Incident Dog Nighttime', 36.0, 2.79, 0.0, 2, 'False', 'False', u'No Booking Fee', u'GT Play:Enta', 1.25], [600552834, '2016-06-04 22:08', u'Sunny Afternoon', 49.5, 0.45, 1.5, 3, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552835, '2016-06-04 22:08', u'The Raunch', 30.0, 2.0, 0.0, 3, 'False', 'False', u'Discounted Ticket', u'GT Play:Enta', 0.0], [600552837, '2016-06-04 22:13', u'Aladdin', 110.0, 1.6, 5.5, 2, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552838, '2016-06-04 22:23', u'Jersey Boys', 140.0, 3.35, 0.0, 4, 'False', 'False', u'Fathers Day Sale', u'GT Play:Enta', 1.5], [600552839, '2016-06-04 22:23', u'How the Other Half Loves', 85.0, 8.2, 0.0, 2, 'False', 'False', u'Special Offer', u'GT Play:Enta', 1.5], [600552840, '2016-06-04 22:28', u'The Lion King', 57.5, 0.0, 3.75, 2, 'False', 'False', '', u'GT Play:Enta', 1.25], [600552843, '2016-06-04 22:43', u'Jersey Boys', 165.0, 1.6, 5.5, 3, 'False', 'False', '', u'GT Play:Enta', 1.5], [600552849, '2016-06-04 22:43', u'Kinky Boots', 118.5, 4.75, 0.0, 3, 'False', 'False', u'No Booking Fee', u'GT Play:Enta', 1.5], [600552853, '2016-06-04 22:48', u'The Lion King', 149.0, 4.88, 0.0, 2, u'MD', u'8', u'Show Ticket + Free Meal!', u'GT Play:Enta', 1.25], [600552861, '2016-06-04 22:58', u'Beautiful', 30.0, 1.14, 0.0, 2, 'False', 'False', u'Show of the Month: No Booking Fee', u'GT Play:Enta', 1.25], [600552873, '2016-06-04 23:53', u'Jersey Boys', 139.0, 4.83, 2.0, 2, u'MD', u'8', u'Show tickets plus Meal!', u'GT Play:Enta', 1.5]]

    main(mylist)