OK_FORMAT = True

test = {   'name': 'task6',
    'points': 20,
    'suites': [   {   'cases': [   {   'code': ">>> assert hasattr(logreg, 'coef_'), 'The logistic regression model was not trained properly.'\n"
                                               ">>> assert round(accuracy, 2) == 0.85, 'The accuracy value is not correct.'\n"
                                               ">>> assert len(y_pred) == len(y_test), 'The number of predictions should match the number of test samples.'\n",
                                       'hidden': False,
                                       'locked': False,
                                       'points': 20}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
