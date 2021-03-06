"""
poorly performing, poorly written module

"""

import datetime
import csv
import logging

# Set Up Logger
logging.basicConfig(level=logging.DEBUG)


def analyze(filename):
    # Starts the Timer
    start = datetime.datetime.now()

    logging.info("CSV1 Read Start")
    # Timer for First CSV Reader
    start_csv_read_1 = datetime.datetime.now()
    # With loop to process the csv file
    with open(filename) as csvfile:
        # Creates a reader object and gives delimeter
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        # Create a new list
        new_ones = []
        for row in reader:
            lrow = list(row)
            if lrow[5] > '00/00/2012':
                new_ones.append((lrow[5], lrow[0]))

        # Determine Elapsed time to perform csv reader
        end_csv_read_1 = datetime.datetime.now()
        csv_read_delta = end_csv_read_1 - start_csv_read_1
        logging.info("csv_read_1 Elapsed Time: {}".format(csv_read_delta))

        year_count = {
            "2013": 0,
            "2014": 0,
            "2015": 0,
            "2016": 0,
            "2017": 0,
            "2018": 0
        }

        # Tracking Parsing Information
        logging.info("Year Counters Start")
        new_ones_start = datetime.datetime.now()
        for new in new_ones:
            if new[0][6:] == '2013':
                year_count["2013"] += 1
            if new[0][6:] == '2014':
                year_count["2014"] += 1
            if new[0][6:] == '2015':
                year_count["2015"] += 1
            if new[0][6:] == '2016':
                year_count["2016"] += 1
            if new[0][6:] == '2017':
                year_count["2017"] += 1
            if new[0][6:] == '2018':
                year_count["2017"] += 1

        new_ones_end = datetime.datetime.now()
        delta_new_ones = new_ones_end - new_ones_start
        logging.info("New Ones Elapsed: {}". format(delta_new_ones))

        print(year_count)

    logging.info("AO Search")
    AO_search_start = datetime.datetime.now()
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')

        found = 0

        for line in reader:
            lrow = list(line)
            if "ao" in line[6]:
                found += 1

        print(f"'ao' was found {found} times")
    AO_search_end = datetime.datetime.now()
    AO_search_delta = AO_search_end - AO_search_start

    logging.info("AO Search Elapsed: {}".format(AO_search_delta))
    end = datetime.datetime.now()
    full_delta = end - start
    logging.info("Total Time: {}".format(full_delta))

    return (start, end, year_count, found)

def main():
    #filename = "data/exercise.csv"
    filename = "testfile.csv"
    analyze(filename)


if __name__ == "__main__":
    main()
