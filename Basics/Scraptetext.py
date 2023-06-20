import requests
from bs4 import BeautifulSoup
import re


# Make a request
def site_compare1(link,filename1):
    page = requests.get(
        link)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Extract title of page
    page_title = soup.title.text

    # Extract body of page
    page_body = soup.body

    # Extract head of page
    page_head = soup.head
    text1 = page_body.text
    text1=re.sub(r'\n\s*\n','\n',text1,re.MULTILINE)
    with open(filename1, 'w',encoding='utf-8') as f:
        f.writelines(text1)


def site_compare2(link,filename2):
    page = requests.get(
        link)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Extract title of page
    page_title = soup.title.text

    # Extract body of page
    page_body = soup.body

    # Extract head of page
    page_head = soup.head
    text2 = page_body.text
    text2 = re.sub(r'\n\s*\n', '\n', text2, re.MULTILINE)
    with open(filename2, 'w',encoding='utf-8') as f:
        f.writelines(text2)
def compare(filename1,filename2):
    file_1 = open(filename1,"r",encoding='utf-8')
    file_2 = open(filename2,"r",encoding='utf-8')


    print("Comparing files ", " @ " + filename1, " # " + filename2, sep='\n')

    file_1_line = file_1.readline()
    file_2_line = file_2.readline()

    # Use as a COunter
    line_no = 1

    print()

    with open(filename1,"r",encoding='utf-8') as file1:
        with open(filename2,"r",encoding='utf-8') as file2:
            same = set(file1).intersection(file2)

    print("Common Lines in Both Files")

    for line in same:
        print(line, end='')

    print('\n')
    print("Difference Lines in Both Files")
    while file_1_line != '' or file_2_line != '':

        # Removing whitespaces
        file_1_line = file_1_line.rstrip()
        file_2_line = file_2_line.rstrip()

        # Compare the lines from both file
        if file_1_line != file_2_line:

            # otherwise output the line on file1 and use @ sign
            if file_1_line == '':
                print("@", "Line-%d" % line_no, file_1_line)
            else:
                print("@-", "Line-%d" % line_no, file_1_line)

            # otherwise output the line on file2 and use # sign
            if file_2_line == '':
                print("#", "Line-%d" % line_no, file_2_line)
            else:
                print("#+", "Line-%d" % line_no, file_2_line)

            # Print a empty line
            print()

        # Read the next line from the file
        file_1_line = file_1.readline()
        file_2_line = file_2.readline()

        line_no += 1

    file_1.close()
    file_2.close()


#
#link1 = input("Enter the Link for the Content:")
#filename1= input("Enter the file name for Website1")
#filename1= filename1 +".txt"
#link2 = input("Enter the Link of the Website:")
#filename2= input("Enter the file name for Website2")
#filename2= filename2 +".txt"

#site_compare1(link1,filename1)
#site_compare2(link2,filename2)

filename1="word.txt"
filename2="WORD1.txt"
compare(filename1,filename2)