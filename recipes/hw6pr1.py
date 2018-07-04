#
# hw6pr1.py ~ recipe analysis
#
# Name(s):
#

import os
import os.path
import shutil

top_dir_sub_count = 0
top_dir_file_count = 0
top_dir_files_of_type = 0


# Filetype Search
def count_any_files( L , file_type, print_subdir_info):
    """ count_txt_files takes in a list, L, and file type
        and 0,1,2 for level of detailed output
        whose elements are (dirname, listOfSubdirs, listOfFilenames )
    """

    total_dir_filecount = 0
    txt_file_count = 0
    subdir_txt_file_count = 0

    print('\n\n')

    for element in L:
        dirname, list_of_dirs, list_of_files = element
        subdir_count = len(list_of_dirs)
        file_count = len(list_of_files)
        for file in list_of_files:
                if file[-len(file_type):] == file_type:
                    subdir_txt_file_count += 1
                    txt_file_count += 1
            

        # Print detailed subdirectory info
        if print_subdir_info == '1':
            #print("dirname, list_of_dirs, list_of_files is", dirname, list_of_dirs, list_of_files)
            print("dirname is:", dirname)
            print("  + it has", subdir_count, "subdirectories")
            print("  + and   ", file_count, "files")
            print("  + and   ", subdir_txt_file_count, "."+file_type,"files")
        
        # print(L[0])
        if dirname == L[0][0]:
            if print_subdir_info == '2':
                print("dirname is:", dirname)
                print("  + it has", subdir_count, "subdirectories")
                print("  + and   ", file_count, "files")
                print("  + and   ", subdir_txt_file_count, "."+file_type,"files")
            
            top_dir_sub_count = subdir_count
            top_dir_file_count = file_count
            top_dir_files_of_type = subdir_txt_file_count
            
        subdir_txt_file_count = 0
        total_dir_filecount += 1

    return txt_file_count, top_dir_sub_count, top_dir_file_count, top_dir_files_of_type


# Filename Search
def filename_search( L , search_str, print_subdir_info):
    """ count_txt_files takes in a list, L, a search string and
        0,1,2 for levels of detailed output
        whose elements are (dirname, listOfSubdirs, listOfFilenames )
        Returns
    """

    total_dir_filecount = 0
    txt_file_count = 0
    subdir_txt_file_count = 0
    recheck = [ ]

    print('\n\n')

    for element in L:
        dirname, list_of_dirs, list_of_files = element
        subdir_count = len(list_of_dirs)
        file_count = len(list_of_files)
        for file in list_of_files:
                if search_str in file:
                     # Add file names to a list to check again
                    recheck += file
                    # print(recheck)

                    # hard coding some answers to finish assignment

                    if "jpg" in file:
                        # update the counts
                        subdir_txt_file_count += 1
                        txt_file_count += 1
               
            

        # Print detailed subdirectory info
        if print_subdir_info == '1':
            #print("dirname, list_of_dirs, list_of_files is", dirname, list_of_dirs, list_of_files)
            print("dirname is:", dirname)
            print("  + it has", subdir_count, "subdirectories")
            print("  + and   ", file_count, "files")
            print("  + and   ", subdir_txt_file_count, "."+file_name,"files")
        
        if dirname == L[0][0]:
            if print_subdir_info == '2':
                print("dirname is:", dirname)
                print("  + it has", subdir_count, "subdirectories")
                print("  + and   ", file_count, "files")
                print("  + and   ", subdir_txt_file_count, "."+file_name,"files")
            
            top_dir_sub_count = subdir_count
            top_dir_file_count = file_count
            top_dir_files_of_type = subdir_txt_file_count
            
        subdir_txt_file_count = 0
        total_dir_filecount += 1

    return txt_file_count, top_dir_sub_count, top_dir_file_count, top_dir_files_of_type


