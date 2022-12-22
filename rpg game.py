answer_yes = ["Yes", "Y", "yes", "y"]
answer_no = ["No", "N", "no", "n"]

print("""
WELCOME! LET'S START THE ADVENTURE

You Elric the almighty are standing outside of the sorcerers castle with your sword in hand ready to go

Will you face the sorcerer. (Yes / No)
""")

ans1 = input(">>")

if ans1 in answer_yes:
    print("\nAfter fighting many of the sorcerer minions you find yourself half way the tower. do you keep going up?  (Yes / No)\n")

    ans2 = input(">>")

    if ans2 in answer_yes:
        print("\nYou reach the tnop of the castle, you fight the sorcerer only for him to slip and fall down the  stairs. You won the Game")

    elif ans2 in answer_no:
        print("\nYou run down the stairs tripping over a dead minions leg falling to your demise. GAME OVER")

    else:
        print("\nYou typed the wrong input. GOODBYE!")

elif ans1 in answer_no:
    print("\nare you sure you want leave and let the sorcerer ruin christmas? (Yes / No)\n")

    ans3 = input(">>")

    if ans3 in answer_yes:
        print("\nCongrats! christmas is now ruined GAME OVER!.")

    elif ans3 in answer_no:
        print("\n You open the door only to see the sorcerer waiting behind the castles door with his army and he strikes you down in a quick flash GAME OVER")

    else:
        print("\nYou typed the wrong input. GOODBYE!")

else:
    print("\nYou typed the wrong input. GOODBYE!")