# Script name:      romain_clemencon_R00193006_project.py
# Author:           Romain Clemencon
# Student Number:   R00193006
# Group:            COMP1B Y
# Description:      SOFT6018 Project

from math import inf
folder_name = ""
file_name = ""
WIDTH = 4
# Emojis
WAVING = "\U0001F44B"
EARTH = "\U0001F30D"
SATURN = "\U0001FA90"
WARNING = "\U000026A0"
# Colors
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
RESET = "\033[m"

while True:
    try:
        print(f"{GREEN}1: Add a new hero"
              f"\n{BLUE}2: View details of hero"
              f"\n{MAGENTA}3: Quit")
        choice = int(input(f"{RESET}=>> "))

        if choice == 1:
            print(f"{GREEN}")
            overwrite = 0
            hero_name = input("What's your hero name (press Enter to return to menu) => ").lower()

            while hero_name.isspace():
                print(f"{RED}The hero name can't be empty spaces.\n")
                hero_name = input(f"{GREEN}What's your hero name (press Enter to return to menu) => ").lower()

            while True:
                try:
                    exist = open(f'''{hero_name.lower().replace(" ", "_")}.txt''', "r")
                    exist.close()
                except FileNotFoundError:           # if the hero doesn't exist
                    break                           # the program will proceed
                else:
                    print(f"'{hero_name.title()}' is already on our file")
                    prev_name = hero_name
                    hero_name = input(f"-> type 'overwrite' if you want to this hero information."
                                      f"\n-> or try another Hero name (press Enter to return to menu)=> ").lower()
                    if hero_name == 'overwrite':
                        overwrite += 1              # Store if the Hero was overwritten
                        hero_name = prev_name       # if the hero is overwritten
                        break                       # keep previous name and continue the program

            if hero_name == "":
                continue                            # Using continue to go back to the menu

            hero_aka = input(f"\nAlso known as => ")
            hero_power = input(f"\nDescribe your power => ")
            print(f"\nAre you"
                  f"\n1: from Earth {EARTH}"
                  f"\n2: not from Earth {SATURN}")

            while True:
                try:
                    hero_origin = int(input(f"{GREEN}=> "))
                    if 1 <= hero_origin <= 2:
                        break
                    print("Please input 1 or 2.")
                except ValueError:
                    print(f"{RED}Only numbers please!")

            if hero_origin == 1:
                hero_origin = EARTH
            elif hero_origin == 2:
                hero_origin = SATURN

            print(f"\nAre you from"
                  f"\n1: DC"
                  f"\n2: Marvel Comics")

            # No need to ask if he is from Marvel or DC
            if overwrite == 0:
                while True:
                    try:
                        hero_comics = int(input("=> "))
                        if 1 <= hero_comics <= 2:
                            break
                        print(f"{GREEN}Please input 1 or 2.")
                    except ValueError:
                        print(f"{RED}Only numbers please!")

                if hero_comics == 1:
                    hero_comics = "DC"
                elif hero_comics == 2:
                    hero_comics = "Marvel"

            # If the hero has not been overwritten, add him to the list
                with open(f"{hero_comics}.txt", "a") as hero_list:
                    print(hero_name.title(), file=hero_list)

            with open(f'''{hero_name.replace(" ", "_")}.txt''', "w", encoding="utf-8") as hero:
                print(f"{'':<{WIDTH}}{'Name':<{(len(hero_name) + 5)}s}{'Power':<{(len(hero_power) + 5)}s}"
                      f"{'AKA':<{(len(hero_aka))}s}", file=hero)
                print(f"{'=' * ((len(hero_name) + len(hero_power) + len(hero_aka)) + 14 )}", file=hero)
                print(f"{hero_origin:<{WIDTH - 1}}{hero_name:<{(len(hero_name) + 5)}s}"
                      f"{hero_power:<{(len(hero_power) + 5)}s}{hero_aka:<{(len(hero_aka) + 3)}s}", file=hero)
            print("")                                                   # Jumping line to make it more readable

        elif choice == 2:
            print(f"{BLUE}")

            dc_num = 0
            marvel_num = 0
            dc_heroes = ""
            marvel_heroes = ""
            hero_tuple = ""
            exist = ""

            # Counting the number of DC and Marvel heroes and adding them to a respective tuple
            with open("DC.txt", "r") as count_dc_r:
                for d in count_dc_r:
                    dc_num += 1
                    dc_heroes = d.lower().rstrip() + ', ' + dc_heroes
            with open("Marvel.txt", "r") as count_marvel_r:
                for m in count_marvel_r:
                    marvel_num += 1
                    marvel_heroes = m.lower().rstrip() + ', ' + marvel_heroes

            total_heroes = dc_num + marvel_num

            if total_heroes == 0:
                print("There are no heroes on records.")
                break

            print("\nIs your hero from:"
                  f"\n1: DC"
                  f"\n2: Marvel Comics"
                  f"\n3: Return to main menu")

            # Checking if one list is empty
            while True:
                try:
                    hero_comics = int(input("=> "))
                    if 1 <= hero_comics <= 2:
                        if hero_comics == 1 and dc_num == 0:
                            print(f"There are no DC heroes.")
                        elif hero_comics == 2 and marvel_num == 0:
                            print(f"There are no Marvel heroes.")
                        else:
                            break
                    elif hero_comics == 3:
                        break
                    print("Please input 1, 2 or 3.")
                except ValueError:
                    print("Only numbers please!")

            if hero_comics == 1:
                file_name = "DC.txt"
                hero_tuple = dc_heroes
            elif hero_comics == 2:
                file_name = "Marvel.txt"
                hero_tuple = marvel_heroes
            elif hero_comics == 3:
                continue

            print("\nPlease choose an hero from the following list:")
            print("=" * 46)
            with open(file_name, "r") as hero_list:
                for x in hero_list:
                    print(f">>  {x.rstrip()}")

            # Not letting opening every heroes, only the one from the list selected
            while True:
                try:
                    choice = input(f"\n{BLUE}Choose your hero (press Enter to return to the menu) => ")
                    if choice == "":
                        break
                    elif choice.lower() in hero_tuple:
                        exist = open(f'''{choice.lower().replace(" ", "_")}.txt''', "r", encoding="utf-8")
                        break
                    elif choice.lower() not in hero_tuple:
                        print(f"{RED}It looks like {choice} is not on our list.\n"
                              f"Please check for any misspell and try again.")
                except FileNotFoundError:
                    print(f"{RED}It looks like {choice} is no longer on our records.\n"  # if the hero doesn't exist
                          f"Please try again with another hero.")  # it will repeat

            if choice == "":
                continue

            print('')
            for x in exist:
                print(x.rstrip())
            print('')
            exist.close()

        elif choice == 3:
            print(f"{MAGENTA}")

            dc_num = 0
            marvel_num = 0
            max_hero = -inf
            min_hero = inf
            longest = ""
            shortest = ""
            p_longest = ""
            p_smallest = ""
            count_longest = 0
            count_smallest = 0
            plural_longest = ""
            plural_smallest = ""

            with open("DC.txt", "r") as count_dc_r:
                for d in count_dc_r:
                    dc_num += 1
                    if len(d.rstrip()) > max_hero:
                        longest = d.rstrip()
                        max_hero = len(d.rstrip())
                    elif len(d.rstrip()) == max_hero and d.rstrip() != p_longest:
                        longest = longest + ", " + d.rstrip()
                        count_longest += 1
                    p_longest = d.rstrip()
                    if len(d.rstrip()) < min_hero:
                        shortest = d.rstrip()
                        min_hero = len(d.rstrip())
                    elif len(d.rstrip()) == min_hero and d.rstrip() != p_smallest:
                        shortest = shortest + ", " + d.rstrip()
                        count_smallest += 1
                    p_smallest = d.rstrip()

            with open("Marvel.txt", "r") as count_marvel_r:
                for m in count_marvel_r:
                    marvel_num += 1
                    if len(m.rstrip()) > max_hero:
                        longest = m.rstrip()
                        max_hero = len(m.rstrip())
                    elif len(m.rstrip()) == max_hero and m.rstrip() != p_longest:
                        longest = longest + ", " + m.rstrip()
                        count_longest += 1
                    p_longest = m.rstrip()
                    if len(m.rstrip()) < min_hero:
                        shortest = m.rstrip()
                        min_hero = len(m.rstrip())
                    elif len(m.rstrip()) == min_hero and m.rstrip() != p_smallest:
                        shortest = shortest + ", " + m.rstrip()
                        count_smallest += 1
                    p_smallest = m.rstrip()

            total_heroes = dc_num + marvel_num

            if total_heroes > 1:
                if count_longest > 0:
                    plural_longest = "s"
                if count_smallest > 0:
                    plural_smallest = "s"
            if total_heroes == 0:
                print("There are no heroes on records.")

            elif total_heroes > 0:

                if dc_num > 0 and marvel_num == 0:
                    if dc_num == 1:
                        print(f"There's only a DC hero on record.")
                        print(f"Which is: {longest}.")
                    elif dc_num > 1:
                        print(f"There are only DC heroes, and they are {dc_num}.")
                        if longest == shortest:
                            print(f"Which are {longest}, same length {len(longest.split(',')[0])}")
                        else:
                            print(
                                f"longest name{plural_longest} ({len(longest.split(',')[0])} char length)"
                                f" = {longest}")
                            print(
                                f"Shortest name{plural_smallest} ({len(shortest.split(',')[0])} char length)"
                                f" = {shortest}")

                elif marvel_num > 0 and dc_num == 0:
                    if marvel_num == 1:
                        print(f"There's only a Marvel hero on record.")
                        print(f"Which is: {longest}.")
                    elif marvel_num > 1:
                        print(f"There are only Marvel heroes, and they are {marvel_num}.")
                        if longest == shortest:
                            print(f"Which are {longest}, same length {len(longest.split(',')[0])}")
                        else:
                            print(
                                f"longest name{plural_longest} ({len(longest.split(',')[0])} char length)"
                                f" = {longest}")
                            print(
                                f"Shortest name{plural_smallest} ({len(shortest.split(',')[0])} char length)"
                                f" = {shortest}")

                else:
                    dc_percent = (dc_num / total_heroes) * 100
                    marvel_percent = (marvel_num / total_heroes) * 100
                    print(f"There are {total_heroes} super heroes on record.")
                    print(
                        f"DC heroes make up {dc_percent:.2f}%\n"
                        f"Marvel Comics heroes make up {marvel_percent:.2f}%\n"
                        f"For a total of {total_heroes} heroes.")
                    if longest == shortest:
                        print(f"Which are {longest}, same length {len(longest.split(',')[0])}")
                    else:
                        print(f"longest name{plural_longest} ({len(longest.split(',')[0])} char length)"
                              f" = {longest}.")
                        print(f"Shortest name{plural_smallest} ({len(shortest.split(',')[0])} char length)"
                              f" = {shortest}.")
            print(f"{WAVING} Good Bye! {WAVING}")
            break
        else:
            print(f"{RED}{WARNING} Please input 1, 2 or 3.")
    except ValueError:
        print(f"{RED}{WARNING} No letter!")
