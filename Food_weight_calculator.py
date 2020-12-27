from datetime import date

# Dog's date of birth in format YYYY,M,D.
# IMPORTANT! do not add zeros for single digit days or months.
# Correct examples:
# 2017.7.7
# 2011.11.11
age = date.today()-date(2018,8,25) 

ageDays = age.days
ageWeeks = round(age.days / 7)
print("----------------- COMPLETE RAW DIET -----------------")
print("")
print("The dog is", ageWeeks, "weeks now.")
print("")
weight = int(input("Enter the dog's weight in KG here: "))


def foodCalc(dogWeight, dogAge):
    if dogAge >= 16 and dogAge < 20:
        food = dogWeight * 0.065
        percentage = "6.5%"
    elif dogAge >= 20 and dogAge < 24:
        food = dogWeight * 0.055
        percentage = "5.5%"
    elif dogAge >= 24 and dogAge < 36:
        food = dogWeight * 0.045
        percentage = "4.5%"
    elif dogAge >= 36 and dogAge < 56:
        food = dogWeight * 0.035
        percentage = "3.5%"
    elif dogAge >= 56 and dogAge < 68:
        food = dogWeight * 0.03
        percentage = "3%"
    elif dogAge > 68:
        food = dogWeight * 0.02
        percentage = "2%"
    food = food * 1000
    food = round(food)
    meat = food * 0.8
    meat = round(meat)
    mince = meat * 0.75
    mince = round(mince)
    muscle = meat * 0.2
    muscle = round(muscle)
    fish = meat * 0.15
    fish = round(fish)
    offal = food * 0.1
    offal = round(offal)
    bone = food * 0.1
    bone = round(bone)
    print("")
    print("")
    print("Feed around", food,"grams of raw food. This should be", percentage, "of his body weight.")
    print("")
    print("Daily norm should contain:")
    print("")
    print("----------------- 1 -----------------")
    print("A total of", meat,"grams of meat combined of:")
    print("")
    print(mince, "grams of beef, chicken, lamb etc.")
    print(muscle,"grams of muscle like tripe, heart, tongue,")
    print(fish, "grams of fish like sardines.")
    print("")
    print("----------------- 2 -----------------")
    print(offal,"grams of organs. Half of which needs to be liver and half other, like kidney, spleen, brain, etc.")
    print("")
    print("----------------- 3 -----------------")
    print(bone, "grams of bone wings, ribs, necks, carcass.")
    print("")
    print("")
    print("--------- Norms per meal 1/3 ---------")
    print("Total weight of the bowl -", round(food/3), "grams.")
    print(round(mince/3), "grams of meat (e.g. beef).")
    print(round(muscle/3),"grams of other meat (e.g. tripe).")
    print(round(fish/3), "grams of fish (e.g. sardines).")
    print(round(offal/3),"grams of organs (e.g. liver + kidney).")
    print(round(bone/3), "grams of bone (e.g. chicken bone).")
    print("")
    print("More info at https://www.rfas.uk/puppy-starter-guide") 
    print("")
    print("--------- Price estimates ---------")
    print("")
    price = (mince/1000*2.04) + (muscle/1000*2.8) + (offal/1000*2.8) + (fish/1000*4.5) + (bone/1000*1.65)
    price = round(price, 2)
    monthlyPrice = price * 30
    monthlyPrice = round(monthlyPrice, 2)
    print("Price is estimated to be £", price, "per day")
    print("or £", monthlyPrice, "per month based on a month with 30 days.")
    print("")
foodCalc(weight, ageWeeks)
