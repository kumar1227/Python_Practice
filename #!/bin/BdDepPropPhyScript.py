#!/bin/python
import json
import sys
REPO = sys.argv[1]
DEPJAR = sys.argv[2]
FILE = sys.argv[3]
with open(FILE) as json_file:
        data = json.load(json_file)
        Prop = data["properties"]
        if (Prop.get("APPCODE") != None and Prop.get("AppCode") != None):
                AppCodeList = Prop["APPCODE"] + Prop["AppCode"]
                #AppCodeValue = ";".join(AppCodeList)
                sent_str = ""
                for i in AppCodeList:
                        sent_str += str(i) + ";"
                        AppCodeValue = sent_str[:-1]
                        AppCodeValue = AppCodeValue.replace(",", ";")
        elif (Prop.get("APPCODE") != None and Prop.get("AppCode") == None):
                AppCodeList = Prop["APPCODE"]
                sent_str = ""
                for i in AppCodeList:
                        sent_str += str(i) + ";"
                        AppCodeValue = sent_str[:-1]
                        AppCodeValue = AppCodeValue.replace(",", ";")
        elif (Prop.get("APPCODE") == None and Prop.get("AppCode") != None):
                AppCodeList = Prop["AppCode"]
                sent_str = ""
                for i in AppCodeList:
                        sent_str += str(i) + ";"
                        AppCodeValue = sent_str[:-1]
                        AppCodeValue = AppCodeValue.replace(",", ";")
        else:
                print("Nothing Matching")
        if (Prop.get("BDScanStatus") != None):
                ApprovalStatus = Prop["BDScanStatus"]
                sent_str = ""
                for i in ApprovalStatus:
                        sent_str += str(i) + ";"
                        BDScanStatus = sent_str[:-1]
                        BDScanStatus = BDScanStatus.replace(",", ";")
        else:
                BDScanStatus = "Null"
        print(REPO + "," + DEPJAR + "," + AppCodeValue + "," + BDScanStatus)
        WriteDependency = open('MavenDependencyReport.csv','a')
        WriteDependency.write(REPO + "," + DEPJAR + "," + AppCodeValue + "," + BDScanStatus +"\n")
        WriteDependency.close()
