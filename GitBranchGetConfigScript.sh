#!/bin/bash
#!/bin/python
GIT_URL="https://gitprod.statestr.com"
UID=e651793
PASSWD="Something"
echo "============================[Start]Genrating Orgaization List======================================="
rm -rf ./OrgJosn.txt
rm -rf ./OrgList.txt
x=1
while [ $x -le 100 ]
do
curl -XGET -u "$UID:$PASSWD" "${GIT_URL}/api/v3/user/repos?per_page=100\&page=$x"  >> ./OrgJosn.txt
x=$(( $x + 1 ))
done
cat OrgJosn.txt | grep '"full_name"' | awk -F ':' '{print $2}' | tr -d "[:blank:]" | tr -d , | tr -d '\"' | grep -v ^e | grep -v ^p | cut -d'/' -f1 | uniq > ./OrgList.txt
echo "============================[END]Generating Orgaization List======================================="
echo "============================[Start]Generating ORG & REPO csv file======================================="
rm -rf ./RepoJson.txt
rm -rf ./OrgRepo.csv
while read ORGNAME
do
curl -XGET -u "$UID:$PASSWD" "${GIT_URL}/api/v3/orgs/$ORGNAME/repos" > ./RepoJson.txt
pyhton GitBrnachPhyScript.py ORGREPOCSV
done < ./OrgList.txt
echo "============================[END]Generating ORG & REPO csv file======================================="
echo "============================[Start]Generating ORG, REPO & BRANCH csv file======================================="
rm -rf ./BranchJson.txt
rm -rf ./OrgRepoBranch.csv
IFS=","
while read OWNER REPO
do
curl -XGET -u "$UID:$PASSWD" "${GIT_URL}/api/v3/repos/$OWNER/$REPO/branches > ./BranchJson.txt
pyhton GitBrnachPhyScript.py ORGREPOBRANCHCSV
done < ./OrgRepo.csv
echo "============================[END]Generating ORG, REPO & BRANCH csv file======================================="
echo "============================[Start]Generating protected branch config csv======================================="
rm -rf ./ProtectedBranchConfigJson.txt
rm -rf ./ProtectedBranchConfig.csv
IFS=","
while read OWNER REPO BRANCH
do
curl -XGET -u "$UID:$PASSWD" "${GIT_URL}/api/v3/repos/$OWNER/$REPO/branches/$BRANCH/protection > ./ProtectedBranchConfigJson.txt
pyhton GitBrnachPhyScript.py GETBRNCHPRTXCONF
done < ./OrgRepoBranch.csv
echo "============================[END]Generating protected branch config csv======================================="
