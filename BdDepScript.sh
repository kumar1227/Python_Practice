#!/bin/bash
echo "REPO,ARTIFACT,APPCODES,BD_SCAN_STATUS" > MavenDependencyReport.csv
IFS=","
while read repo binaryname
do
curl -u $GIT_USR:$GIT_PWD -XGET "$GIT_URL/api/storage/$repo/$binaryname?properties" > ./ProperiesResponseJson
python BdDepPropPhyScript $repo $binaryname ProperiesResponseJson
done < ./SDP_Maven_Dependencies_List.csv
