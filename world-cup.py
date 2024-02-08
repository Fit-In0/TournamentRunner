import random
import re


countries = {
    "Argentina": 1,
    "France": 2,
    "England": 3,
    "Belgium": 4,
    "Brazil": 5,
    "Netherlands": 6,
    "Portugal": 7,
    "Spain": 8,
    "Italy": 9,
    "Croatia": 10,
    "Uruguay": 11,
    "USA": 12,
    "Morocco": 13,
    "Colombia": 14,
    "Mexico": 15,
    "Germany": 16,
    "Japan": 17,
    "Switzerland": 18,
    "Denmark": 19,
    "Senegal": 20,
    "IR Iran": 21,
    "Ukraine": 22,
    "Korea Republic": 23,
    "Austria": 24,
    "Australia": 25,
    "Sweden": 26,
    "Hungary": 27,
    "Tunisia": 28,
    "Wales": 29,
    "Algeria": 30,
    "Poland": 31,
    "Ecuador": 32
}

country_list = []
for _ in countries.keys():
    country_list.append(_)

group_stage_data = []




class Group():
    def pots(self):
        self.pot1 = []
        self.pot2 = []
        self.pot3 = []
        self.pot4 = []

        length = len(countries)
        pot_length = int(length / 4)
        for _ in countries:
            if countries[_] <= pot_length:
                self.pot1.append(_)
            if countries[_] > pot_length and countries[_] <= pot_length * 2:
                self.pot2.append(_)
            if countries[_] > pot_length * 2 and countries[_] <= pot_length * 3:
                self.pot3.append(_)
            if countries[_] > pot_length * 3 and countries[_] <= pot_length * 4:
                self.pot4.append(_)
        
        
            

    def groups_divide(self, pot):
        return list(zip(*[iter(pot)] * 1))

    def groups(self):
        slots = [1, 2, 3, 4, 5, 6, 7, 8]
        self.group1 = []
        self.group2 = []
        self.group3 = []
        self.group4 = []
        self.group5 = []
        self.group6 = []
        self.group7 = []
        self.group8 = []
        groups = self.groups_divide(self.pot1)
        for _ in groups:
            for i in _:
                _slot = random.choice(slots)
                self.check_slot(_slot, i)
                slots.remove(_slot)
        groups = self.groups_divide(self.pot2)
        slots = [1, 2, 3, 4, 5, 6, 7, 8]
        for _ in groups:
            for i in _:
                _slot = random.choice(slots)
                self.check_slot(_slot, i)
                slots.remove(_slot)
        groups = self.groups_divide(self.pot3)
        slots = [1, 2, 3, 4, 5, 6, 7, 8]
        for _ in groups:
            for i in _:
                _slot = random.choice(slots)
                self.check_slot(_slot, i)
                slots.remove(_slot)
        groups = self.groups_divide(self.pot4)
        slots = [1, 2, 3, 4, 5, 6, 7, 8]
        for _ in groups:
            for i in _:
                _slot = random.choice(slots)
                self.check_slot(_slot, i)
                slots.remove(_slot)

        return self.group1, self.group2, self.group3, self.group4, self.group5, self.group6, self.group7, self.group8

    def check_slot(self, slot, i):
        if slot == 1:
            self.group1.append(i)
        elif slot == 2:
            self.group2.append(i)
        elif slot == 3:
            self.group3.append(i)
        elif slot == 4:
            self.group4.append(i)
        elif slot == 5:
            self.group5.append(i)
        elif slot == 6:
            self.group6.append(i)
        elif slot == 7:
            self.group7.append(i)
        elif slot == 8:
            self.group8.append(i)

def win_loss(x, y):
    countries_keys = list(countries.keys())
    print(f"{countries_keys[x-1]} vs {countries_keys[y-1]}")
    if x > y:
        difference = x - y
        difference *= 3.1935483871
        y_percentage = 100 - difference
        if random.randint(0, 100) <= y_percentage:
            print(f"{countries_keys[y-1]} wins!")
            return y
        else:
            print(f"{countries_keys[x-1]} wins!")
            return x

    if y > x:
        difference = y - x
        difference *= 3.1935483871
        x_percentage = 100 - difference
        if random.randint(0, 100) <= x_percentage:
            print(f"{countries_keys[x-1]} wins!")
            return x
        else:
            print(f"{countries_keys[y-1]} wins!")
            return y
        
