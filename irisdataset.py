# Sharon Gibbons, 18-03-2018
# Iris dataset
# http://archive.ics.uci.edu/ml/datasets/Iris

# Python script that reads and prints the Iris dataset

# opens CSV file and extracts the data for reading
with open('data/iris.csv') as f:

    # iterates over each line of data in opened file
    for line in f:

       # outputs requested unpacked arguments as split list  
       print (*line.split(',')[:4])
