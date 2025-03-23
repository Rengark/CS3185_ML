OK_FORMAT = True

test = {   'name': 'task3',
    'points': 20,
    'suites': [   {   'cases': [   {   'code': ">>> assert y_value_counts.sum() == 41188, 'The sum of value counts should equal the total number of rows.'\n"
                                               ">>> assert y_value_counts[0] == 36548, 'The number of 0 class is not correct.'\n"
                                               ">>> assert y_value_counts[1] == 4640, 'The number of 1 class is not correct.'\n",
                                       'hidden': False,
                                       'locked': False,
                                       'points': 5},
                                   {   'code': ">>> assert count_no_sub == 36548, 'Count of non-subscriptions is wrong.'\n"
                                               ">>> assert count_sub == 4640, 'Count of subscriptions is wrong.'\n"
                                               ">>> assert count_no_sub + count_sub == 41188, 'The sum of subscriptions and non-subscriptions should equal the total number of rows.'\n"
                                               ">>> assert pct_of_no_sub == 36548 / 41188, 'The value of pct_of_no_sub is wrong'\n"
                                               ">>> assert pct_of_sub == 4640 / 41188, 'The value of pct_of_sub is wrong'\n"
                                               ">>> assert np.isclose(pct_of_no_sub + pct_of_sub, 1), 'The sum of percentages should equal 100%.'\n",
                                       'hidden': False,
                                       'locked': False,
                                       'points': 5},
                                   {   'code': ">>> expected_grouped_means = data.groupby('y').mean(numeric_only=True)\n"
                                               ">>> assert grouped_means.equals(expected_grouped_means), 'The output of `groupby().mean()` is not correct'\n"
                                               ">>> assert isinstance(grouped_means, pd.DataFrame), 'The output of `groupby().mean()` should be a pandas DataFrame.'\n"
                                               '>>> assert \'y\' not in grouped_means.columns, "The grouped DataFrame should not contain the \'y\' column."\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 5}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
