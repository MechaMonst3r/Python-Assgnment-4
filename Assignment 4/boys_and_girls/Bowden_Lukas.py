# Name: Luke Bowden
# Student Number: t00040951
# Lab Number: 4
# Date: 2020-10-08
# Description: Reads in a file of boy and girl names then sorts them into their own seperate files.

#Opening all files. One for reading, the others for writing.
names_file = open("babynames2000s.txt", "r");
boyNames_file = open("boynames.txt", "w");
girlNames_file = open("girlnames.txt", "w");
comNames_file = open("comboygirlnames.txt", "w");

#Creating lists to hold boy, girl, and common names.
girl_list = [];
boy_list = [];
comm_list = [];

#Iterates through every line in the names_file
for line in names_file:
    
    #Seperates and appends boy and girl names to their seperate lists
    boy_list.append(line.split()[1].strip() + "\n");
    girl_list.append(line.split()[3].strip() + "\n");
    
    #Creates temporary strings to hold the number of people with those names.
    tempString1 = line.split()[2].strip();
    tempString2 = line.split()[4].strip();
    
    #Converts temp strings to numbers and if they are over a certain threshold, appends to common names list.
    if(int(tempString1.replace(',', '')) >= 100000):
        comm_list.append(line.split()[1].strip() + "\n");
    
    if(int(tempString2.replace(',', '')) >= 100000):
        comm_list.append(line.split()[3].strip() + "\n");

#Closes main file for reading.
names_file.close();

#Writes everything from the lists into their own seperate files.
for i in range(len(girl_list)):
    girlNames_file.write(girl_list[i]);
    
for i in range(len(boy_list)):
    boyNames_file.write(boy_list[i]);
    
for i in range(len(comm_list)):
    comNames_file.write(comm_list[i]);    

#Closes all remaining files being used to write to.
boyNames_file.close();
print("Boys names saved to: boynames.txt file");

girlNames_file.close();
print("Girls names saved to: girlnames.txt file");

comNames_file.close();
print("Common boys and girls names saved to: comboygirlnames.txt file");

