#!/usr/bin/python

import argparse
import json
import time


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data", help="input path to data.json result of /pf-admin-api/v1/bulk/export PingFederate API endpoint", required=True)
    parser.add_argument("-o", "--output", help="Output path to processed data.json", required=True)
    args = parser.parse_args()

    dataFile = open(args.data)

    dataJSON = json.load(dataFile)
    outputJSON = dataJSON

    outputJSON['item1'] = time.time()

    dataFile.close()

    outputFile = open(args.output, 'w')
    outputFile.write(json.dumps(outputJSON, indent=2))
    outputFile.close()
