import gspread
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient import discovery

# use credentials to create a cleint to interact with the google drive api
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

service = discovery.build('sheets', 'v4', credentials=creds)

# find workbook by name and open the first sheet
# make sure you use the right name here
sheet = client.open("forklift").sheet1

data = {
        'page_url': 'https://www.testcolumn.com', 'company': 'test column', 'test': 'Test column', 'location': 'The Netherlands',
        'price_excl_vat': 'on request', 'make': 'Crown', 'type': 'Vertical Order Pickers',
        'model': 'SP 3522 - 1.0 ** 2W5100 -  NEW battery !!', 'engine_type': 'Electric',
        'capacity': '1,000 kg', 'YOM': 2012, 'running_hours': '1,612', 'mast_type': 'Duplex',
        'lift_height': '5,100 mm', 'closed_height': '2,720 mm', 'free_lift': '0 mm',
        'fork_carriage': '', 'fork_length': '0 mm', 'forks': '', 'engine_charger': '',
        'transmission': '', 'battery_size_age': 'Capacity: 775Ah, Voltage: 24V, Year battery: 2018',
        'tyres': 'unknown/unknown', 'front_tyres': '', 'rear_tyres': '',
        'length': '0 mm', 'width': '0 mm', 'weight': '0 kg', 'images': ''
}


# sheet2 = sheet.spreadsheet.worksheet('supralift')
# col_name = []
# if len(sheet2.row_values((1))) == 0:
#     for k in data.keys():
#         col_name.append(k)
#
#     sheet2.append_row(values=col_name, value_input_option="RAW")
#
# # elif len(sheet2.row_values(1)) < len(data):
# #     for k1, k2 in zip(data.keys(), sheet2.row_values(1)):
# #         if k1 is not k2:
# #             sheet2.add_cols(1)
#     # find the key what is missing
#     # add a new column in location of element
#     # append data into new column
# else:
#     forklift_values = []
#     for k1, k2 in zip(data.keys(), sheet2.row_values(1)):
#         if k1 == k2:
#             forklift_values.append(data.get(k1))
#         elif k1 is not k2:
#             forklift_values.append(data.get(k1))
#
#
#
#
#     sheet2.append_row(values=forklift_values, value_input_option="RAW")


# mascus
mascus = [
        'url',
        'Company',
        'Location',
        'Price Excluding Tax',
        'Brand / model',
        'Category',
        'Year',
        'Hours',
        'Country',
        'Mascus ID',
        'Unit Number',
        'Serial Number',
        'Maximum lift capacity',
        'Maximum lift height',
        'Overall Lowered Height',
        'Fork length',
        'Tire type',
        'Transmission',
        'Additional Information'
]
#
# # supralift
supralift = [
        'url',
        'company',
        'location',
        'Price',
        'model',
        'Year of manufacture',
        'Power unit',
        'Type of truck',
        'Capacity (kg)',
        'Lift height (mm)',
        'Supralift product no.',
        'Mast type',
        'Comment',
]
#
# # tradus
tradus = [
        'url',
        'company',
        'Location',
        'price',
        'Price type',
        'Make',
        'Model',
        'Year',
        'Hours run',
        'Mileage',
        'Engine',
        'Condition',
        'description'
]
#
# # forklift
forklift = [
        'page_url',
        'company',
        'location',
        'price_excl_vat',
        'make',
        'model',
        'year_yom',
        'running_hours',
        'type',
        'engine_type',
        'capacity',
        'mast_type',
        'lift_height',
        'closed_height',
        'free_lift',
        'fork_carriage',
        'fork_length',
        'forks',
        'engine_charger',
        'transmission',
        'battery_size_age',
        'tyres',
        'front_tyres',
        'rear_tyres',
        'length',
        'width',
        'weight',
]

FIELDS = ['url', 'company', 'location', 'price', 'make', 'model', 'year']