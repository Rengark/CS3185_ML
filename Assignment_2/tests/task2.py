OK_FORMAT = True

test = {   'name': 'task2',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': ">>> assert isinstance(missing_values, pd.Series), 'The output of `isnull().sum()` should be a pandas Series.'\n"
                                               ">>> assert missing_values.sum() == 0, 'Missing values count should be non-negative.'\n"
                                               ">>> assert len(data_shape) == 2, 'The shape should have two dimensions (rows, columns).'\n"
                                               ">>> assert data_shape[0] == 41188, 'The DataFrame should have at least one row.'\n"
                                               ">>> assert data_shape[1] == 21, 'The DataFrame should have at least one column.'\n"
                                               ">>> assert len(education_categories) == 8, 'The `education` column should contain 8 unique categories.'\n"
                                               ">>> assert list(education_categories) == ['basic.4y', 'unknown', 'university.degree', 'high.school', 'basic.9y', 'professional.course', 'basic.6y', "
                                               "'illiterate']\n",
                                       'hidden': False,
                                       'locked': False,
                                       'points': 5}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
