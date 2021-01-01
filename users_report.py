from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import requests
import json
import csv

def get_specific_user_details(login):
    single_user_details = requests.get(f'https://api.github.com/users/{login}').json()
    return single_user_details

def get_followers_details(login):
    followers_details = requests.get(f'https://api.github.com/users/{login}/followers').json()
    return followers_details

def git_all_user_details():
    user_details=requests.get(f'https://api.github.com/users').json()
    return user_details

def upload_file_to_drive():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    file = drive.CreateFile({"mimeType": "text/csv"})
    file.SetContentFile("users_and_followers_list.csv")
    file.Upload()


all_user_details = git_all_user_details()
rows = []
for user in all_user_details:
    if user["id"]%10==0:
        single_user_details = get_specific_user_details(user["login"])
        followers_details = get_followers_details(single_user_details["login"])

        for followers in followers_details:
            rows.append([user["id"],user["login"],single_user_details["name"],followers["id"],followers['login']])

fields = ['UserId', 'UserLogin', 'UserName', 'FollowerId', 'FollowerLogin']
filename = "users_and_followers_list.csv"

with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

upload_file_to_drive()
