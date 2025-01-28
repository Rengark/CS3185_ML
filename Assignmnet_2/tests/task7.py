OK_FORMAT = True

test = {   'name': 'task7',
    'points': 30,
    'suites': [   {   'cases': [   {   'code': ">>> assert hyperparameters == {'penalty': ['l1', 'l2', 'elasticnet', 'none'], 'C': [0.01, 0.1, 1, 10]}, 'Hyperparameter dictionary is incorrect.'\n"
                                               ">>> assert isinstance(lgr, LogisticRegression), 'Logistic Regression model not instantiated correctly.'\n"
                                               ">>> assert isinstance(grid_search, GridSearchCV), 'GridSearchCV is not instantiated correctly.'\n"
                                               ">>> assert grid_search.param_grid == hyperparameters, 'Parameter grid is incorrect in GridSearchCV.'\n",
                                       'hidden': False,
                                       'locked': False,
                                       'points': 10},
                                   {   'code': ">>> assert grid_search.best_params_ == best_params, 'Best parameters do not match GridSearchCV output.'\n"
                                               ">>> assert grid_search.best_score_ == best_score, 'Best score does not match GridSearchCV output.'\n"
                                               ">>> assert grid_search.best_estimator_ == best_model, 'Best model does not match GridSearchCV output.'\n",
                                       'hidden': False,
                                       'locked': False,
                                       'points': 10},
                                   {   'code': ">>> assert y_pred.shape[0] == y_test.shape[0], 'Predictions shape does not match test data shape.'\n"
                                               ">>> assert conf_matrix[0][0] == 9296 or conf_matrix[0][1] == 1630 or conf_matrix[1][0] == 209 or (conf_matrix[1][1] == 1222), 'The values in confusion "
                                               "matrix are not correct.'\n",
                                       'hidden': False,
                                       'locked': False,
                                       'points': 10}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
