import random
import time
from colorama import Fore
health = 100
hunger = 50
day = 30
inventory = ["🪓", "🧪", "🍗", "🍖", "🥩"]
def waiting():
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(2)
def inventory_showing():
    print(Fore.CYAN + f"Inventory: {inventory}")
    time.sleep(2)
def bad_ans():
    global health, hunger, day
    print("Wrong answer ❌")
    time.sleep(1)
    print(Fore.RED + "You lose health...")
    day -= 1
    hunger -= 10
    health -= 25
def good_ans():
    global day
    print("Good answer ✅")
    time.sleep(1)
    print(Fore.GREEN + "You leave safe and sound 😌.")
    day -= 1
def heal():
    global health
    if "🧪" in inventory:
        if health == 100:
            print(Fore.RED + "You cannot have more than 100 HP !")
            time.sleep(2)
        else:
            print(Fore.MAGENTA + "Healing in progress")
            waiting()
            print(Fore.GREEN + "Healing successful !")
            health += 25
            inventory.remove("🧪")
            time.sleep(2)
    else:
        print(Fore.RED + "You don't have any healing potions !")
        time.sleep(2)
def eating():
    global hunger
    if "🍗" or "🍖" or "🥩" in inventory:
        if hunger == 50:
            print(Fore.RED + "You are not hungry")
            time.sleep(1)
        else:
            while True:
                print(Fore.RESET + "1) Eat chicken leg 🍗 (+10 Hunger)")
                print("2) Eat meat on a bone 🍖 (+20 Hunger)")
                print("3) Eat red meat 🥩 (+40 Hunger) ")
                choice_meat = input("")
                if choice_meat == "1":
                    if "🍗" not in inventory:
                        print(Fore.RED + "You don't have any chicken leg 🍗 in your inventory !")
                        time.sleep(2)
                        break
                    else:
                        print(Fore.MAGENTA + "Eating")
                        waiting()
                        print(Fore.GREEN + "+ 10 Hunger")
                        hunger += 10
                        inventory.remove("🍗")
                        time.sleep(2)
                        break
                elif choice_meat == "2":
                    if "🍖" not in inventory:
                        print(Fore.RED + "You don't have any meat on a bone 🍖 in your inventory !")
                        time.sleep(2)
                        break
                    else:
                        hunger += 20
                        if hunger > 50:
                            hunger = 50
                            print(Fore.MAGENTA + "Eating")
                            waiting()
                            print(Fore.GREEN + "You ate some of the meat on a bone 🍖. ")
                            time.sleep(2)
                            print(Fore.YELLOW + "However, you threw the rest away as you were already full.")
                            inventory.remove("🍖")
                            time.sleep(2)
                            break

                        else:
                            print(Fore.MAGENTA + "Eating")
                            waiting()
                            print(Fore.GREEN + "+ 20 Hunger")
                            inventory.remove("🍖")
                            time.sleep(2)
                            break
                elif choice_meat == "3":
                    if "🥩" not in inventory:
                        print(Fore.RED + "You don't have any red meat 🥩 in your inventory !")
                        time.sleep(2)
                        break
                    else:
                        hunger += 40
                        if hunger > 50:
                            hunger = 50
                            print(Fore.MAGENTA + "Eating")
                            waiting()
                            print(Fore.GREEN + "You ate some of the red meat 🥩. ")
                            time.sleep(2)
                            print(Fore.YELLOW + "However, you threw the rest away as you were already full.")
                            inventory.remove("🥩")
                            time.sleep(2)
                            break

                        else:
                            print(Fore.MAGENTA + "Eating")
                            waiting()
                            print(Fore.GREEN + "+ 40 Hunger")
                            inventory.remove("🥩")
                            time.sleep(2)
                            break
                else:
                    print(Fore.RED + "Unknown command !")
                    time.sleep(1)
    else:
        print(Fore.RED + "You have nothing to eat !")
