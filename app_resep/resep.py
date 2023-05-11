import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.graphics import Color, Rectangle

class MainMenu(GridLayout):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.cols = 1
        # Set background color
        with self.canvas.before:
            Color(125/255,65/255,119/255,1)  # green color
            self.rect = Rectangle(size=self.size, pos=self.pos)
        
        self.add_widget(Label(text="Menu Utama", font_size=80))

        self.start_button = Button(text="Mulai",font_size=30,size_hint=(1,0.1))
        self.start_button.bind(on_press=self.show_recipe_menu)
        self.add_widget(self.start_button)

    def on_size(self, *args):
        self.rect.size = self.size

    def on_pos(self, *args):
        self.rect.pos = self.pos

    def show_recipe_menu(self, instance):
        popup_layout = GridLayout(cols=1)
        popup = Popup(title="Pilih Jenis Resep", content=popup_layout, size_hint=(None, None), size=(400, 400))
        popup_layout.add_widget(Label(text="Pilih jenis resep:"))

        food_button = Button(text="Makanan")
        food_button.bind(on_press=self.show_food_menu)
        popup_layout.add_widget(food_button)

        drink_button = Button(text="Minuman")
        drink_button.bind(on_press=self.show_drink_menu)
        popup_layout.add_widget(drink_button)

        snack_button = Button(text="Cemilan")
        snack_button.bind(on_press=self.show_snack_menu)
        popup_layout.add_widget(snack_button)
        popup.background_color = (125/255,65/255,119/255,1)
        popup.open()

    def show_food_menu(self, instance):
        popup_layout = GridLayout(cols=1)
        popup = Popup(title="Daftar Makanan", content=popup_layout, size_hint=(None, None), size=(400, 400))

        food_list = ['Nasi Goreng','Mie Goreng','Ketoprak','Pecel Sayur']
        for food in food_list:
            food_button = Button(text=food)
            food_button.bind(on_press=lambda x, food=food: self.show_recipe(food))
            popup_layout.add_widget(food_button)
        print(food)
        popup.open()

    def show_drink_menu(self, instance):
        popup_layout = GridLayout(cols=1)
        popup = Popup(title="Daftar Minuman", content=popup_layout, size_hint=(None, None), size=(400, 400))

        drink_list = ['Es Teh', 'Es Jeruk', 'Es Campur','Wedang Jahe','Bandrek','STMJ']
        for drink in drink_list:
            drink_button = Button(text=drink)
            drink_button.bind(on_press=lambda x,drink=drink: self.show_recipe(drink))
            popup_layout.add_widget(drink_button)

        popup.open()

    def show_snack_menu(self, instance):
        popup_layout = GridLayout(cols=1)
        popup = Popup(title="Daftar Cemilan", content=popup_layout, size_hint=(None, None), size=(400, 400))

        snack_list = ['Kentang Goreng']
        for snack in snack_list:
            snack_button = Button(text=snack,size_hint=(None,None),size=(375,50))
            snack_button.bind(on_press=lambda x,snack=snack: self.show_recipe(snack))
            popup_layout.add_widget(snack_button)

        popup.open()

    def show_recipe(self, recipe):
        recipe_layout = GridLayout(cols=1, padding=10)
        recipe_popup = Popup(title=recipe, content=recipe_layout, size_hint=(None, None),size=(500,500))
        recipe_layout.add_widget(Label(text="Bahan:",bold=True))
        if recipe == "Nasi Goreng":
            ingredients = ["nasi sesuai selera", "bawang merah 5 siung", "bawang putih 5 siung", "cabai rawit sesuai selera",
                           "kecap manis", "minyak goreng", "telur","garam (bila perlu)","penyedap rasa (bila perlu)","gula (bila perlu)"]
        elif recipe == "Mie Goreng":
            ingredients = ["mie instan secukupnya", "bawang merah 5 siung", "bawang putih 3 siung", "cabai sesuai selera", "minyak goreng","telur",
                           "sosis secukupnya (bila perlu)","sawi secukupnya","kol seckupnya"]
        elif recipe == "Ketoprak":
            ingredients = ["tahu putih 2 buah","ketupat iris","tauge 50 gr","bihun 100 gr","kecap manis","kacang tanah 150 gr",
                           "gula merah sisir secukupnya","bawang putih 1 siung","cabai secukupnya","garam","air asam jawa 2 sdm",
                           "bawang goreng","kerupuk"]
        elif recipe == "Pecel Sayur":
            ingredients = ["kol 1 buah, iris","kacang panjang 1 ikat, potong","sawi 1 ikat, potong","buncis 10 batang",
                           "tauge 50 gr","larutan asam jawa 1 sdm","gula merah sisir 100 gr","kacang tanah 100 gr, goreng dan haluskan",
                           "daun jeruk (bila perlu)","bawang putih 7 siung","air secukupnya","cabai rawit sesuai selera",
                           "garam secukupnya"]
        elif recipe == "Es Teh":
            ingredients = ["Teh celup 1 buah","Es batu secukupnya","Gula pasir secukupnya","Air secukupnya"]
        elif recipe == "Es Jeruk":
            ingredients = ["Jeruk Peras secukupnya","Gula secukupnya","Es batu","Air secukupnya"]
        elif recipe == "Es Campur":
            ingredients = ["Roti Tawar","Cincau hitam","Agar-agar","Nata de coco","Alpukat","Semangka","Susu kental manis",
                           "Gula pasir","Sirup cocopandan","Es batu","Air mineral"]
        elif recipe == "Wedang Jahe":
            ingredients = ["Jahe 2 rimpang (bersihkan dan memarkan)","Air secukupnya","Kayu manis","Madu secukupnya",
                           "Serai 1 batang (memarkan)"]
        elif recipe == "Bandrek":
            ingredients = ["Gula merah/gula aren secukupnya","Jahe 2 ruas","Serai 2 batang","Air secukupnya"]
        elif recipe == "STMJ":
            ingredients = ["Susu UHT secukupnya","Susu kental manis","Madu secukupnya","Jahe 6 cm","Telur ayam kampung 2 butir"]
        elif recipe == "Kentang Goreng":
            ingredients = ["Kentang 200 gram","Garam secukupnya","Minyak goreng","Air dingin","Es batu"]

        for ingredient in ingredients:
            recipe_layout.add_widget(Label(text=ingredient))
        
        recipe_layout.add_widget(Label(text="-------------------------------------------------------------------------------------------------------------"))

        recipe_layout.add_widget(Label(text="Langkah - langkah:",bold=True))
        if recipe == "Nasi Goreng":
            langkah = ["1. Haluskan bawang merah, bawang putih, dan cabai.",
                       "2. Panaskan minyak goreng, masukkan telur dan orak-arik.",
                       "3. Tumis bumbu yang telah dihaluskan hingga wangi.",
                       "4. Masukkan nasi, kecap manis, dan penyedap rasa, aduk hingga rata."]
        elif recipe == "Mie Goreng":
            langkah = ["1. Haluskan bawang merah, bawang putih, dan cabai.",
                       "2. Panaskan minyak goreng, tumis bumbu yang telah dihaluskan.",
                       "3. Tambahkan sosi dan telur, aduk hingga rata.",
                       "4. Masukkan mie instan yang telah direbus, masukkan bumbu mie instan",
                       "5. Masukkan sawi dan kol yang telah di iris. Aduk semua bahan hingga rata."]
        elif recipe == "Ketoprak":
            langkah = ["1. Potong tahu dadu, goreng hingga kering. Rebus tauge dan bihun.",
                       "2. Haluskan bawang putih, cabai, kacang tanah goreng, dan gula merah.","\n",
                       "3. Tambahkan garam, air asam jawa, dan air matang secukupnya. Tuang bumbu halus ke piring.","\n",
                       "4. Sajikan dengan potongan ketupat, tahu goreng, bihun, dan tambahkan kecap serta taburan bawang goreng.Hidangkan bersama kerupuk."]
        elif recipe == "Pecel Sayur":
            langkah = ["1. Rebus semua sayuran yang telah di iris hingga matang.","\n",
                       "2. Tumis bawang, cabai, dan daun jeruk. Lalu haluskan bersama gula merah dan kacang tanah.","\n",
                       "3. Tambahkan larutan asam jawa dan garam secukupnya, aduk hingga rata.",
                       "4. Sajikan sayuran yang telah direbus lalu siram dengan bumbu kacang."]
        elif recipe == "Es Teh":
            langkah = ["1. Isi gelas dengan air panas, lalu celupkan teh.",
                       "2. Tunggu hingga teh larut, tambahkan gula secukupnya dan aduk rata.",
                       "3. Tambahkan es batu, sajikan."]
        elif recipe == "Es Jeruk":
            langkah = ["1. Peras Jeruk dan mauskkan hasil perasan ke dalam gelas.",
                       "2. Tambahkan gula, air, dan es batu secukupnya. Aduk hingga gula larut."]
        elif recipe == "Es Campur":
            langkah = ["1. Potong dadu Roti Tawar,Cincau hitam,Agar-agar,Alpukat,Semangka",
                       "2. Campurkan semua bahan ke dalam mangkok.",
                       "3. Larutkan gula dengan air panas, lalu tuang ke mangkok.",
                       "4. Tambahkan sirup, susu kental manis, dan es batu. Aduk rata."]
        elif recipe == "Wedang Jahe":
            langkah = ["1. Rebus air bersama seluruh bahan dengan api sedang dan tunggu 15 menit.",
                       "2. Jika sudah, angkat dan saring ke dalam gelas.",
                       "3. Tambahkan madu secukupnya. Madu dapat diganti dengan SKM."]
        elif recipe == "Bandrek":
            langkah = ["1. Bersihkan jahe dari kulit, memarkan jahe dan serai.",
                       "2. Rebus air bersama semua bahan, tunggu gula larut dan mendidih.",
                       "3. Jika sudah tuang kedalam gelas, sajikah selagi hangat."]
        elif recipe == "STMJ":
            langkah = ["1. Bersihkan dan kupas jahe, memarkan dan bakar.",
                       "2. Panaskan susu UHT, kental manis, dan jahe. Aduk dan jangan sampai mendidih.",
                       "3. Pisahkan kuning dan putih telur, ambil kuning telur saja.",
                       "4. Masukkan kunign telur kedalam gelas bersama madu.",
                       "5. Tuang campuran susu kedalam gelas, aduk hingga merata."]
        elif recipe == "Kentang Goreng":
            langkah = ["1. Kupas kentang dan bersihkan, potong kentang memanjang.",
                       "2. Rendam kentang dicampuran air dingin dan es batu selama 15 menit.",
                       "3. Angkat dan tiriskan kentang.",
                       "4. Panaskan minyak dengan api sedang, goreng kentang 1/2 matang.",
                       "5. Angkat dan tiriskan kentang.",
                       "6. Goreng kembali kentang dengan api besar.",
                       "7. Jika sudah matang angkat dan tiriskan.",
                       "8. Sajikan dengan bubuk instan/taburi penyedap rasa."]

        for cara in langkah:
            recipe_layout.add_widget(Label(text=cara, text_size=(recipe_popup.width, None), halign='left',valign='top'))
        print(recipe)
            
        recipe_popup.background_color = (125/255,65/255,119/255,1)
        recipe_popup.open()

class RecipeApp(App):
    def build(self):
        return MainMenu()

if __name__ == '__main__':
    RecipeApp().run()
