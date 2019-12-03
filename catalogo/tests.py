from django.test import TestCase
from catalogo.models import Game, Platform, Developer
from django.contrib.auth.models import User
# Create your tests here.
class GameModelTest(TestCase):

    @classmethod 
    def setUp(self):
        d1= Developer.objects.create(name = 'Riot Games')
        d2= Developer.objects.create(name = 'Digital Extremes')
        self.p1 = Platform.objects.create(name = 'PC')
        self.p2 = Platform.objects.create(name = 'PS5')
      

       	Game.objects.create(title='League of Legends', developer=d1, launch='11/05/2010', summary='Moba Game 5v5', price= 0, platform = self.p1, image='img/lol.jpg',requiriments= 'Not found')
       	Game.objects.create(title='Warframe',Developer=d2, launch='10/10/2009',summary='multiplayer shooter rpg', price=0, platform = self.p2 , image='img/warframe.jpg',requiriments='Not found')

    def test_game_developer(self):
        game1 = Game.objects.get(title='Warframe')
        self.assertEqual(game1.developer.name, 'Digital Extremes')

    def test_game_launch(self):
        game2 = Game.objects.get(title='League of Legends') 
        self.assertEqual(game2.launch, '11/05/2010')


		
