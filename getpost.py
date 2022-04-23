import requests
import time
from datetime import datetime

# Here we define our query as a multi-line string
query = '''
query ($id: Int, $post_count: Int) {
  Page(page: 1, perPage: $post_count) {
    activities(userId: $id, sort: ID_DESC) {
      ... on TextActivity {
        type
        id
        user {
            name
            avatar {
                large
            }
        }
        createdAt
        siteUrl
        text
        likeCount
      }
    }
  }
}
'''

# Define our query variables and values that will be used in the query request
variables = {
    "id": 5211659,
    "post_count": 1
}

url = 'https://graphql.anilist.co'

# Make the HTTP Api request


while(True):
    response = requests.post(url, json={'query': query, 'variables': variables})
    data = response.json()

    name = data['data']['Page']['activities'][0]['user']['name']
    avatar = data['data']['Page']['activities'][0]['user']['avatar']['large']
    date = datetime.fromtimestamp(int(data['data']['Page']['activities'][0]['createdAt'])).strftime("%d/%m/%y %H:%M:%S")
    contents = data['data']['Page']['activities'][0]['text']
    id = data['data']['Page']['activities'][0]['id']

    print(name + " Posted at " + date)
    print(contents)
    print(f"ID: {id}")
    print("==========================")

    f = open("msg.dat", "r")
    msg = f.read()
    if str(msg) == str(id):
        print("Message already read")
    else:
        f = open("msg.dat", "w")
        f.write(str(id))
        f.close()
        print("New message!")
        
    time.sleep(30)