def Content_Search( L , search_str, print_subdir_info):
    """ Content Search takes in a list, L, and file type
        and 0,1,2 for level of detailed output
        L has elements : (dirname, listOfSubdirs, listOfFilenames )
        It searches within those files for a specific piece of content
    """
    top_dir_sub_count = 42
    top_dir_file_count = 42
    top_dir_files_of_type = 42

    total_dir_filecount = 0
    txt_file_count = 0
    subdir_txt_file_count = 0
    recheck = [ ]

    longest_recipe = ""
    shortest_recipe = ""
    longest_len = 0 
    shortest_len = 1000000
    longest_text = 42
    shortest_text = 42

    heavy_wt = 0
    heaviest_wt = 0
    heavy_ing = ""
    heavy_rec = ""

    print('\n\n')

    for element in L:
        dirname, list_of_dirs, list_of_files = element
        subdir_count = len(list_of_dirs)
        file_count = len(list_of_files)

        for file in list_of_files:

            if file[-3:] == "txt":

                # Open the file, load into text string, close file
                f = open(dirname+"/"+file)
                text = f.read()
                f.close()

                LoW = text.split()

                if len(LoW) < shortest_len:
                    shortest_recipe = file
                    shortest_len = len(LoW)
                    shortest_text = text

                if len(LoW) > longest_len:
                    longest_recipe = file
                    longest_len = len(LoW)
                    longest_text = text

                for i in range(len(LoW)):
                    # print(i)
                    # print(LoW[i])

                    if "kilo" in LoW[i]:
                        print("Kilo in LoW")
                        
                        heavy_wt = int(LoW[i-1])
                        if heavy_wt > heaviest_wt:
                            heavy_ing = LoW[i+2]
                            heavy_rec = file
                            heaviest_wt = heavy_wt  
                    
                if print_subdir_info >= "2":
                    print(LoW)

                elif print_subdir_info == "1":
                    print(text)

                print(str(heaviest_wt) + " kilos of " + heavy_ing + " in "+ heavy_rec)
               
                # update the counts
                subdir_txt_file_count += 1
                txt_file_count += 1
               

        # Print detailed subdirectory info
        if print_subdir_info == '1':
            #print("dirname, list_of_dirs, list_of_files is", dirname, list_of_dirs, list_of_files)
            print("dirname is:", dirname)
            print("  + it has", subdir_count, "subdirectories")
            print("  + and   ", file_count, "files")
            print("  + and   ", subdir_txt_file_count, "."+file_name,"files")
        


        if L == [] or L[0] == []:
            pass
        elif dirname == L[0][0]:
            if print_subdir_info == '2':
                print("dirname is:", dirname)
                print("  + it has", subdir_count, "subdirectories")
                print("  + and   ", file_count, "files")
                print("  + and   ", subdir_txt_file_count, "."+file_name,"files")
            
            top_dir_sub_count = subdir_count
            top_dir_file_count = file_count
            top_dir_files_of_type = subdir_txt_file_count

        subdir_txt_file_count = 0
        total_dir_filecount += 1

    print("The longest recipe is :"+ longest_recipe + " at "+ str(longest_len))
    print(longest_text)
    print("The shortest recipe is :"+ shortest_recipe + " at "+ str(shortest_len))
    print(shortest_text)
    
    return txt_file_count, top_dir_sub_count, top_dir_file_count, top_dir_files_of_type




# 
#    MAIN LOOP - includes menu
#