def chance():
    global day
    day_won = 0
    print(Fore.GREEN + "Here, you can reduce the number of days you have left to survive.")
    time.sleep(3)
    print(Fore.RESET + "Each successful attempt removes 2 days.")
    time.sleep(2)
    print("After each success, you can:")
    time.sleep(2)
    print("1) Continue to try to win more.")
    time.sleep(2)
    print("2) Stop and keep your winnings.")
    time.sleep(2)
    print(Fore.RED + "⚠️ If you continue and lose, you lose all the days you gained.")
    time.sleep(3)
    print(Fore.RESET + f"\nRemaining days: {day}")
    while True:
        print(Fore.RESET + "1) Try to reduce the days")
        print("2) Quit")
        choice_day = input("")
        if choice_day == "1":
            randomness_game = random.randint(1, 4)
            print(Fore.MAGENTA + "Randomness in progress")
            waiting()
            if randomness_game <= 3:
                print(Fore.GREEN + "Luck was on your side, you gained 2 days.")
                day_won -= 2
                time.sleep(2)
                while True:
                    print(Fore.RESET + "\n1) Continue ")
                    print("2) Stop")
                    choice_day = input("")
                    if choice_day == "1":
                        randomness_game = random.randint(1, 4)
                        print(Fore.MAGENTA + "Randomness in progress")
                        waiting()
                        if randomness_game <= 3:
                            print(Fore.GREEN + "Luck was on your side, you gained 2 days. ")
                            day_won -= 2
                            time.sleep(2)
                        else:
                            print(Fore.YELLOW + "Luck was not on your side...")
                            time.sleep(2)
                            print("You didn’t stop playing at the right time.")
                            time.sleep(2)
                            print(Fore.RED + f"{-day_won} extra days have been added to your day counter.")
                            day -= day_won
                            return
                    elif choice_day == "2":
                        print(Fore.GREEN + f"You gained {-day_won} fewer days.")
                        day += day_won
                        time.sleep(2)
                        print(Fore.GREEN + "See you next time !")
                        return
                    else:
                        print(Fore.RED + "Unknown command !")
                        time.sleep(1)
            else:
                print(Fore.YELLOW + "Luck was not on your side...")
                day += 2
                time.sleep(2)
                break
        elif choice_day == "2":
            print(Fore.GREEN + "See you next time !")
            time.sleep(2)
            break
        else:
            print(Fore.RED + "Unknown command !")
            time.sleep(1)

