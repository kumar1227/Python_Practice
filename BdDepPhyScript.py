#!/bin/python
import json
import sys
FILE = sys.argv[1]
with open(FILE) as json_file:
        data = json.load(json_file)
        Results = data["results"]
        for p in Results:
                DependencyUri = p["uri"].encode('ascii')
                if(DependencyUri[-3:] == "jar"):
                        Dependency = DependencyUri[63:]
                        WriteDependency = open('DependencyList.txt','a')
                        WriteDependency.write(Dependency +"\n")
