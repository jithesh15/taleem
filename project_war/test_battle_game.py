# test_battle_game.py

import unittest
from battle_game import Army, Battle


class TestBattle(unittest.TestCase):
    def test_battle_with_win(self):
        our_data = "Militia#10;Spearmen#20;LightCavalry#15"
        opp_data = "FootArcher#12;CavalryArcher#10;HeavyCavalry#5"
        our_soldiers = Army(our_data)
        opp_soldiers = Army(opp_data)
        battle = Battle(our_soldiers, opp_soldiers)
        self.assertGreaterEqual(battle.fight(), 3)

    def test_battle_with_loss(self):
        our_data = "Militia#5;Spearmen#5;LightCavalry#5"
        opp_data = "FootArcher#20;CavalryArcher#20;HeavyCavalry#20"
        our_soldiers = Army(our_data)
        opp_soldiers = Army(opp_data)
        battle = Battle(our_soldiers, opp_soldiers)
        self.assertEqual(battle.fight(), 0)

    def test_equal_strength_no_advantage(self):
        our_data = "Militia#10;Spearmen#10;LightCavalry#10"
        opp_data = "Militia#10;Spearmen#10;LightCavalry#10"
        our_soldiers = Army(our_data)
        opp_soldiers = Army(opp_data)
        battle = Battle(our_soldiers, opp_soldiers)
        self.assertEqual(battle.fight(), 0)


if __name__ == '__main__':
    unittest.main()
