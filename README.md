# users_report_generating_task

#Task 1:
    #Get the users and their followers in the CSV format
    #1. To get the list of users https://api.github.com/users
    #2. Get the list of user Ids divisible by 5
    #3. Iterate the result and get the user details https://api.github.com/users/{login}
    #4. Get the followers list for that user https://api.github.com/users/{login}/followers
    
    #Initially I import the 'requests' pacakages for working with github api calls.
    #And also I import the 'json' and 'csv' package for converting of json format and creating a csv file.
    #First get all users details by git_all_user_details() function.
    #And the git_all_user_details() return value has a id of user, the condition is get the user's by id%10==0.
    #We use get_specific_user_details(user["login"]) function for getting the single user details,because,
    # this function return's user name.
    #And we get the followers details by get_followers_details(single_user_details["login"]) function,
    #finally we add the UserId,UserLogin,UserName,FollowerId and FollowerLogin to 'fields' variable,
    # and add the data's to rows variable.
    #And finally create the csv file using csvwriter object.
    
#Task 2:

    #Task 2 is add the csv file into google drive.
    
    # For this we need to install Pydrive packages.
    # Then, use upload_file_to_drive() function to uploading the file. this function contains code for that.
    # Before, running the code , we need to "create a credentials" for Google drive API.
    # First open the Google cloud platform using this link https://console.cloud.google.com/
    # And create a project if you don't have. 
    # choose API & credentials option from side menu bar. And enable the API services.
    #And click credentials option. It will move to create credentials option.
    #And click a 'create credentials' and in that click 'Oauth client ID' option.
    #Select applicaton type and further details and save.
    #Come back to dashboard and get the credential details from right side of download option.
    #create a client_secrets.json file in your working directory, store the json values in that.
    #Now we can run the program. It will lead to upload the csv file to drive.
    
    # one thing is we could upload the file to particular, credential matched Google drive only.
    #If we try with other accounts it will through authentication error.