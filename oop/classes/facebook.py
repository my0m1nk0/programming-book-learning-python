class Facebook:
    post =""
    title =""

    def __init__(self,title = "POST",post = 'ရေသောက်နည်း သင်တန်း'):
        self.title = title
        self.post = post
        print('default constructor')

    def add_post(self):
        return  self.title , self.post


story = Facebook("Add Story","JustKidding")
post = story.add_post()

like = Facebook("Add Like","Love React")
res = like.add_post()

print(post)
print(res)