def group_stage(groups):
    qualifiers = []
    for _ in groups:
        win_records = []
        games_left = [[0,1], [0,2], [0,3], [1,2], [1,3], [2,3]]
        group = {
            0: _[0],
            1: _[1],
            2: _[2],
            3: _[3],
        }
        records = {
            _[0]: [0,0],
            _[1]: [0,0],
            _[2]: [0,0],
            _[3]: [0,0]
        }
        for i in games_left:
            team1 = group[i[0]]
            team2 = group[i[1]]
            win_num = win_loss(countries[team1], countries[team2])
            if win_num == countries[team1]:
                records[team1][0] += 1
                records[team2][1] += 1
            else:
                records[team2][0] += 1
                records[team1][1] += 1
        
        print(records)
        records[_[0]] = records[_[0]][0]
        records[_[1]] = records[_[1]][0]
        records[_[2]] = records[_[2]][0]
        records[_[3]] = records[_[3]][0]
        win_list = [[_[0], records[_[0]]], [_[1], records[_[1]]], [_[2], records[_[2]]], [_[3], records[_[3]]]]
        
        for i in range(0, len(win_list)):
            for j in range(0, len(win_list)-i-1):
                if (win_list[j][1] > win_list[j+1][1]):
                    tempo = win_list[j]
                    win_list[j] = win_list[j+1]
                    win_list[j+1] = tempo

        print(f"Qualifiers: Congratulations to {win_list[2][0]} and {win_list[3][0]}!")
        qualifiers.append(win_list[2][0])
        qualifiers.append(win_list[3][0])
    return qualifiers

def tournament_round_1(qualifiers):
    winners = []
    # A winner vs B runner up, A runner up vs B winner
    countries_keys = list(countries.keys())
    winners.append(countries_keys[win_loss(countries[qualifiers[0]], countries[qualifiers[3]]) - 1])
    winners.append(countries_keys[win_loss(countries[qualifiers[1]], countries[qualifiers[2]]) - 1])
    winners.append(countries_keys[win_loss(countries[qualifiers[4]], countries[qualifiers[7]]) - 1])
    winners.append(countries_keys[win_loss(countries[qualifiers[5]], countries[qualifiers[6]]) - 1])
    winners.append(countries_keys[win_loss(countries[qualifiers[8]], countries[qualifiers[11]]) - 1])
    winners.append(countries_keys[win_loss(countries[qualifiers[9]], countries[qualifiers[12]]) - 1])
    winners.append(countries_keys[win_loss(countries[qualifiers[12]], countries[qualifiers[15]]) - 1])
    winners.append(countries_keys[win_loss(countries[qualifiers[13]], countries[qualifiers[14]]) - 1])
    return winners

def tournament_round_2(qualifiers):
    winners = []
    countries_keys = list(countries.keys())
    winners.append(countries_keys[win_loss(countries[qualifiers[0]], countries[qualifiers[1]]) - 1])
    winners.append(countries_keys[win_loss(countries[qualifiers[2]], countries[qualifiers[3]]) - 1])
    winners.append(countries_keys[win_loss(countries[qualifiers[4]], countries[qualifiers[5]]) - 1])
    winners.append(countries_keys[win_loss(countries[qualifiers[6]], countries[qualifiers[7]]) - 1])
    return winners

def tournament_round_3(qualifiers):
    winners = []
    countries_keys = list(countries.keys())
    winners.append(countries_keys[win_loss(countries[qualifiers[0]], countries[qualifiers[1]]) - 1])
    winners.append(countries_keys[win_loss(countries[qualifiers[2]], countries[qualifiers[3]]) - 1])
    return winners

def tournament_round_4(qualifiers):
    winners = []
    countries_keys = list(countries.keys())
    winners.append(countries_keys[win_loss(countries[qualifiers[0]], countries[qualifiers[1]]) - 1])
    return winners

#Grouping
grouping = Group()
grouping.pots()
g1, g2, g3, g4, g5, g6, g7, g8 = grouping.groups()
groups = [g1, g2, g3, g4, g5, g6, g7, g8]

#Contest
print("Group Stage_____________________________")
qualifiers = group_stage(groups)
print("\n\n\n\n\n\n\n\n\n\n\n\n")
print("Round of 16_____________________________")
print(qualifiers)
qualifiers = tournament_round_1(qualifiers)
print("\n\n\n\n\n\n\n\n\n\n\n\n")
print("Quarterfinals_____________________________")
print(qualifiers)
qualifiers = tournament_round_2(qualifiers)
print(qualifiers)
print("\n\n\n\n\n\n\n\n\n\n\n\n")
print("Semifinals_____________________________")
print(qualifiers)
qualifiers = tournament_round_3(qualifiers)
print(qualifiers)
print("\n\n\n\n\n\n\n\n\n\n\n\n")
print("Finals_____________________________")
print(qualifiers)
qualifiers = tournament_round_4(qualifiers)
print(f"Congratulations! {qualifiers} won the world cup!")
print("\n\n\n\n\n\n\n\n\n\n\n\n")