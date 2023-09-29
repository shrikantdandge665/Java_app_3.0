import requests

def jfrogUpload():
    url = "http://3.85.54.23:8082/artifactory/java-web-app/"
    file_path = "/var/lib/jenkins/workspace/Demo_3.0/target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar"
    username = "admin"
    password = "Password"

    # Construct the URL for uploading
    upload_url = f"{url}Assignment2-artifact-path.jar"  # Replace 'your-artifact-path.jar' with the desired destination in your Artifactory repository

    try:
        # Create a session and set basic authentication
        session = requests.Session()
        session.auth = (username, password)

        # Perform the file upload
        with open(file_path, 'rb') as file:
            response = session.put(upload_url, data=file)

        if response.status_code == 201:
            print(f"Upload successful: {upload_url}")
        else:
            print(f"Upload failed with status code {response.status_code}: {response.text}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    jfrogUpload()