# Class and object

class Instagram:
    def __init__(self, title, description, creator_name, location):  
        self.title = title
        self.description = description
        self.creator_name = creator_name
        self.location = location
        self.comments = []  
        self.likes = 0

    def display_title(self):
        print("The title of the reel is", self.title)

    def display_description(self):
        print("The description of the reel is", self.description)

    def display_creator_name(self):
        print("The creator name is", self.creator_name)

    def display_location(self):
        print("The location is", self.location)

    def display_comments(self):
        print("Comments on the reel:",self.comments)
      

    def display_likes(self):
        print("The likes of the reel is", self.likes)

    def liked(self):
        self.likes += 1

    def disliked(self):
        if self.likes > 0:
            self.likes -= 1

    def add_comment(self,comment):
        self.comments.append(comment)

    def delete_comment(self):
        self.comments.pop()
        print(self.comments)

reel1 = Instagram(
    "dancing",
    "dancing with friends",
    "XYZ",
    "Mysuru"
)

reel1.disliked()  # 0
reel1.liked()     # 1

reel2 = Instagram(
    "finance minister conference",
    "finance minister conference with friends",
    "Ananya",
    "Bengaluru"
)

reel1.liked()     # 2
reel2.liked()     # 1
reel1.disliked()  # 1

reel1.display_likes()
reel2.display_likes()

reel1.display_creator_name()
reel1.display_location()
reel1.display_comments()
reel1.add_comment("Comment1")
reel1.display_comments()