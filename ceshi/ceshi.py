import unittest
from herostore import Hero

class TestHero(unittest.TestCase):
    def test_init_hero(self):
        milo=Hero(name='milo', hp= 100, act= 10)
        self.assertEqual(milo.hp,100)
        self.assertEqual(milo.act,10)
    def test_hero_say(self):
        hero=Hero(name='hero')
        hero.say()
        self.assertEqual(hero.say(),'superman!')
    def test_act(self):
        milo=Hero(name='milo', hp= 100, act= 10)
        hero=Hero(name='hero')
        milo.act(hero)
        self.assertEqual(hero.hp,990)

unittest.main()
