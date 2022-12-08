import csv

def lecture02_01_printHeroStatus() -> None:
    hero_header =[]
    hero_data = []
    with open('lecture02_Hero.csv') as f:
        for line in f:
            if len(hero_header) == 0:
                hero_header = line.rstrip().split(",")
            else :
                data = line.rstrip().split(",")
                hero_data.append(data)
    for e in hero_data:
        if e[0] == '1':
            print (f"{e[1]}のステータスは" +
                f"HP:{e[2]}," +
                f"MP:{e[3]}," +
                f"Atk:{e[4]}," +
                f"Def:{e[5]}," +
                f"Age:{e[6]}")

def lecture02_01_printWeaponStatus() -> None:
    weapon_header = []
    weapon_data = []
    with open('lecture02_Weapon.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(weapon_header) == 0:
                weapon_header = row
            else :
                weapon_data.append(row)
    for e in weapon_data:
        if e[0] == '1':
            print (f"{e[1]}のステータスは" +
                f"HP:{e[2]}," +
                f"MP:{e[3]}," +
                f"Atk:{e[4]}," +
                f"Def:{e[5]}," +
                f"Age:{e[6]}")

def lecture02_01_printHeroStatusWithWeapon() -> None:
    hero_header = []
    hero_data = []
    with open('lecture02_Hero.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(hero_header) == 0:
                hero_header = row
            else :
                hero_data.append(row)
    for e in hero_data:
        if e[0] == '1':
            hero_name = e[1]
            hero_hp = int(e[2])
            hero_mp = int(e[3])
            hero_atk = int(e[4])
            hero_def = int(e[5])
            hero_age = int(e[6])
            hero_weapon = e[7]

    weapon_header = []
    weapon_data = []
    with open('lecture02_Weapon.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(weapon_header) == 0:
                weapon_header = row
            else :
                weapon_data.append(row)
    for e in weapon_data:
        if e[0] == hero_weapon:
            weapon_name = e[1]
            weapon_hp = int(e[2])
            weapon_mp = int(e[3])
            weapon_atk = int(e[4])
            weapon_def = int(e[5])
            weapon_age = int(e[6])

    print(f"{weapon_name}を装備した{hero_name}のステータスは" +
        f"HP:{hero_hp+weapon_hp}," +
        f"MP:{hero_mp+weapon_mp}," +
        f"Atk:{hero_atk+weapon_atk}," +
        f"Def:{hero_def+weapon_def}," +
        f"Age:{hero_age+weapon_age}")


if __name__ == '__main__':
    lecture02_01_printHeroStatus()
    lecture02_01_printWeaponStatus()
    lecture02_01_printHeroStatusWithWeapon()
