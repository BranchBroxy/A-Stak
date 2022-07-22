export_liste = []

def add_variable_to_csv_1(feature_mean, feature_std, feature_values, feature_pref, feature_label, csv_name):
    import csv

    with open('C:/test/test.csv', 'r') as csvinput:
        reader = csv.reader(csvinput)


        with open('C:/test/output.csv', 'w') as csvoutput:
            writer = csv.writer(csvoutput, lineterminator='\n')
            reader = csv.reader(csvinput)

            all = []
            row = next(reader)
            row.append('Berry')
            all.append(row)

            for row in reader:
                row.append(row[0])
                all.append(row)

            writer.writerows(all)

def add_variable_to_csv_1(feature_mean, feature_std, feature_values, feature_pref, feature_label, csv_name):
    from csv import writer
    from csv import reader
    default_text = 'Some Text'
    # Open the input_file in read mode and output_file in write mode
    with open(csv_name, 'r') as read_obj, \
            open(csv_name, 'w', newline='') as write_obj:
        # Create a csv.reader object from the input file object
        csv_reader = reader(read_obj)
        # Create a csv.writer object from the output file object
        csv_writer = writer(write_obj)
        # Read each row of the input csv file as list
        for row in csv_reader:
            # Append the default text in the row / list
            row.append(default_text)
            # Add the updated row / list to the output file
            csv_writer.writerow(row)

def add_variable_to_temp(feature_mean, feature_std, feature_values, feature_pref, feature_label):
    import os
    import tempfile
    fd, path = tempfile.mkstemp()
    try:
        with os.fdopen(fd, 'w') as tmp:
            # do stuff with temp file
            tmp.write('stuff')
    finally:
        os.remove(path)

def append_data_to_csv(feature, feature_mean, feature_std, feature_values, feature_pref, feature_label, file, path):
    import pandas as pd
    try:
        df = pd.read_csv(path)
        # df["new_column"] = "abc"
        df.loc[len(df.index)] = [file, feature, feature_mean, feature_std, feature_values, feature_pref, feature_label]
        df.to_csv(path, index=False, decimal=".")
    except:
        import csv
        import os
        # print(os.getcwd())
        # path = os.getcwd() + "/Feature.csv"
        print(path)
        with open(path, 'w') as myfile:

            writer = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            header = ["file", "feature", "feature_mean", "feature_std", "feature_values", "feature_pref",
                      "feature_label"]
            writer.writerow(header)
        append_data_to_csv(feature, feature_mean, feature_std, feature_values, feature_pref, feature_label, file, path)
