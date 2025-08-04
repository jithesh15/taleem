from itertools import permutations
import soldier_exception

class Unit:
    """
    Abstract base class for a combat unit.
    """
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def strength(self, opponent_type):
        """
        Base strength method, optionally overridden.
        """
        return self.count


class Soldier(Unit):
    """
    Represents a specific soldier with a possible advantage against others.
    """
    # Static dictionary for advantages
    advantage_map = {
        "Militia": ["Spearmen", "LightCavalry"],
        "Spearmen": ["LightCavalry", "HeavyCavalry"],
        "LightCavalry": ["FootArcher", "CavalryArcher"],
        "HeavyCavalry": ["Militia", "FootArcher", "LightCavalry"],
        "CavalryArcher": ["Spearmen", "HeavyCavalry"],
        "FootArcher": ["Militia", "CavalryArcher"]
    }

    def has_advantage(self, opponent_type):
        return opponent_type in Soldier.advantage_map.get(self.name, [])

    def strength(self, opponent_type):
        """
        Calculate effective strength. Doubled if advantage exists.
        """
        if self.has_advantage(opponent_type):
            return self.count * 2
        return self.count


class Army:
    """
    Represents a collection of soldiers.
    """
    def __init__(self, data_string):
        self.units = self.parse(data_string)

    def parse(self, data_string):
        """
        Converts string like 'Militia#10;Spearmen#20' into Soldier objects.
        """
        return [
            Soldier(name, int(count))
            for unit in data_string.split(';') if unit
            for name, count in [unit.split('#')]
        ]


class Battle:
    """
    Handles battle logic between two armies.
    """
    def __init__(self, our_army: Army, opponent_army: Army):
        self.our_army = our_army.units
        self.opp_army = opponent_army.units
        if len(self.our_army) != len(self.opp_army):
            raise SoldierException("Soldier count got mismatched need to be a fair battle, please Try again")

    def compare_strength(self, our_strength, opp_strength):
        return our_strength > opp_strength

    def fight(self):
        """
        Tries all permutations of our units to match opponent order.
        Returns the win count of the first successful winning permutation (3+ wins).
        """
        for arrangement in permutations(self.our_army):
            win_count = 0
            for our_unit, opp_unit in zip(arrangement, self.opp_army):
                if self.compare_strength(our_unit.strength(opp_unit.name), opp_unit.count):
                    win_count += 1
            if win_count >= 3:
                return win_count
        return 0


def main():
    """
    Main function simulating a battle and printing the result.
    """
    while True:
        
        # Input data
        our_data = input("our_soldiers :")
        opp_data = input("opp_soldiers :")

        try:
            # Create armies
            our_army = Army(our_data)
            opp_army = Army(opp_data)

            # Run battle
            battle = Battle(our_army, opp_army)
            result = battle.fight()
        except SoldierException as e:
            print(f"{e}")
            continue    
        except Exception as e:
            raise ValueError(f"Unexpected error while parsing {e}")

        # Output result
        print("Number of wins:", result)

        exit = input("Wish to contine the battle 1 to continue")
        if exit != '1':
            break


if __name__ == "__main__":
    main()
