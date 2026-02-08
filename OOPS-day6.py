class InstagramAccount:
    def __init__(self,account_name,password):
        self.account_name=account_name
        self._private_reels=[]
        self.__archived_reels=[]
        self.__password=password

    def add_private_reel(self,reel_name):
        self._private_reels.append(reel_name)
        print("private reel added")

    def display_private_reels(self,is_follower):
        if is_follower:
            for reel in self._private_reels:
                print("Private reels: ",reel)
        else:
            print("Access Denied! Only followers can view private reels")

    def add_archived_reel(self,reel_name):
        self.__archived_reels.append(reel_name)
        print("archive reel added")

    def display_archived_reels(self,password):
        if password==self.__password:
             for reel in self.__archived_reels:
                print("Archived reels: ",reel)
        else:
            print("Access Denied! Only account holder can view archived reels")
            return self.__archived_reels
        
    def get_archived_reels(self, password):
        if password == self.__password:
            return self.__archived_reels
        else:
            print("Access Denied! Wrong password")
            return None

   
    def set_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password updated successfully!")
        else:
            print("Wrong old password! Password not changed.")

acc=InstagramAccount("ABC","1124")

acc.add_private_reel("Technical reel")
acc.add_private_reel("Song reel")

acc.add_archived_reel("Dance reel")
acc.add_archived_reel("College reel")

# acc.display_private_reels(True)



# acc.get_archived_reels("1124")
# acc.set_password("1124","6789")



