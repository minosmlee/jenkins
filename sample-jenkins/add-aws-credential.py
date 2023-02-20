import requests
import json

# Jenkins 설정값
jenkins_url = "http://localhost:8080"
jenkins_user = "admin"
jenkins_token = "1234567890123456789012345678901234"

# 새로운 credential 정보
credential_id = "aws-access-key-id"
credential_description = "AWS Access Key ID"
aws_access_key_id = "AKI**************"
aws_secret_access_key = "**********"

# Jenkins에 Credential 등록하는 API 호출
credential_data = {
    "": "0",
    "credentials": {
        "scope": "GLOBAL",
        "id": credential_id,
        "username": aws_access_key_id,
        "password": aws_secret_access_key,
        "description": credential_description,
        "$class": "com.cloudbees.plugins.credentials.impl.UsernamePasswordCredentialsImpl"
    }
}

create_credential_url = f"{jenkins_url}/credentials/store/system/domain/_/createCredentials"
response = requests.post(create_credential_url, data=json.dumps(credential_data), auth=(jenkins_user, jenkins_token), headers={'Content-Type': 'application/json'})

if response.status_code == 200:
    print(f"Credential {credential_id} created successfully!")
else:
    print("Failed to create credential.")
    print(f"Response status code: {response.status_code}")
    print(f"Response content: {response.content}")
