import json


with open('blog_source.json') as file:
    posts_data = json.load(file)


class GetPost:
    def __init__(self):
        self.all_posts = posts_data
        self.post = None

    def get_by_id(self, post_id):
        for n in self.all_posts:
            if n["id"] == post_id:
                return n
