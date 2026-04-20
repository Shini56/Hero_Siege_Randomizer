from hero import Heroes
from skills import skillset
from copy import deepcopy
import random

#Picks a Random Hero out the hero.py
selectedHero = (random.choice(Heroes))

#makes a copy of the choosen Hero to keep the original data
heroChoice = (selectedHero.copy())

#Takes the choosen hero and looks up the right skillset and puts it as a copy into skillChoice
def skillChoice(heroChoice):

    skill_name = heroChoice["skillset"]

    selectedSkills = deepcopy(skillset[skill_name])

    return selectedSkills

#checks if Hero level is below 100 and increases it for 1 if it is below 100.
def levelUp(heroChoice):

    if heroChoice["heroLevel"] < 100:
        heroChoice["heroLevel"] += 1
        return True

    return False


def availableSkills(heroChoice, skillChoice):
    
    available = []

    for skill in skillChoice:

        # checks if the hero level is higher then the level for the skill to unlock
        if skill["unlockLevel"] <= heroChoice["heroLevel"]:

            # checks if the choosen skill is under max level
            if skill["currentLevel"] < skill["maxLevel"]:

                # checks if the skill need skills to unlock
                requirements = skill["requirements"]

                # if there are none then it gets approven directly
                if not requirements:
                    available.append(skill)

                else:
                    reqMet = True

                    for req in requirements:
                        found = False

                        for s in skillChoice:
                            if s["name"] == req:
                                found = True
                                if s["currentLevel"] < 1:
                                    reqMet = False
                                break

                        # in case the req skill doesnt exist
                        if not found:
                            reqMet = False

                    if reqMet:
                        available.append(skill)

    return available



def skillUp(available):
    if not available:
        print("No skills avaible anymore!")
        return None

    chosenSkill = random.choice(available)
    chosenSkill["currentLevel"] += 1

    print("Choosen:", chosenSkill["name"], "-> Level:", chosenSkill["currentLevel"])
    return chosenSkill


# Max skills Randomizer Option. Chooses 5 skills
maxSkillList = []


# Choice for Skill 1 basic level 0 Skill
def firstSkillChoice(maxSkillList, skillChoice):
    
    skillList = []

    for skill in skillChoice:
    
        if skill["unlockLevel"] == 0:
        
            skillList.append(skill)

    if skillList:
        chosenSkill = random.choice(skillList)
        maxSkillList.append(chosenSkill)

    return maxSkillList


# Choice for Skill 2 under Level 20 to be safe to have 2 Skills
def secondSkillChoice(maxSkillList, skillChoice):
        
    skillList = []

    for skill in skillChoice:

        if skill["unlockLevel"] < 20:
            
            if skill not in maxSkillList:

                
                if not skill["requirements"]:
                    skillList.append(skill)

                else:
                    reqMet = True

                    for req in skill["requirements"]:
                        found = False

                        for s in maxSkillList:
                            if s["name"] == req:
                                found = True
                                break

                        if not found:
                            reqMet = False

                    if reqMet:
                        skillList.append(skill)

    if skillList:
        chosenSkill = random.choice(skillList)
        maxSkillList.append(chosenSkill)
    
    return maxSkillList


# The last 3 skills to have 5 for Max Leveling
def thirdSkillChoice(maxSkillList, skillChoice):

    skillList = []

    for skill in skillChoice:
            
        if skill not in maxSkillList:

            # Requirement Check
            if not skill["requirements"]:
                skillList.append(skill)

            else:
                reqMet = True

                for req in skill["requirements"]:
                    found = False

                    for s in maxSkillList:
                        if s["name"] == req:
                            found = True
                            break

                    if not found:
                        reqMet = False

                if reqMet:
                    skillList.append(skill)

    while len(maxSkillList) < 5 and skillList:

        chosenSkill = random.choice(skillList)
        maxSkillList.append(chosenSkill)

        skillList.remove(chosenSkill)

    return maxSkillList