def forest():
    global health, hunger, day
    randomness_forest = random.randint(1,4)
    print(Fore.GREEN + "Forest exploration in progress")
    waiting()
    if randomness_forest == 1:
        print(Fore.RED + "A monster stands in front of you !!!")
        time.sleep(2)
        while True:
            print(Fore.RESET + "1) Fight")
            print(Fore.RESET + "2) Do not fight")
            choice_fight = input("")
            if choice_fight == "1":
                if "🪓" in inventory:
                    randomness_forest_fight = random.randint(1,2)
                    print(Fore.MAGENTA + "Fight in progress")
                    waiting()
                    if randomness_forest_fight == 1:
                        if "🛡️" in inventory:
                            print(Fore.YELLOW + "The monster is winning the fight...")
                            time.sleep(2.5)
                            while True:
                                print(Fore.RESET + "1) Use the shield")
                                print("2) Do not use the shield")
                                choice_fight_shield = input("")
                                if choice_fight_shield == "1":
                                    print(Fore.GREEN + "You managed to protect yourself with the shield 💪.")
                                    day -= 1
                                    hunger -= 10
                                    inventory.remove("🛡️")
                                    time.sleep(2)
                                    return
                                elif choice_fight_shield == "2":
                                    print(Fore.RED + "You lost the fight and your axe...")
                                    day -= 1
                                    health -= 25
                                    hunger -= 10
                                    inventory.remove("🪓")
                                    time.sleep(2)
                                    return
                                else:
                                    print(Fore.RED + "Unknown command !")
                                    time.sleep(1)
                        else:
                            health -= 25
                            hunger -= 10
                            inventory.remove("🪓")
                            print(Fore.RED + "You lost the fight and your axe...")
                            day -= 1
                            time.sleep(2)
                            break

                    else:
                        random_dropped_weapon = random.randint(1,5)
                        if random_dropped_weapon == 1:
                            print(Fore.GREEN + "Congratulations, you won the fight 🎉")
                            time.sleep(2)
                            print("The monster had an axe before dying, which you swap for your broken one 🪓")
                            day -= 1
                            hunger -= 10
                            time.sleep(3)
                            break
                        elif random_dropped_weapon == 2:
                            print(Fore.GREEN + "Congratulations, you won the fight 🎉")
                            time.sleep(2)
                            print("The monster had a shield that you add to your inventory 🛡️.")
                            time.sleep(3)
                            print(Fore.RED + "But unfortunately, during the fight, your sword broke...")
                            inventory.append("🛡️")
                            inventory.remove("🪓")
                            day -= 1
                            hunger -= 10
                            time.sleep(2)
                            break
                        elif random_dropped_weapon == 3:
                            print(Fore.GREEN + "Congratulations, you won the fight 🎉.")
                            time.sleep(2)
                            print("You obtained a healing potion from the monster and added it to your inventory 🧪. ")
                            inventory.append("🧪")
                            day -= 1
                            hunger -= 10
                            time.sleep(3)
                            break
                        elif random_dropped_weapon == 4:
                            print(Fore.GREEN + "Congratulations, you won the fight 🎉.")
                            time.sleep(2)
                            print("The monster had a chicken leg, you grab it and add it to your inventory 🍗. ")
                            inventory.append("🍗")
                            day -= 1
                            hunger -= 10
                            time.sleep(3)
                            break
                        else:
                            print(Fore.GREEN + "Congratulations, you won the fight 🎉.")
                            time.sleep(2)
                            print("The monster had meat on a bone, you grab it and add it to your inventory 🍖. ")
                            inventory.append("🍖")
                            day -= 1
                            hunger -= 10
                            time.sleep(3)
                            break
                else:
                    print(Fore.RED + "You can't fight without a sword, so you run away.")
                    hunger -= 10
                    time.sleep(2)
                    break
            elif choice_fight == "2":
                print(Fore.MAGENTA + "Fleeing in progress")
                waiting()
                hunger -= 10
                break
            else:
                print(Fore.RED + "Unknown command !")
                time.sleep(1)

    elif randomness_forest == 2:
        print(Fore.GREEN + "You spot a chest !")
        time.sleep(2)
        while True:
            print(Fore.RESET + "1) Open")
            print("2) Don't open")
            choice_chest = input("")
            if choice_chest == "1":
                randomness_chest = random.randint(1,2)
                if randomness_chest == 1:
                    random_object_chest = random.randint(1, 3)
                    if random_object_chest == 1:
                        print(Fore.GREEN + "You found a shield 🛡️.")
                        inventory.append("🛡️")
                        day -= 1
                        time.sleep(1)
                        break
                    elif random_object_chest == 2:
                        print(Fore.GREEN + "You found an axe 🪓.")
                        inventory.append("🪓")
                        day -= 1
                        time.sleep(1)
                        break
                    else:
                        print(Fore.GREEN + "You found a healing potion 🧪")
                        inventory.append("🧪")
                        day -= 1
                        time.sleep(1)
                        break
                else:
                    print(Fore.RED + "A monster jumps out of the chest and attacks you !")
                    time.sleep(2)
                    if "🪓" in inventory:
                        randomness_fight_chest = random.randint(1,2)
                        print(Fore.MAGENTA + "Fight in progress")
                        waiting()
                        if randomness_fight_chest == 1:
                            print(Fore.GREEN + "You won the fight 🎉.")
                            day -= 1
                            hunger -= 10
                            time.sleep(2)
                            break
                        else:
                            if "🛡️" in inventory:
                                print(Fore.YELLOW + "The monster is winning the fight...")
                                time.sleep(2.5)
                                while True:
                                    print(Fore.RESET + "1) Use the shield")
                                    print("2) Don't use the shield")
                                    choice_fight_shield = input("")
                                    if choice_fight_shield == "1":
                                        print(Fore.GREEN + "You managed to protect yourself with the shield 💪.")
                                        day -= 1
                                        hunger -= 10
                                        inventory.remove("🛡️")
                                        time.sleep(2)
                                        return
                                    elif choice_fight_shield == "2":
                                        print(Fore.RED + "You lost the fight ☠️.")
                                        day -= 1
                                        health -= 25
                                        hunger -= 10
                                        time.sleep(2)
                                        return
                                    else:
                                        print(Fore.RED + "Unknown command !")
                                        time.sleep(1)
                            else:
                                print(Fore.RED + "The monster made you lose HP ☠️.")
                                day -= 1
                                health -= 25
                                hunger -= 10
                                time.sleep(2)
                                break
                    else:
                        if "🛡️" in inventory:
                            print(Fore.YELLOW + "The monster is defeating you...")
                            time.sleep(2)
                            while True:
                                print(Fore.RESET + "1) Use the shield")
                                print("2) Don't use the shield")
                                choice_fight_shield = input("")
                                if choice_fight_shield == "1":
                                    print(Fore.GREEN + "You managed to protect yourself with the shield 💪.")
                                    day -= 1
                                    hunger -= 10
                                    inventory.remove("🛡️")
                                    time.sleep(2)
                                    return
                                elif choice_fight_shield == "2":
                                    print(Fore.RED + "The monster made you lose HP ☠️")
                                    day -= 1
                                    health -= 25
                                    hunger -= 10
                                    time.sleep(2)
                                    return
                                else:
                                    print(Fore.RED + "Unknown command !")
                                    time.sleep(1)

                        else:
                            print(Fore.RED + "The monster made you lose HP ☠️")
                            hunger -= 10
                            health -= 25
                            day -= 1
                            time.sleep(2)
                            break
            elif choice_chest == "2":
                randomness_no_chest = random.randint(1,2)
                if randomness_no_chest == 1:
                    randomness_no_chest_object = random.randint(1, 3)
                    if randomness_no_chest_object == 1:
                        print(Fore.YELLOW + "If you had opened the chest, it would have contained an axe 🪓.")
                        time.sleep(3)
                        break
                    elif randomness_no_chest_object == 2:
                        print(Fore.YELLOW + "If you had opened the chest, it would have contained a shield 🛡️.")
                        time.sleep(3)
                        break
                    else:
                        print(Fore.YELLOW + "If you had opened the chest, it would have contained a healing potion 🧪.")
                        time.sleep(3)
                        break
                else:
                    print(Fore.GREEN + "If you had opened the chest, a monster would have jumped at your face 😅")
                    time.sleep(3)
                    break
            else:
                print(Fore.RED + "Unknown command !")
                time.sleep(1)
    elif randomness_forest == 3:
        print(Fore.RED + "You fell into a trap 🪤.")
        randomness_trap = random.randint(1, 5)
        time.sleep(2)
        print(Fore.YELLOW + "Solve this riddle. ")
        time.sleep(2)
        if randomness_trap == 1:
            print(Fore.RESET + "You are taking part in a race. You overtake the person in second place.")
            time.sleep(3)
            print("You are now...")
            time.sleep(1)
            while True:
                print(Fore.RESET + "A) 1st")
                print("B) 2nd")
                print("C) 3rd")
                choice_trap = input("Choice (A/B/C): ").upper()
                if choice_trap == "A":
                    bad_ans()
                    break
                elif choice_trap == "B":
                    good_ans()
                    break
                elif choice_trap == "C":
                    bad_ans()
                    break
                else:
                    print(Fore.RED + "Unknown command !")
                    time.sleep(1)
        elif randomness_trap == 2:
            print(Fore.RESET + "A man looks at a photograph and says: ")
            time.sleep(2)
            print("I have neither a brother nor a sister, but this person's father is my father's son.")
            time.sleep(4)
            print("Who's on the picture ?")
            time.sleep(1)
            while True:
                print(Fore.RESET + "A) His son")
                print("B) His father")
                print("C) himself")
                choice_trap = input("Choice (A/B/C): ").upper()
                if choice_trap == "A":
                    good_ans()
                    break
                elif choice_trap == "B":
                    bad_ans()
                    break
                elif choice_trap == "C":
                    bad_ans()
                    break
                else:
                    print(Fore.RED + "Unknown command !")
                    time.sleep(1)
        elif randomness_trap == 3:
            print(Fore.RESET + "I am always ahead of you, but you can never catch me.")
            time.sleep(3)
            print("Who am I ?")
            time.sleep(1)
            while True:
                print(Fore.RESET + "A) Your past")
                print("B) Your future")
                print("C) Your shadow")
                choice_trap = input("Choice (A/B/C): ").upper()
                if choice_trap == "A":
                    bad_ans()
                    break
                elif choice_trap == "B":
                    good_ans()
                    break
                elif choice_trap == "C":
                    bad_ans()
                    break
                else:
                    print(Fore.RED + "Unknown command !")
                    time.sleep(1)
        elif randomness_trap == 4:
            print(Fore.RESET + "A man lives on the 10th floor of a building.")
            time.sleep(2)
            print("Every morning, he takes the elevator down to the ground floor.")
            time.sleep(4)
            print("In the evening, when he comes home:")
            time.sleep(1)
            print("He takes the elevator up to the 7th floor.")
            time.sleep(2)
            print("Then he takes the stairs up to the 10th floor.")
            time.sleep(2)
            print("Except on rainy days: on those days, he goes directly to the 10th floor by elevator.")
            time.sleep(4)
            print("Why ?")
            time.sleep(1)
            while True:
                print(Fore.RESET + "A) The elevator is broken between the 7th and 10th floors.")
                print("B) He is too short to reach the 10th-floor button.")
                print("C) He prefers to get some exercise.")
                choice_trap = input("Choice (A/B/C): ").upper()
                if choice_trap == "A":
                    bad_ans()
                    break
                elif choice_trap == "B":
                    good_ans()
                    break
                elif choice_trap == "C":
                    bad_ans()
                    break
                else:
                    print(Fore.RED + "Unknown command !")
                    time.sleep(1)
        else:
            print(Fore.RESET + "A farmer has 17 sheep.")
            time.sleep(1)
            print("All except 9 run away.")
            time.sleep(1)
            print("How many sheep are left? ?")
            time.sleep(1.5)
            while True:
                print(Fore.RESET + "A) 8")
                print("B) 9")
                print("C) 17")
                choice_trap = input("Choice (A/B/C): ").upper()
                if choice_trap == "A":
                    bad_ans()
                    break
                elif choice_trap == "B":
                    good_ans()
                    break
                elif choice_trap == "C":
                    bad_ans()
                    break
                else:
                    print(Fore.RED + "Unknown command !")
                    time.sleep(1)
    else:
        print(Fore.RESET + "You find yourself in front of a cave !")
        time.sleep(2)
        print(Fore.GREEN + "As you venture into the cave, if you choose the right directions, you will be rewarded.")
        time.sleep(3)
        print(Fore.YELLOW + "However, if you make a mistake,")
        time.sleep(1.5)
        print(Fore.RED + "You could lose HP.")
        time.sleep(2)
        while True:
            print(Fore.RESET + "1) Enter the cave")
            print("2) Do not enter")
            choice_cave = input("")
            if choice_cave == "1":
                print(Fore.MAGENTA + "Entering the cave")
                waiting()
                for loop in range (1, 6):
                    print(Fore.RESET + "1) Go right")
                    print("2) Go left")
                    choice_direction_cave = input()
                    if choice_direction_cave == "1":
                        print(Fore.MAGENTA + "Exploration in progress")
                        waiting()
                        random_right = random.randint(1,4)
                        if random_right <= 3:
                            if loop == 5:
                                randomness_end_cave = random.randint(1,3)
                                if randomness_end_cave == 1:
                                    print(Fore.GREEN + "You found red meat 🥩 at the very back of the cave.")
                                    day -= 1
                                    hunger -= 10
                                    inventory.append("🥩")
                                    time.sleep(2)
                                    return
                                elif randomness_end_cave == 2:
                                    print(Fore.GREEN + "You reduced your adventure time by 5 days 📅. ")
                                    day -= 5
                                    hunger -= 10
                                    time.sleep(2)
                                    return
                                else:
                                    print(Fore.GREEN + "You found three healing potions 🧪🧪🧪 at the bottom of the cave.")
                                    day -= 1
                                    hunger -= 10
                                    inventory.append("🧪")
                                    inventory.append("🧪")
                                    inventory.append("🧪")
                                    time.sleep(2)
                                    return
                            else:
                                print(Fore.YELLOW + "You find yourself facing two paths.")
                                time.sleep(2)
                        else:
                            print(Fore.RED + "A monster emerges from the path and attacks you.")
                            time.sleep(2)
                            if "🪓" in inventory:
                                randomness_cave_fight = random.randint(1,2)
                                print(Fore.MAGENTA + "Fight in progress")
                                waiting()
                                if randomness_cave_fight == 1:
                                    print(Fore.GREEN + "You won the fight 🎉")
                                    day -= 1
                                    hunger -= 10
                                    time.sleep(2)
                                    return

                                else:
                                    if "🛡️" in inventory:
                                        print(Fore.YELLOW + "The monster is winning the fight...")
                                        time.sleep(2)
                                        while True:
                                            print(Fore.RESET + "1) Use the shield")
                                            print("2) Don't use the shield")
                                            choice_fight_shield = input("")
                                            if choice_fight_shield == "1":
                                                print(Fore.GREEN + "You managed to protect yourself with the shield 💪.")
                                                day -= 1
                                                hunger -= 10
                                                inventory.remove("🛡️")
                                                time.sleep(2)
                                                return
                                            elif choice_fight_shield == "2":
                                                print(Fore.RED + "You lost the fight ☠️")
                                                day -= 1
                                                health -= 25
                                                hunger -= 10
                                                time.sleep(2)
                                                return
                                            else:
                                                print(Fore.RED + "Unknown command")
                                                time.sleep(1)
                                    else:
                                        print(Fore.RED + "The monster made you lose HP ☠️")
                                        hunger -= 10
                                        health -= 25
                                        day -= 1
                                        time.sleep(2)
                                        return
                            else:
                                if "🛡️" in inventory:
                                    print(Fore.YELLOW + "The monster is defeating you...")
                                    time.sleep(2)
                                    while True:
                                        print(Fore.RESET + "1) Use the shield")
                                        print("2) Don't use the shield")
                                        choice_fight_shield = input("")
                                        if choice_fight_shield == "1":
                                            print(Fore.GREEN + "You managed to protect yourself with the shield 💪.")
                                            day -= 1
                                            hunger -= 10
                                            inventory.remove("🛡️")
                                            time.sleep(2)
                                            return
                                        elif choice_fight_shield == "2":
                                            print(Fore.RED + "You lost the fight ☠️")
                                            day -= 1
                                            health -= 25
                                            hunger -= 10
                                            time.sleep(2)
                                            return
                                        else:
                                            print(Fore.RED + "Unknown command")
                                            time.sleep(1)
                                else:
                                    print(Fore.RED + "The monster made you lose HP ☠️")
                                    hunger -= 10
                                    health -= 25
                                    day -= 1
                                    time.sleep(2)
                                    return
                    elif choice_direction_cave == "2":
                        print(Fore.MAGENTA + "Exploration in progress")
                        waiting()
                        random_left = random.randint(1, 4)
                        if random_left <= 3:
                            if loop == 5:
                                randomness_end_cave = random.randint(1, 3)
                                if randomness_end_cave == 1:
                                    print(Fore.GREEN + "You found red meat 🥩 at the very back of the cave.")
                                    day -= 1
                                    hunger -= 10
                                    inventory.append("🥩")
                                    return
                                elif randomness_end_cave == 2:
                                    print(Fore.GREEN + "You reduced your adventure time by 5 days 📅. ")
                                    day -= 5
                                    hunger -= 10
                                    time.sleep(2)
                                    return
                                else:
                                    print(Fore.GREEN + "You found three healing potions 🧪🧪🧪 at the bottom of the cave.")
                                    day -= 1
                                    hunger -= 10
                                    inventory.append("🧪")
                                    inventory.append("🧪")
                                    inventory.append("🧪")
                                    time.sleep(2)
                                    return
                            else:
                                print(Fore.YELLOW + "You find yourself facing two paths.")
                                time.sleep(2)
                        else:
                            print(Fore.RED + "A monster emerges from the path and attacks you.")
                            time.sleep(2)
                            if "🪓" in inventory:
                                randomness_cave_fight = random.randint(1, 2)
                                print(Fore.MAGENTA + "Fight in progress")
                                waiting()
                                if randomness_cave_fight == 1:
                                    print(Fore.GREEN + "You won the fight 🎉")
                                    day -= 1
                                    hunger -= 10
                                    time.sleep(2)
                                    return
                                else:
                                    if "🛡️" in inventory:
                                        print(Fore.YELLOW + "The monster is winning the fight...")
                                        time.sleep(2)
                                        while True:
                                            print(Fore.RESET + "1) Use the shield")
                                            print("2) Don't use the shield")
                                            choice_fight_shield = input("")
                                            if choice_fight_shield == "1":
                                                print(Fore.GREEN + "You managed to protect yourself with the shield 💪.")
                                                day -= 1
                                                hunger -= 10
                                                inventory.remove("🛡️")
                                                time.sleep(2)
                                                return
                                            elif choice_fight_shield == "2":
                                                print(Fore.RED + "You lost the fight ☠️")
                                                day -= 1
                                                health -= 25
                                                hunger -= 10
                                                time.sleep(2)
                                                return
                                            else:
                                                print(Fore.RED + "Unknown command")
                                                time.sleep(1)
                                    else:
                                        print(Fore.RED + "The monster made you lose HP ☠️")
                                        hunger -= 10
                                        health -= 25
                                        day -= 1
                                        time.sleep(2)
                                        return
                            else:
                                if "🛡️" in inventory:
                                    print(Fore.YELLOW + "The monster is defeating you...")
                                    time.sleep(2)
                                    while True:
                                        print(Fore.RESET + "1) Use the shield")
                                        print("2) Don't use the shield")
                                        choice_fight_shield = input("")
                                        if choice_fight_shield == "1":
                                            print(Fore.GREEN + "You managed to protect yourself with the shield 💪.")
                                            day -= 1
                                            hunger -= 10
                                            inventory.remove("🛡️")
                                            time.sleep(2)
                                            return
                                        elif choice_fight_shield == "2":
                                            print(Fore.RED + "You lost the fight ☠️")
                                            day -= 1
                                            health -= 25
                                            hunger -= 10
                                            time.sleep(2)
                                            return
                                        else:
                                            print(Fore.RED + "Unknown command")
                                            time.sleep(1)
                                else:
                                    print(Fore.RED + "The monster made you lose HP ☠️")
                                    hunger -= 10
                                    health -= 25
                                    day -= 1
                                    time.sleep(2)
                                    return
                    else:
                        print(Fore.RED + "Unknown command !")
                        time.sleep(1)
            elif choice_cave == "2":
                print(Fore.MAGENTA + "Fleeing in progress")
                waiting()
                hunger -= 10
                break
            else:
                print(Fore.RED + "Unknown command !")
                time.sleep(1)