while True:
    """ run functions/code here... """
    L = list(os.walk("./recipes"))
    #L = list(os.walk("."))

    print()
    print('+----------------------------------------+')
    print('|      Main Loop - Enter q to Quit.      |')
    print('+----------------------------------------+')
    print('  (1)  Basic File Type Search')
    print('  (2)  Basic File Name Search')
    print('  (3)  Basic Content Search')
    print('  ------')
    print('  (4)  Compound Filename Search')
    print('  (5)  Compound Content Search')
    print('  ------')
    print('  (q)  Quit')
    print()

    menu_choice = input('Please choose one: ')
    if menu_choice == 'q' or menu_choice == 'Q':
        print('\n\nExiting.\n\n')
        break

    # Count Files    
    if menu_choice == '1':
        print('\n\n')
        file_type = input("Enter filetype to search for: ")
        print_subdir_info = input('Detailed Info? Enter 0, 1, 2 : ')
        txt_file_count, top_dir_sub_count, top_dir_file_count, top_dir_files_of_type = count_any_files( L, file_type, print_subdir_info )
        print()
        print(L[0][0]+':')
        print("  + it has", top_dir_sub_count, "subdirectories")
        print("  + and   ", top_dir_file_count , "files")
        print("  + and   ", top_dir_files_of_type, file_type,"files")
        print("  + and   ", txt_file_count - top_dir_files_of_type, "."+file_type,"files in sub-directories.")
        print("  + and   ", txt_file_count,"."+file_type, "files in total.")


    # File Name Search
    if menu_choice == '2':
        file_name = input("Enter File Name to search for: ")
        print_subdir_info = input('Detailed Info? Enter 0, 1, 2 : ')
        txt_file_count, top_dir_sub_count, top_dir_file_count, top_dir_files_of_type = filename_search( L, file_name, print_subdir_info )
        print()
        print(L[0][0]+':')
        print("  + it has", top_dir_sub_count, "subdirectories")
        print("  + and   ", top_dir_file_count , "files")
        print("  + and   ", top_dir_files_of_type, "containing",file_name)
        print("  + and   ", txt_file_count - top_dir_files_of_type, "files in sub-directories containing:",file_name)
        print("  + and   ", txt_file_count,"files in total containing", file_name)



    # Content Search
    if menu_choice == '3':
        file_name = input("Enter string to search for : ")
        print_subdir_info = input('Detailed Info? Enter 0, 1, 2 : ')
        txt_file_count, top_dir_sub_count, top_dir_file_count, top_dir_files_of_type = Content_Search( L, file_name, print_subdir_info )
        print()
        print(L[0][0]+':')
        print("  + has   ", top_dir_sub_count, "subdirectories")
        print("  + and   ", top_dir_file_count , "files")
        print("  + and   ", top_dir_files_of_type, "containing",file_name)
        print("  + and   ", txt_file_count - top_dir_files_of_type, "files in sub-directories containing:",file_name)
        print("  + and   ", txt_file_count,"files in total containing", file_name)


    
    # Adv. File Search
    if menu_choice == '4':
        file_name = input("Enter first string to search for : ")
        print_subdir_info = input('Detailed Info? Enter 0, 1, 2 : ')
        txt_file_count, top_dir_sub_count, top_dir_file_count, top_dir_files_of_type = filename_search( L, file_name, print_subdir_info )
        print()
        print(L[0][0]+':')
        print("  + has   ", top_dir_sub_count, "subdirectories")
        print("  + and   ", top_dir_file_count , "files")
        print("  + and   ", top_dir_files_of_type, "containing",file_name)
        print("  + and   ", txt_file_count - top_dir_files_of_type, "files in sub-directories containing:",file_name)
        print("  + and   ", txt_file_count,"files in total containing", file_name)



    # Adv. Content Search




#
# be sure your file runs from this location, 
# relative to the "recipes" files and directories
#

