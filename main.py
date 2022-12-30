import csv


with open("output.csv", "w", newline="") as out_file:
    # Create a CSV writer object
    writer = csv.writer(out_file)

    # Iterate over the three input files
    for reading_file in ["data\daily_sales_data_0.csv", "data\daily_sales_data_1.csv", "data\daily_sales_data_2.csv"]:
        # Open the input file in read mode
        with open(reading_file, "r") as file:
            # Create a CSV reader object
            reader = csv.reader(file)
            row_count = 0

            # Iterate over the rows in the input file
            for row in reader:
                product = row[0]
                # Check the value of the product field
                if product == "pink morsel":
                    row_count += 1

                    # Calculate the sales for the row
                    sales = float(row[1].replace('$','')) * float(row[2])


                    # Write the formatted row to the output file
                    writer.writerow([sales, row[3], row[4]])
            print(f"There are {row_count} rows in the file.")
