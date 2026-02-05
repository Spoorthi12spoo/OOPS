#Multiple inheritance

class Camera:
    def __init__(self,camera_quality):
        self.camera_quality=camera_quality
    def display_camera_details(self):
        print(f"Camera quality: {self.camera_quality}")

class MusicPlayer:
    def __init__(self,sound_quality):
        self.sound_quality=sound_quality
    def display_music_details(self):
        print(f"Sound quality: {self.sound_quality}")

class SmartPhone(Camera,MusicPlayer):
    def __init__(self,camera_quality,sound_quality,brand):
        Camera.__init__(self,camera_quality)
        MusicPlayer.__init__(self,sound_quality)
        self.brand=brand
    def display_smartphone_details(self):
        print(f"Smart phone brand is: {self.brand}")
        self.display_camera_details()
        self.display_music_details()

Phone1=SmartPhone("50 MP","Hifi audio","Samsung")
Phone1.display_smartphone_details()


#Multilevel inheritance

class Product:
    def __init__(self,product_name,price):
        self.product_name=product_name
        self.price=price

    def display_product(self):
        print(f"Product: {self.product_name} Price: {self.price}")

class ElectronicProduct(Product):
    def __init__(self,product_name,price,brand,warranty):
        super().__init__(product_name,price)
        self.brand=brand
        self.warranty=warranty

    def display_electronic_product(self):
        print(f"Brand: {self.brand} Warranty: {self.warranty}")
        self.display_product()

    
class MobilePhone(ElectronicProduct):
    def __init__(self, product_name, price, brand, warranty, ram, storage):
        super().__init__(product_name, price, brand, warranty)
        self.ram = ram
        self.storage = storage

    def display_mobile_details(self):
        print(f"Ram: {self.ram} Storage: {self.storage}")
        self.display_electronic_product()

Mobile1=MobilePhone("Phone1",20000,"Samsung","2 years","8 GB","512 GB")
Mobile1.display_mobile_details()