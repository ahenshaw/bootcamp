def impute(df):
    # define the columns to be examined
    cols = set(df.columns.values)
    for column_name in cols:
        seq = df[column_name]

        # check for coding by looking for numbers that are all '9's
        #  (and perhaps a decimal point)
        s = str(int(seq.max()))
        if s.count('9') == len(s):
            # Now compute a low value by changing the last 
            # digit to a 2
            low = float(s[:-1]+'2')
            print(low)

            # Change coded observations to nulls
            df[column_name] = seq.where(seq < low)

    # replace all NaNs (which includes missing values) with the mean
    df = df.fillna(df.mean())
    return df
