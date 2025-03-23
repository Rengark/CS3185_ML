OK_FORMAT = True

test = {   'name': 'task1',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': ">>> assert data.shape[0] == 41188, 'Dataset should have 41188 rows. Please check if you loaded the correct dataset.'\n"
                                               ">>> assert data.shape[1] == 21, 'Dataset should have 21 columns. Please check if you loaded the correct dataset.'\n"
                                               '>>> assert head_data.shape[0] == 5, "The \'head_data\' should return exactly 5 rows. Ensure you are using the \'head()\' function correctly."\n'
                                               '>>> assert data_description.equals(data.describe()), "The function used to get summary of statistics is not correct. Ensure you use the \'describe()\' '
                                               'method."\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 5}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
