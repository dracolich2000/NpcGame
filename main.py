import random
import json

playerhealth = 100
playerattack = 1
playerlevel = 1


NpcCount = list(range(1, 1001))



npclevel = 1


  

  




    

  


      
#Rules of the Game

# 1. King_Infected_Npc has 1000 health, 75 damages
# 2. Primary_Infected_Npc has 100 health, 20 damages.
# 3. Secondary_Infected_Npc has 30 health, 10 damages.
# 4. Strong_Infected_Npc has 5 health, 
# 5. Normal_Infected_Npc has 1 health

# There are 1000 npc in total (excluding Player and Primary_Infected_Npc)
# Player has 100 health in total
# Npc has 1 health in total
# Each round, Player will automatically attack an infected Npc.
# Each round, npc will attack automatically, dealing 1 attack damage to a random Infected_npcs.
# Each round, Infected_npcs will do the same back to either npc or player.
# If player chooses the right answer while the npc chooses wrong, then npc loses whatever health point the player attack at.
# If an Infected_Npc's health reaches 0, it's eliminated.
# If an Npc's health reaches 0, it has 75% chance becoming an infected level based on the type of Infected_Npc or 25% chance getting eliminated.
# If player eliminates all Infected_Npcs, then player wins.
# If player's health reaches 0, then player loses.
# Player has a total stats called "Eliminations".
# Player can upgrade the level of damages, which needs 10 elinations on first level, and 5 additional elimination for further levels. 
# Player can upgrade the level of npcs, so it improves their health and damages, this also needs 10 elinations on first level, and 5 additional elimination for further levels.
# Player can also "heal" 20 health points, which require 25 eliminations.

       #Level 2 Npc will require 70 more Eliminations from the player
       #Level 3 Npc will require 100 more Eliminations from the player
       #Level 4 Npc will require 150 more Eliminations from the player
       #Level 5 Npc will require 250 more Eliminations from the player
       #Level 5 is top level upgrade.

       #This is not possible to code