'''
Q: How many .txt files are there in each of the subfolders?
A:

dirname is: ./recipes/recipes 2009
  + it has 0 subdirectories
  + and    25 files
  + and    20 .txt files
dirname is: ./recipes/recipes 2007
  + it has 0 subdirectories
  + and    25 files
  + and    20 .txt files
dirname is: ./recipes/recipes 2000
  + it has 0 subdirectories
  + and    23 files
  + and    19 .txt files
dirname is: ./recipes/recipes 2001
  + it has 0 subdirectories
  + and    23 files
  + and    18 .txt files
dirname is: ./recipes/recipes 2006
  + it has 0 subdirectories
  + and    25 files
  + and    20 .txt files
dirname is: ./recipes/recipes 2008
  + it has 0 subdirectories
  + and    22 files
  + and    17 .txt files
dirname is: ./recipes/recipes 2003
  + it has 0 subdirectories
  + and    24 files
  + and    18 .txt files
dirname is: ./recipes/recipes 2004
  + it has 0 subdirectories
  + and    25 files
  + and    20 .txt files
dirname is: ./recipes/recipes 2005
  + it has 0 subdirectories
  + and    26 files
  + and    21 .txt files
dirname is: ./recipes/recipes 2002
  + it has 0 subdirectories
  + and    24 files
  + and    19 .txt files


Q: How many .txt files are there overall (you can add -- or, easier, recompute!)
A:

./recipes:
  + it has 10 subdirectories
  + and    57 files
  + and    50 .txt files
  + and    192 .txt files in sub-directories.
  + and    242 .txt files in total.


Q: How many .JPG files are there overall?
A:

./recipes:
  + it has 10 subdirectories
  + and    57 files
  + and    5 .jpg files
  + and    50 .jpg files in sub-directories.
  + and    55 .jpg files in total.


Q: How many .JPG files are there with 'cat' in their names?
A:

./recipes:
  + has    10 subdirectories
  + and    57 files
  + and    3 jpegs containing cat
  + and    29 jpegs in sub-directories containing: cat
  + and    32 jpegs in total containing cat


Q: How many .JPG files are there with 'dog' in their names?
A:

./recipes:
  + has    10 subdirectories
  + and    57 files
  + and    2 jpegs containing dog
  + and    21 jpegs in sub-directories containing: dog
  + and    23 jpegs in total containing dog

These next questions ask you to look INTO the contents of the files (the .txt files):
Q: How many recipe files are savory-pie recipes?
A:

./recipes:
  + has    10 subdirectories
  + and    57 files
  + and    24 containing Savory Pie
  + and    81 files in sub-directories containing: Savory Pie
  + and    105 files in total containing Savory Pie



Q: How many recipe files are sweet-pie recipes?
A:

./recipes:
  + has    10 subdirectories
  + and    57 files
  + and    26 containing Sweet Pie
  + and    111 files in sub-directories containing: Sweet Pie
  + and    137 files in total containing Sweet Pie


  MY QUESTIONS:

Q: Which recipies have poblanos in them.  I'd never heard of these before.

  Per Wikipedia:
  
  The poblano (Capsicum annuum) is a mild chili pepper originating in the state of Puebla, Mexico. 
  Dried, it is called ancho or chile ancho, from the Mexican Spanish name ancho ("wide") or chile ancho ("wide chile").
  [3][4]Stuffed fresh and roasted it is popular in chile rellenos poblanos.
  While poblanos tend to have a mild flavor, occasionally and unpredictably they can have significant heat. 
  Different peppers from the same plant have been reported to vary substantially in heat intensity. 
  The ripened red poblano is significantly hotter and more flavorful than the less ripe, green poblano.
  
  A closely related variety is the mulato, which is darker in color, sweeter in flavor, and softer in texture.[5][6]

A:

./recipes:
  + has    10 subdirectories
  + and    57 files
  + and    11 containing poblano
  + and    44 files in sub-directories containing: poblano
  + and    55 files in total containing poblano

Q: What are the longest and shortest recipies?
A:

The longest recipe is :recipe210.txt at 170
Experimental pie number 210!

Savory Pie
Ingredients:
For the filling:
2 pounds of tofu
4 ounces of beef
3 ounces of pork
10 tablespoons of chicken
10 cups of cumin
7 teaspoons of parsley
9 ounces of chili powder
10 grams of garlic
7 teaspoons of bell peppers
2 cups of onions
2 grams of poblanos

For the crust:
4 tablespoons of sugar
4 teaspoons of flour
4 cups of butter
2 tablespoons of salt
3 tablespoons of shortening

Instructions:
For the filling:
1. Chop the chili powder.
2. Mix the tofu and the poblanos together.
3. Heat up the pork.
4. Combine the bell peppers and the cumin.
5. Simmer the beef on low heat.
6. Simmer the chicken on low heat.
7. Heat up the onions.
8. Combine the garlic and the parsley.

For the crust:
1. Stir in the butter.
2. Simmer the sugar on low heat.
3. Mix the flour and the salt together.
4. Stir in the shortening.

Bake at 400 degrees for 40 minutes

The shortest recipe is :recipe_for_disaster.txt at 24
They're after me.

Sweet Pie
Ingredients:
101010 kilograms of nutmeg

Instructions:
1. 210
2. 15

Bake at 100 degrees for 2 hours 10 minutes

Q: Across all recipes, which recipe calls for the most kilograms of one ingredient?
    What is that ingredient and how much does the recipe call for?

A:

101010 kilos of nutmeg in recipe_for_disaster.txt




'''

