#!/usr/bin/python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

"""
Dice Simultion
5 faces dice
numbers 1-7
"""
import random

def roll_dice(): #Function that rolls dice
    dice_faces = (1, 2, 3, 4, 5, 6, 7) #7 faces dice
    face = random.randint(1,7)

    return face

if __name__ == "__main__":
    print(roll_dice())
        
