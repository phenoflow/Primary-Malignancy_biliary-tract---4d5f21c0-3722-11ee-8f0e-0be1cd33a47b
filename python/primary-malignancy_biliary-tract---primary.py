# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"105613.0","system":"med"},{"code":"107299.0","system":"med"},{"code":"10949.0","system":"med"},{"code":"110147.0","system":"med"},{"code":"16915.0","system":"med"},{"code":"23433.0","system":"med"},{"code":"35039.0","system":"med"},{"code":"36495.0","system":"med"},{"code":"40438.0","system":"med"},{"code":"41313.0","system":"med"},{"code":"52537.0","system":"med"},{"code":"58088.0","system":"med"},{"code":"61643.0","system":"med"},{"code":"65124.0","system":"med"},{"code":"72445.0","system":"med"},{"code":"74896.0","system":"med"},{"code":"7982.0","system":"med"},{"code":"8711.0","system":"med"},{"code":"89593.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('primary-malignancy_biliary-tract-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["primary-malignancy_biliary-tract---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["primary-malignancy_biliary-tract---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["primary-malignancy_biliary-tract---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
