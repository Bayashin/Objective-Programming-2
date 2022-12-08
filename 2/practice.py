hero_header =[]
hero_data = []
with open('lecture02_Hero.csv') as f:
    for line in f:
        if len(hero_header) == 0:
            hero_header = line.rstrip().split(",")
        else :
            data = line.rstrip().split(",")
            hero_data.append(data)

print(hero_header)
print(hero_data)

#csvモジュールを利用
import csv
weapon_header = []
weapon_data = []
with open('lecture02_Weapon.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(weapon_header) == 0:
            weapon_header = row
        else :
            weapon_data.append(row)

print(weapon_header)
print(weapon_data)