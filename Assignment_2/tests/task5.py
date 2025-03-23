OK_FORMAT = True

test = {   'name': 'task5',
    'points': 30,
    'suites': [   {   'cases': [   {   'code': ">>> assert X.shape[0] == 41188, 'The number of rows in X should match the number of rows in data_final.'\n"
                                               ">>> assert y.shape[0] == 41188, 'The number of rows in y should match the number of rows in data_final.'\n"
                                               '>>> assert \'y\' not in X.columns, "\'y\' column should not be present in X."\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 5},
                                   {   'code': ">>> assert len(majority) == 25622, 'The majority class is empty.'\n"
                                               ">>> assert len(minority) == 3209, 'The minority class is empty.'\n"
                                               ">>> assert majority.shape[0] + minority.shape[0] == train_data.shape[0], 'The majority and minority classes do not sum up to the training data size.'\n"
                                               ">>> assert minority_upsampled.shape[0] == majority.shape[0], 'The number of upsampled minority class samples is not equal to the majority class.'\n"
                                               ">>> assert minority_upsampled.shape[0] > minority.shape[0], 'The minority class was not upsampled properly.'\n"
                                               ">>> assert majority.equals(train_data[train_data['y'] == 0]), 'wrong majority'\n"
                                               ">>> assert minority.equals(train_data[train_data['y'] == 1]), 'wrong minority'\n",
                                       'hidden': False,
                                       'locked': False,
                                       'points': 5},
                                   {   'code': ">>> assert upsampled_data.shape[0] == majority.shape[0] + minority_upsampled.shape[0], 'The concatenated data has incorrect size.'\n"
                                               '>>> assert \'y\' in upsampled_data.columns, "The \'y\' column is missing in the upsampled data."\n'
                                               '>>> assert \'y\' not in X_train.columns, "\'y\' should not be present in X_train."\n'
                                               '>>> assert y_train.shape[0] == upsampled_data.shape[0], "The size of y_train doesn\'t match the number of rows in the upsampled data."\n'
                                               ">>> assert len(y_train[y_train == 0]) == len(y_train[y_train == 1]), 'The class distribution after upsampling is not balanced.'\n"
                                               ">>> assert set(y_train).issubset({0, 1}), 'The y_train variable contains values outside the expected 0 and 1 classes.'\n",
                                       'hidden': False,
                                       'locked': False,
                                       'points': 10},
                                   {   'code': ">>> assert X_train_scaled.shape == X_train.shape, 'X_train_scaled should have the same shape as X_train'\n"
                                               ">>> assert X_test_scaled.shape == X_test.shape, 'X_test_scaled should have the same shape as X_test'\n"
                                               ">>> assert np.allclose(X_train_scaled.mean(axis=0), 0, atol=1e-07), 'Mean of scaled features in X_train_scaled should be close to 0'\n"
                                               ">>> assert np.allclose(X_train_scaled.std(axis=0), 1, atol=1e-07), 'Standard deviation of scaled features in X_train_scaled should be close to 1'\n"
                                               ">>> assert np.allclose((X_test - scaler.mean_) / scaler.scale_, X_test_scaled, atol=1e-07), 'X_test_scaled should be consistent with the scaling "
                                               "applied during fit on X_train'\n",
                                       'hidden': False,
                                       'locked': False,
                                       'points': 5}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
