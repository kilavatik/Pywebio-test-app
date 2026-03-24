import random
import os
import time
from pywebio import *
from pywebio.output import *
from pywebio.input import *
from keyboard import *
def main():
    class Monsters:
        def __init__(self, mobLvl, mobName, mobDamage, mobHP, mobImage):
            self.mobLvl = mobLvl
            self.mobName = mobName
            self.mobDamage = mobDamage
            self.mobHP = mobHP
            self.mobImage = mobImage
        def Getinfo(self):
            return f'{self.mobName} {self.mobLvl} {self.mobHP}, {self.mobDamage}'

    class Weapon:
        def __init__(self, title, damage, price, nameImage):
            self.title = title
            self.damage = damage
            self.price = price
            self.nameImage = nameImage

        def GetInfo(self):
            return f"{self.title}, цена: {self.price}, урон: {self.damage}"

        def GetInfoInv(self):
            return f"{self.title}, урон: {self.damage}"

    class Armor:
        def __init__(self, title, armorstats, price, nameImage):
            self.title = title
            self.armorstats = armorstats
            self.price = price
            self.nameImage = nameImage

        def GetInfo(self):
            return f'{self.title}, цена: {self.price}, защита: {self.armorstats}'

        def GetInfoInv(self):
            return f'{self.title}, защита: {self.armorstats}'

    class Potion:
        def __init__(self, title, regen, price, nameImage):
            self.title = title
            self.regen = regen
            self.price = price
            self.nameImage = nameImage

        def GetInfo(self):
            return f'{self.title}, цена: {self.price}, лечение: {self.regen}'

        def GetInfoInv(self):
            return f'{self.title}, лечение: {self.regen}'

    logins = []
    with open("logins.txt", "r") as file:
        loginsMas = str(file.readline())
        logins = loginsMas.split(" ")
    print(logins)
    weapons = [Weapon('обычный клинок', 1, 15, 'swordcommon.png'), Weapon('клинок Алекса', 3, 45, 'swordalex.png'),
               Weapon('клинок Гудини', 5, 75, 'swordgydini.png'),
               Weapon("обычный лук", 2, 30, '2309152.png'), Weapon('лук Алекса', 4, 60, '2309152.png'),
               Weapon('лук Гудини', 6, 90, '2309152.png')]
    armors = [Armor('Обычный доспех', 1, 15, "armorwarrior.png"), Armor('Доспех воина', 3, 45, 'armorcrusader.png'),
              Armor('Доспех короля', 5, 75, 'armorking.png'),
              Armor('Божественный доспех', 7, 105, 'armorgods.png'),
              Armor('Доспех Алекса', 9, 135, 'armoralex.png'),
              Armor('Доспех Гудини', 10, 150, 'armorgydini.png')]
    potions = [Potion('маленькое лечебное зелье', 20, 10, "healsmall.png"),
               Potion('среднее лечебное зелье', 45, 15, 'healmidle.png'),
               Potion('большое лечебное зелье', 80, 20, 'healbig.png')]
    money = 1000
    weaponlist = list()
    armorlist = list()
    potionlist = list()
    lvl = 1
    mobLvl = int(random.randrange(lvl-1, lvl+2))
    playerWeapon = 0
    damage = 5+(5/10*lvl)+playerWeapon
    hp =100
    exp = 0
    needExp = 50
    playerArmor = 0
    while True:
        if mobLvl == 0:
             mobLvl = int(random.randrange(lvl - 1, lvl + 3))
        else:
             break
    mobName = ["Слизь", "Зомби", "Скелет", "Паук"]
    mobDamage = [int(1+(1/10*mobLvl))-playerArmor, int(8+(8/10*mobLvl))-playerArmor, int(10+(10/10*mobLvl))-playerArmor,
                 int(7+(7/10*mobLvl))-playerArmor]
    mobHP = [int(10+(10/10*mobLvl)), int(20+(20/10*mobLvl)), int(20+(20/10*mobLvl)),
             int(15+(15/10*mobLvl))]
    clear()
    while True:

        put_image(open("Redemption.png","rb").read())
        menu = actions("Меню",["Старт","Выход"])
        if menu == "Старт":
            menu = actions("Меню:", ["Вход", "Регистрация"])
            if menu == "Регистрация":
                while True:
                    login = input("Введите ваш логин")
                    if login in logins:
                        toast("Такой логин уже занят", color="red")
                    else:
                        break
                name = input("Введите ваше имя: ")
                while True:
                    password = input("Введите ваш пароль")
                    passwordControl = input("Повторите ваш пароль")
                    if password == passwordControl:
                        break
                    else:
                        toast("Пароли не совпадают!", color="red")
                put_markdown("**Выбор персонажа**")
                put_image(open("Воин.gif","rb").read())
                put_markdown("**Воин**")
                put_image(open("Варвар.gif","rb").read())
                put_markdown("**Варвар**")
                player = actions("Выбор персонажа", ["Воин", "Варвар"])
                player+=".gif"
                toast("Игра началась.", color="Gold")
                logins.append(login)
                with open("logins.txt", "w") as file:
                    for loginX in logins:
                        file.write(f" {loginX}")
                with open(f"{login}.txt", "w") as file:
                            file.write("")
            elif menu == "Вход":
                while True:
                    login = input("Введите ваш логин")
                    if login in logins:
                        with open(f"{login}.txt", "r") as file:
                            acc = str(file.readline()).split("|")
                        print(acc)
                        break
                    else:
                        toast("Такого пользователя не найдено!", color="red")
                while True:
                    password = input("Введите ваш пароль")
                    if password == acc[0]:
                        name = acc[1]
                        player = acc[2]
                        lvl = int(acc[3])
                        money = int(acc[4])
                        with open(f"{login}Armor.txt", "r") as File:
                            for armor in File.readlines():
                                if armor != "\n":
                                    armorlist.append(Armor(armor.split("|")[0],int(armor.split("|")[1]),int(armor.split("|")[2]),armor.split("|")[3]))
                        with open(f"{login}Weapon.txt", "r") as File:
                            for weapon in File.readlines():
                                if weapon != "\n":
                                    weaponlist.append(Weapon(weapon.split("|")[0],int(weapon.split("|")[1]),int(weapon.split("|")[2]),weapon.split("|")[3]))
                        with open(f"{login}Potion.txt", "r") as File:
                            for potion in File.readlines():
                                if potion != "\n":
                                    potionlist.append(Potion(potion.split("|")[0],int(potion.split("|")[1]),int(potion.split("|")[2]),potion.split("|")[3]))
                        break
                    else:
                        toast("Не верный пароль!", color="Red")
            while True:
                clear()
                put_image(open("Menu.gif", "rb").read())
                menu2 = actions("Меню",["В бой","В лавку","Домой","В таверну","Персонаж","Выход"])
                clear()
                if menu2 == "В бой":
                    mobLvl = int(random.randrange(lvl - 1, lvl + 3))
                    monsters = [Monsters(mobLvl, 'Слизь', int(1 + (1 / 10 * mobLvl) - playerArmor), int(10 + (10 / 10 * mobLvl)), "Slime.gif"),
                                Monsters(mobLvl, 'Зомби', int(8 + (8 / 10 * mobLvl)-playerArmor), int(20 + (20 / 10 * mobLvl)), "Zombie.gif"),
                                Monsters(mobLvl, 'Одержимый', int(10 + (10 / 10 * mobLvl)) - playerArmor,int(20 + (20 / 10 * mobLvl)), "Possessed.gif"),
                                Monsters(mobLvl, 'Паук', int(10 + (10 / 10 * mobLvl)) - playerArmor, int(15 + (15 / 10 * mobLvl)), "Spider.gif")]
                    mob = int(random.randrange(0, 4))
                    toast(f"на вас напал {monsters[mob].mobName}", color="Black")
                    while monsters[mob].mobHP > 0:
                        if hp <= 0:
                            hp = 0
                            toast("Ваша жизнь на грани", color="Red")
                            break
                        put_text(f"{monsters[mob].mobName} Ур.{monsters[mob].mobLvl} ХП: {monsters[mob].mobHP}")
                        put_image(open(monsters[mob].mobImage, "rb").read())
                        put_text(f"{name} Ур.{lvl} {exp}/{needExp} ХП: {hp}")
                        put_image(open(player, "rb").read())
                        menu3 = actions("Ваши действия",["Атака","Уклонение","Инвентарь","Побег"])
                        if menu3 == "Атака":
                            monsters[mob].mobHP -= damage
                            if monsters[mob].mobHP <= 0:
                                getExp = int(random.randrange(5, 15))
                                exp += getExp
                                getMoney = int(random.randrange(5+mobLvl, 10+mobLvl))
                                money = money + getMoney
                                if exp > needExp:
                                    lvl=lvl+1
                                    exp= exp -needExp
                                    needExp=int(needExp+needExp/10)
                                    toast("Повышение уровня!", color="Green")
                                clear()
                                put_image(open("Victory.png", "rb").read())
                                put_markdown(f"**Получено {getExp} опыта и {getMoney} золота.**")
                                put_markdown("**Нажмите пробел для продолжения**")
                                wait("Space")
                            else:
                                if monsters[mob].mobDamage > 0:
                                    hp -= monsters[mob].mobDamage
                                    toast(f"Вы получили {monsters[mob].mobDamage} урона!", color="Black")
                                else:
                                    toast("Вы избежали урона, ваша защита великолепна!", color="Black")
                            clear()
                        elif menu3 == "Уклонение":
                            if int(random.randrange(0, 100))>50:
                                toast("Вы удачно уклонились!", color="Black")
                                clear()
                            else:
                                clear()
                                put_markdown("**Враг оказался коварнее и предвидел ваши движения!**")
                                toast(f"Вы получили {monsters[mob].mobDamage - playerArmor} урона!")
                                hp -= monsters[mob].mobDamage
                        elif menu3 == "Инвентарь":
                            clear()
                            put_text(f"Имя: {name} Ур. {lvl}Опыт: {exp}/{needExp} ХП: {hp} Урон: {damage} "
                                     f"Защита: {playerArmor} Золотые: {money}")
                            put_image(open(player, "rb").read())
                            masbtn = list()
                            for x in potionlist:
                                masbtn.append(x.GetInfoInv())
                            masbtn.append("Назад")
                            choiseX = actions("Инвентарь:", masbtn)
                            if choiseX == "Назад":
                                clear()
                                continue
                            for x in potionlist:
                                if choiseX == x.GetInfoInv():
                                    hp += x.regen
                                    potionlist.remove(x)
                                    toast(f"Вы выпили {x.title}", color="Black")
                                    if hp > 100:
                                        hp = 100
                        elif menu3 == "Побег":
                            clear()
                            if int(random.randrange(0, 100))>50:
                                toast("Вы удачно сбежали!")
                                break
                            else:
                                put_text(f"Вам не удалось бежать!")
                                toast(f"Вы получили {mobDamage[mob]+playerArmor} урона!")
                                hp-=mobDamage[mob]+playerArmor
                elif menu2 == "В лавку":
                    while True:
                        clear()
                        put_image(open("Shop.gif", "rb").read())
                        choice1 = actions("меню", ['оружие', 'броня', 'зелья', 'выйти из магазина'])
                        if choice1 == "оружие":
                            while True:
                                clear()
                                put_image(open("Shop.gif", "rb").read())
                                put_text(f'Ваши деньги: ', money)
                                choice2 = select("Какое оружие вы пожелаете?",
                                                 options=[weapons[0].GetInfo(), weapons[1].GetInfo(),
                                                          weapons[2].GetInfo(), weapons[3].GetInfo(),
                                                          weapons[4].GetInfo(), weapons[5].GetInfo(), 'назад'])
                                if choice2 == 'назад':
                                    break
                                for x in weapons:
                                    if x.GetInfo() == choice2:
                                        if x.price <= money:
                                            put_image(open(x.nameImage, 'rb').read(), width="300")
                                            confirm = actions(f"вы уверенны,что хотите купить {x.title}?",
                                                              ['да', 'нет'])
                                            if confirm == 'нет':
                                                put_text(f'а жаль, {x.title} неплохое оружие')
                                            elif confirm == "да":
                                                money -= x.price
                                                toast(f'вы купили {x.title}', color="Black")
                                                weaponlist.append(x)
                                                break
                                        else:
                                            toast(f'подкопите ещё {x.price - money} монет на {x.title}', color='Red')
                        elif choice1 == "броня":
                            while True:
                                clear()
                                put_image(open("Shop.gif", "rb").read())
                                put_text(f'Ваши деньги: ', money)
                                choice2 = select("Какую броню вы пожелаете?",
                                                 options=[armors[0].GetInfo(), armors[1].GetInfo(),
                                                          armors[2].GetInfo(), armors[3].GetInfo(),
                                                          armors[4].GetInfo(), armors[5].GetInfo(),
                                                          'назад'])
                                if choice2 == 'назад':
                                    break
                                for x in armors:
                                    if x.GetInfo() == choice2:
                                        if x.price <= money:
                                            put_image(open(x.nameImage, 'rb').read(), width="300")
                                            confirm = actions(f"вы уверенны,что хотите купить {x.title}?",
                                                              ['да', 'нет'])
                                            if confirm == 'нет':
                                                put_text(f'а жаль, {x.title} неплохо защищает от урона')
                                            elif confirm == "да":
                                                money -= x.price
                                                toast(f'вы купили {x.title}', color="Black")
                                                armorlist.append(x)
                                                break
                                        else:
                                            toast(
                                                f'{x.title} не бесплатный, найди ещё {x.price - money} монет или уходи',
                                                color="Red")
                        elif choice1 == "зелья":
                            while True:
                                clear()
                                put_image(open("Shop.gif", "rb").read())
                                put_text(f'Ваши деньги: ', money)
                                choice2 = select("Какое зелье хотите купить?",
                                                 options=[potions[0].GetInfo(), potions[1].GetInfo(),
                                                          potions[2].GetInfo(), 'назад'])
                                if choice2 == 'назад':
                                    break
                                for x in potions:
                                    if x.GetInfo() == choice2:
                                        if x.price <= money:
                                            put_image(open(x.nameImage, 'rb').read(), width="300")
                                            confirm = actions(f"вы уверенны,что хотите купить {x.title}?",
                                                              ['да', 'нет'])
                                            if confirm == 'нет':
                                                put_text(f'А зря, {x.title} быстро ставит на ноги')
                                            elif confirm == "да":
                                                money -= x.price
                                                toast(f'вы купили {x.title}', color="Black")
                                                potionlist.append(x)
                                                break
                                        else:
                                            toast(
                                                f'вам не хватает ровно {x.price - money} монет на {x.title}',
                                                color='Red')
                        elif choice1 == "выйти из магазина":
                            break
                elif menu2 == "Домой":
                    put_text("Идёт востановление...")
                    put_image(open("Home.gif", "rb").read())
                    time.sleep(100-hp)
                    toast("Вы поправились!", color="Green")
                elif menu2 == "В таверну":
                    clear()
                    put_image(open("Tavern.gif", "rb").read())
                    menu4 = actions("Добро пожаловать!\n Не желаете укрепить своё здоровье за счёт огненной воды?\n"
                                    "Цена: 5",["Да","Нет"])
                    if menu4 == "Да":
                        if money >= 5:
                            money = money - 5
                            hp = 100
                            toast("Ваше здоровье востановленно!", color="Green")
                        else:
                            toast("Возвращайся, когда деньги будут!", color="Black")
                    elif menu4 == "Нет":
                        toast("Очень жаль, прощайте", color="Black")
                    clear()
                elif menu2 == "Персонаж":
                    while True:
                        clear()
                        put_text(f"Имя:{name} Ур.:{lvl} Опыт:{exp}/{needExp} ХП:{hp} Урон: {damage} Защита: {playerArmor} "
                                 f"Золотые: {money}")
                        put_image(open(player, "rb").read())
                        menu5 = actions("Меню", ["Оружие","Броня","Предметы","Назад"])
                        if menu5 == "Оружие":
                            while True:
                                clear()
                                put_text(f"Имя:{name} Ур.:{lvl} Опыт:{exp}/{needExp} ХП:{hp} Урон: {damage} "
                                         f"Защита: {playerArmor} Золотые: {money}")
                                put_image(open(player, "rb").read())
                                masbtn = list()
                                for x in weaponlist:
                                    masbtn.append(x.GetInfoInv())
                                masbtn.append("Назад")
                                choiseX = actions("Инвентарь:", masbtn)
                                if choiseX == "Назад":
                                    break
                                for x in weaponlist:
                                    if choiseX == x.GetInfoInv():
                                        playerWeapon = x.damage
                                        toast(f"Вы надели {x.title}", color="Black")
                                        damage = 5 + (5 / 10 * lvl) + playerWeapon
                        elif menu5 == "Броня":
                            while True:
                                clear()
                                put_text(f"Имя:{name} Ур.:{lvl} Опыт:{exp}/{needExp} ХП:{hp} Урон: {damage} "
                                         f"Защита: {playerArmor} Золотые: {money}")
                                put_image(open(player, "rb").read())
                                masbtn = list()
                                for x in armorlist:
                                    masbtn.append(x.GetInfoInv())
                                masbtn.append("Назад")
                                choiseX = actions("Инвентарь:", masbtn)
                                if choiseX == "Назад":
                                    break
                                for x in armorlist:
                                    if choiseX == x.GetInfoInv():
                                        playerArmor = x.armorstats
                                        toast(f"Вы надели {x.title}", color="Black")
                        elif menu5 == "Предметы":
                            while True:
                                clear()
                                put_text(f"Имя:{name} Ур.:{lvl} Опыт:{exp}/{needExp} ХП:{hp} Урон: {damage} "
                                         f"Защита: {playerArmor} Золотые: {money}")
                                put_image(open(player, "rb").read())
                                masbtn = list()
                                for x in potionlist:
                                    masbtn.append(x.GetInfoInv())
                                masbtn.append("Назад")
                                choiseX = actions("Инвентарь:", masbtn)
                                if choiseX == "Назад":
                                    break
                                for x in potionlist:
                                    if choiseX == x.GetInfoInv():
                                        hp += x.regen
                                        potionlist.remove(x)
                                        toast(f"Вы выпили {x.title}", color="Black")
                                        if hp > 100:
                                            hp = 100
                        elif menu5 == "Назад":
                            break
                elif menu2 == "Выход":
                    with open(f"{login}.txt", "w") as File:
                        File.write(f"{password}|{name}|{player}|{lvl}|{money}")
                    with open(f"{login}Weapon.txt", "a") as File:
                        for weapon in weaponlist:
                            File.write(f"\n{weapon.title}|{weapon.damage}|{weapon.price}|{weapon.nameImage}")
                    with open(f"{login}Armor.txt", "a") as File:
                        for armor in armorlist:
                            File.write(f"\n{armor.title}|{armor.armorstats}|{armor.price}|{armor.nameImage}")
                    with open(f"{login}Potion.txT", "a") as File:
                        for potion in potionlist:
                            File.write(f"\n{potion.title}|{potion.regen}|{potion.price}|{potion.nameImage}")
                    break

        elif menu =="Выход":
            put_text("Можете закрыть окно:)")
            break

start_server(main, port=2278, debug=True)