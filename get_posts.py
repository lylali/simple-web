import requests

posts_endpoint = "https://api.npoint.io/c790b4d5cab58020d391"

res = requests.get(url=posts_endpoint)
res.raise_for_status()
posts_data = res.json()

class GetPost:
    def __init__(self):
        self.all_posts = posts_data
        self.post = None

    def get_by_id(self, post_id):
        for n in self.all_posts:
            if n["id"] == post_id:
                return n
