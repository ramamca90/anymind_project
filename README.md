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

# Deployemnt and installation
1. Copy the code repo https://github.com/ramamca90/anymind_project.git and place it into locally 
   or setup a build job in CICD pipline(jenkins/Ansible etc) and install the code into target platform (This part not implemented as par of this project)
    - ![local_code_repo](https://user-images.githubusercontent.com/34347368/137423666-cd406677-2d09-4490-a2ad-d006e8d88169.PNG)

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

# unit testing - pytest 
1. pytest framework added for unit testing
2. tests folder contains all unit tests
3. we can run the below command for check the status of unit tests
    - pytest --cov=src/ tests/ -v --junitxml="result.xml" --cov-report xml --cov-report html --html="results/index.html" -vv --disable-warnings
    - ![pytest_unittesting](https://user-images.githubusercontent.com/34347368/137395453-b7c45285-6e36-41be-be4c-8d2925bb5ddd.PNG)
4. code coverage generated at index.html page
    - ![code_coverage](https://user-images.githubusercontent.com/34347368/137395991-a8001517-ca3d-4d96-a22f-ba033bc53c9c.PNG)



   
   
