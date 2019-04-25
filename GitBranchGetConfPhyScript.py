#!/bin/python3
import json
import sys

CASE = sys.argv[1]
if(CASE == "ORGREPOCSV"):
    print("Creating org and repo csv")
elif(CASE == "ORGREPOBRANCHCSV"):
    print("Creating the org, repo and branches csv")
elif(CASE == "GETBRNCHPRTXCONF"):
    print("creating the branch config csv")
else:
    print ("Please give the correct input")
