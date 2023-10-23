from operator import itemgetter

def sort(filename):
    for j in range (2):

        try:
            with open(filename, "r") as file:
                lines = file.readlines()

            data = []
            for line in lines:
                parts = line.strip().split(", ")
                if len(parts) == 7: 
                    accuracy = float(parts[-1][:-1])
                    data.append((accuracy, line))

            data.sort(key=lambda x: x[0], reverse=True)

            with open(filename, "w") as file:
                for _, line in data:
                    file.write(line + "\n")

            print("File sorted by accuracy.")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

filename = "coincount.txt"

def replace_line(filename2, line_number, text):
    with open(filename2) as file:
        lines = file.readlines()


        if (line_number <= len(lines)):


            lines[line_number - 1] = text + "\n"
            with open(filename2, "w") as file:


                for line in lines:
                    file.write(line)

        else:
            print("Line", line_number, "not in file.")
            print("File has", len(lines), "lines.")

def wordcount(filename , list, accuracy):
    try:
        file = open(filename, "r")
        read = file.readlines()
        file.close()
        for word in list:
            lower = word.lower()
            count = 0
            lines = 0
            for sentence in read:
                line = sentence.split()
                lines = lines + 1
                for each in line:
                    line2 = each.lower()
                    line2 = line2.strip("% ,")
                    if lower == line2:
                        count = count + 1
                        if count >= 1:
                            replace_question = ("We already have a") + (" ") + (volunteer) + (" ") + ("in our system. Would you like to update previous entries? Y or N: ")
                            replace = input(replace_question).lower()
                            if replace == "y":
                                print("Your results have been updated")
                                filename2 = "coincount.txt"
                                accuracy = str(accuracy)
                                text = (volunteer) + (", ")  + (coin_type) + (", ")  + str(input_weight_bag) + (", ")  + str(correct) + (", ") + str(incorrect) + (", ") + str(total) + (", ") + (accuracy) + ("%")
                                print(replace_line(filename2 , lines , text))
                                sort(filename)
                                return True
    except FileExistsError:
        print("The file is not there")

end = ""

while end != "n":

    input1 = False
    input2 = False
    input3 = False
    acc_check = False

    while input1 != True:

        volunteer = input("Enter the Volunteer's name: ")

        try:
            volunteer = str(volunteer)

            input1 = volunteer.isalpha()

            if input1 != True:
                print("Please enter a valid name consisting of only letters")

        except Exception as e:
            print(f"An error occurred: {str(e)}")
    
    correct = 0
    incorrect = 0
    quit = ""
    
    while quit != "n":

        coin_list = ["1p", "2p", "5p", "10p", "20p", "50p", "£1", "£2"]
        bag_weight_list = [356, 356, 235, 325, 250, 160, 175, 120]
        coin_weight_list = [3.56, 7.12, 2.35, 6.50, 5.00, 8.00, 8.75, 12.00]

        input2 = False
        input3 = False


        while input2 != True:

            coin_type = input("Enter coin type: ")

            if coin_type != coin_list:
                print("Please enter the coin's type out of the options of 1p, 2p, 5p, 10p, 20p, 50p, £1, £2")

            else:
                input2 = True

        while input3 != True:

            input_weight_bag = input("Enter the weight of the bag: ")

            try:
                coin_type = str(coin_type)

                input_weight_bag = float(input_weight_bag)

                if coin_type != "" or input_weight_bag != "":
                    input2 = True
                else:
                    print("Please enter the weight of the bag")

            except Exception as e:
                print(f"An error occurred: {str(e)}")
                print("Please enter the correct weight of the bag in numbers")
        
        coin_type = coin_type.lower()

        for i in range(len(coin_list)):

            if coin_type == coin_list[i]:
                
                if input_weight_bag == bag_weight_list[i]:
                    print("Correct")
                    correct = correct + 1
                    
                elif input_weight_bag < bag_weight_list[i]:
                    add = bag_weight_list[i] - input_weight_bag
                    coins = add // coin_weight_list[i]
                    coins = int(coins)
                    print("You will need,", coins, "more", coin_list[i], " coins. Please try again after correcting this error.")
                    incorrect = incorrect + 1

                elif input_weight_bag > bag_weight_list[i]:
                    remove = input_weight_bag - bag_weight_list[i]
                    coins = remove // coin_weight_list[i]
                    coins = int(coins)
                    print("You will need,", coins, "less", coin_list[i], "coins. Please try again after correcting this error.")
                    incorrect = incorrect + 1

        quit = input("Would you like to enter another bag? Y or N: ").lower()

    while acc_check != True:

        try:
            total = correct + incorrect
            accuracy = (correct / total) * 100
            accuracy = str(accuracy)
            print("Your accuracy is ", accuracy , "%")
            acc_check = True

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    coin_data = open("coincount.txt","r")
    data = coin_data.read()
    final_data = (data) + ("\n") + (volunteer) + (", ")  + (coin_type) + (", ")  + str(input_weight_bag) + (", ") + str(correct) + (", ") + str(incorrect) + (", ") + str(total) + (", ") + str(accuracy) + ("%")
    coin_data.close()

    replace = wordcount("coincount.txt", [volunteer], accuracy)

    if replace != True:
        coin_data = open("coincount.txt","w")
        coin_data.write(final_data)
        sort("coincount.txt")
        coin_data.close()
        sort(filename)

    coin_data = open("coincount.txt", "r")
    answer = input("Would you like to see the other volunteer's accuracy? Y or N: \n").lower()

    if answer == "y":
        coin_data = open("coincount.txt","r")
        data = coin_data.read()
        print("Name, Coin Type, Weight Entered, Correct, Incorrect, Total, Accuracy\n")
        print(data)
        print("Done")

    else:
        print("Finished")

    end = input("Would you like to input another volunteer's results? Y or N: ").lower()
print("Thank you for your charity work.")