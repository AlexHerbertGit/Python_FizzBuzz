"""
Scans a csv file redirected into the script
 "--header" indicates the first row is a header row
"""
import sys as sys
import argparse

#Exercise 0 - 
# 1. Look at the python "argparse", 
#    Describe how to set up arguments, 
#    Explain how it is set up - see code under "if __name__ == "__main__:"
# 2. Write out a description of how scan works, 
def scan(has_header=False):
    result = []
    values = []
    do_header = has_header
    header_names = {}
    try:
        for aline in sys.stdin:
                this_line = aline.strip().split(',')
                if do_header:
                    header_names = this_line
                    do_header = False
                else:
                    a_dict = {}
                    for i in range(0,len(this_line)):
                        if has_header :
                            a_dict[header_names[i]]= this_line[i]
                        else:
                            a_dict[i]= this_line[i]

                    result += [a_dict]
                    values += [this_line]
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return result,values

    return result,values

# Exercise one
def sum_of(column_name, a_list_of_dictionary):
    """
    Return one value that is the sum of the column 
    column_name of each "row" (dictionary)
    """
    running_sum = 0
    for row in a_list_of_dictionary:
        running_sum += row[column_name]
    return running_sum

        

#Exercise Two
def multiplies_cols(column_names,a_list_of_dictionary):
    """
    Return a new list of "rows" (dictionary)
    That multiplies the values of the named columns
    
    """
    result_list = []
    for a_row in a_list_of_dictionary:
        row_product = 1
        for a_name in column_names:
            row_product *= a_row[a_name]
        result_list += [{'Mult':row_product}]    
    return result_list

#Exercise Three
# - fix display_table so that the columns all line up
def display_table(a_list_of_dictionary):
    lines = ""
    # Get a header line
    a_dictionary = a_list_of_dictionary[0]
    header_line = ""
    for key in a_dictionary:
        header_line += f'{key}\t'
    header_line = header_line.strip()

    # Make up the table
    lines += header_line 

    for a_dictionary in a_list_of_dictionary:
        a_line = ''
        for key,value in a_dictionary.items():
            a_line += f'{value}\t'
        a_line = a_line.strip()
        lines += f'\n{a_line}'
    print(lines)

if __name__ == "__main__":
   parser = argparse.ArgumentParser(description="Scan some rows into a list of one list per line.")
   parser.add_argument('--header',action='store_true',help='The first row is a header row.')
   args = vars(parser.parse_args())
   print(f'The args are {args}')
   #args = sys.argv
   #print(f'The args are {args}')
   dict_lst,values_lst = scan(args['header'])
   display_table(dict_lst)
