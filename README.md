# anymindgroup_project
Anymindgroup assessment - REST API project

# It created on below environment
1. Anaconda3 with python3.9.0 verson
2. created python3.9.0 virtual environment with below commands
    - conda update conda
    - conda create -n anymind python=3.9.0
    - conda activate anymind
3. install requirements.txt packages
    - pip install -r requirements.txt
     
# Twitter API access
1. To access twitter api , we need a developer access, refer (https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api)
2. Create app in twitter development account , refer (https://developer.twitter.com/en/docs/apps/overview)
3. Twitter api has multiple endpoints , refer (https://developer.twitter.com/en/docs/api-reference-index)

# Flask REST Api
1. This Flask rest api has mainly 2 end points
    - Get tweets by a hashtag - return the list of tweets with the given hashtag.
      - sample request
      - curl -H "Accept: application/json" -X GET http://localhost:5000/hashtags/<sample_hashtag>?limit=40
      - sample_hashtag -> Python or Java ..
    - Get user tweets - return the list of tweets that the user has on his feed in JSON format.
      - sample request
      - curl -H "Accept: application/json" -X GET http://localhost:5000/users/<sample_username>?limit=20
      - sample_username -> twitter or smith ..
2. There are diffrent methods like file_encrypt, file_decrypt, get_logger etc added in this project

# Test the application
1. Run the app by running below command
    - python src/app.py
    - ![flask_api_running](https://user-images.githubusercontent.com/34347368/137393316-c72e78c6-b14a-46ce-8d3c-d48501c0fb12.PNG)
2. Run curl commands for both end points
    - ![curl_01](https://user-images.githubusercontent.com/34347368/137394748-72567d13-3654-4838-b3b3-b2b7b1d9e0b4.PNG)
    - ![curl_02](https://user-images.githubusercontent.com/34347368/137394780-38c9c9ea-82be-4c3a-ba09-a667821a639b.PNG)



   
   
