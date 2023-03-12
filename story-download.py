from instagrapi import Client

# Enter your Instagram username and password
username = "YOUR_USERNAME"
password = "YOUR_PASSWORD"

# Initialize the Instagram client
client = Client()
client.login(username, password)

# Enter the username of the Instagram user whose stories you want to download
user_to_download = "USERNAME_OF_USER_TO_DOWNLOAD"

# Get the user's stories
stories = client.get_stories(user_to_download)

# Loop through the stories and download them
for story in stories:
    filename = story.pk + ".jpg" # Use the story ID as the filename
    with open(filename, "wb") as f:
        f.write(story.get_image())
