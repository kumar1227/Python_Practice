#!/bin/python
import json
import sys
import itertools

COUNT = len(sys.argv)
if(COUNT == 2):
    CASE = sys.argv[1]
elif(COUNT == 4):
	CASE = sys.argv[1]
	OWNER = sys.argv[2]
	REPO = sys.argv[3]
else:
	CASE = sys.argv[1]
	OWNER = sys.argv[2]
	REPO = sys.argv[3]
	BRANCH = sys.argv[4]
if(CASE == "ORGREPOCSV"):
	with open('RepoJson.txt') as json_file:
		data = json.load(json_file)
		for p in data:
			RepoName = p["name"]
			OrgName = p["owner"]["login"]
			WriteRepo = open('OrgRepo.csv','a')
			WriteRepo.write(OrgName + ',' + RepoName +"\n")
			WriteRepo.close()
			print('AppCode: '+OrgName+';'+'Repo: '+RepoName)
elif(CASE == "ORGREPOBRANCHCSV"):
	OrgName = OWNER
	RepoName = REPO
	with open('BranchJson.txt') as json_file:
		data = json.load(json_file)
		for p in data:
			BranchName = p["name"]
			WriteRepo = open('OrgRepoBranch.csv','a')
			WriteRepo.write(OrgName + ',' + RepoName + ',' + BranchName +"\n")
			WriteRepo.close()
			print('AppCode: '+OrgName+';'+'Repo: '+RepoName+';'+'Branch: '+BranchName)
elif(CASE == "GETBRNCHPRTXCONF"):
	OrgName = OWNER
	RepoName = REPO
	BranchName = BRANCH
	with open('ProtectedBranchConfigJson.txt') as json_file:
		p = json.load(json_file)
		if p.get("url") != None:
			RepoStatusCheck = p["required_status_checks"]["strict"]
			if(RepoStatusCheck == 1):
				RepoStatCheckEnable = 'Yes'
			else:
				RepoStatCheckEnable = 'No'
			LdapTeams = p["restrictions"]["teams"]
			TeamName = []
			for LdGroup in LdapTeams:
				TeamName_temp = []
				TeamName_temp.append(LdGroup["name"].encode('ascii'))
				TeamName.append(TeamName_temp)
	 		ListTeam = list(itertools.chain.from_iterable(TeamName))
			JoinTeams = ";".join(ListTeam)
			if p.get("required_pull_request_reviews") != None:
				PullRequestReviewEnabled = 'Yes'
			else:
				PullRequestReviewEnabled = 'No'
			WriteRepo = open('ProtectedBranchConfig.csv','a')
			WriteRepo.write(OrgName + ',' + RepoName + ',' + BranchName + ',' + 'Enabled' + ',' + RepoStatCheckEnable + ',' + JoinTeams + ',' + PullRequestReviewEnabled +"\n")
			WriteRepo.close()
			print('AppCode: '+OrgName+';'+'Repo: '+RepoName+';'+'Branch: '+BranchName+';'+'Protection: '+'Enabled'+';'+ 'RepoStatusCheck: '+ RepoStatCheckEnable +';'+'Teams: '+JoinTeams +';'+'PullRequestReviewEnabled: '+PullRequestReviewEnabled)
else:
print ("Please give the correct input")