print(Fore.GREEN + "=================")
print("  30 days alone  ")
print("=================")
time.sleep(2.5)
print(Fore.RESET + "You find yourself alone in an unfamiliar forest.")
time.sleep(2)
print("Survive for 30 days")
time.sleep(1)


while True:
    print(Fore.RESET + "═══════════════════════════════")
    print(Fore.RESET + f"Days remaining: {day}")
    if health >25:
        print(Fore.GREEN + f"Health: {health}")
    else:
        print(Fore.RED + f"Health: {health}")
    if hunger > 15:
        print(Fore.GREEN + f"Hunger: {hunger}")
    else:
        print(Fore.RED + f"Hunger: {hunger}")
    print(Fore.RESET + "═══════════════════════════════")
    print(Fore.RESET + "1) Explore the forest 🌲")
    print("2) Open inventory 🎒")
    print("3) Heal ❤️‍🩹")
    print("4) Try your luck 🎲")
    print("5) Eat 🍕")
    action = input("")
    if action == "1":
        forest()
    elif action == "2":
        inventory_showing()
    elif action == "3":
        heal()
    elif action == "4":
        chance()
    elif action == "5":
        eating()


    if health <= 0 or hunger <= 0:
        print("GAME OVER 🕹️😭❌")
        time.sleep(1)
        print("Nice Try")
        time.sleep(1)
        break
    if day <= 0:
        print("\nYou made it! 🎉 ")
        time.sleep(1)
        print("You survived 30 days in the forest 🏕️")
        time.sleep(2)
        print("Thanks for playing 🙌")
        break
