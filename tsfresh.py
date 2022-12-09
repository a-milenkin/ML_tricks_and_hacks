# settings = get_setting_tsfresh(settings)
# settings = MinimalFCParameters()
settings = EfficientFCParameters()

train_df.fillna(0, inplace=True)
res_train_df = None
# res_test_df = None

vr = VarianceThreshold(0.5)
for num, num_col in enumerate(numeric_cols):
    now = datetime.now()
    print(num, 'col', num_col)
    
    
    settings = full_settings_filtered[num_col]
    
    Distributor = MultiprocessingDistributor(n_workers=4,
                                             disable_progressbar=False,
                                             progressbar_title="Feature Extraction")

    X = extract_relevant_features(train_df[["customer_ID", "S_2"]+[num_col]].fillna(0), 
                                  y,
                                  column_id='customer_ID',
                                  column_sort='S_2',
                                  n_jobs=5,
                                  chunksize=5,
                                  default_fc_parameters=settings,
                                  fdr_level = 0.01,
                                  distributor = Distributor)
    
    X = pd.DataFrame(vr.fit_transform(X), columns=X.columns[vr.get_support()])
    print('прошло времени до генерации', datetime.now() - now)
    kind_to_fc_parameters = tsfresh.feature_extraction.settings.from_columns(X)
    X_test = extract_features(test_df[["customer_ID", "S_2"]+[num_col]].fillna(0), 
                                  column_id='customer_ID',
                                  column_sort='S_2',
                                  n_jobs = 4,
                                  chunksize=5,
                                  distributor = Distributor,
                                  kind_to_fc_parameters=kind_to_fc_parameters)
    X_test = X_test[X.columns]
    print('прошло времени до фильтрации', datetime.now() - now)
    if res_train_df is None:
        res_train_df = X
        res_train_df["target"] = y.values
        res_train_df["customer_ID"] = customer_train
        res_test_df = X_test
        res_test_df["customer_ID"] = customer_test
    else:
        X = reduce_mem_usage(X)
        X_test = reduce_mem_usage(X_test)

        res_train_df = pd.concat([res_train_df, X], axis=1)
        res_test_df = pd.concat([res_test_df, X_test], axis=1)

        res_train_df.to_csv("./../tmp_data/del_full_train_tsfresh.csv", index=False)
        res_test_df.to_csv("./../tmp_data/del_full_test_tsfresh.csv", index=False)
        
        print('прошло времени до сохраниения', datetime.now() - now)
