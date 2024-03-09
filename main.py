# importing required modules
from pypdf import PdfReader

# creating a pdf reader object
reader = PdfReader('example2.pdf')

# printing number of pages in pdf file
print(len(reader.pages))

# getting a specific page from the pdf file
text = ""
starting_page = 1
for i in range(starting_page,len(reader.pages) - 1):
    page = reader.pages[i]
    text = text + " " + page.extract_text()[50:-100:]
text = text.split()
a = "hello"
b = a.upper()
l = len(text)
i = 0
print(text)
number_of_options = 4
question_starting_string = "question"
questions = []
questions.append([])
questions.append([])
questions.append([])

opion_check = {}
opion_check[0] = 'A'
opion_check[1] = 'B'
opion_check[2] = 'C'
opion_check[3] = 'D'


sect = 0

while(i<l):
    if text[i] == "CHEMISTRY":
        print(text[i])
        sect = 0
    if text[i].strip() == 'PHYSICS':
        print("ppppp")
        sect = 1
    if text[i] == "MATHEMATICS":

        sect = 2
    if text[i] == "Answer" and text[i+1] == "Key":
        print("dadka")
        break
    if '1' <= text[i].lower()[0] <= '9' and text[i][len(text[i]) - 1] == '.':
        question = []
        ind = i
        q = ""
        while text[ind][0] != '(' and text[ind][0] != '[':
            if len(text[ind]) > 2:
                    if (text[ind][2] == ')' or text[ind][2] == ']') and text[ind][1] == 'A' :
                        break;
            q = q +" "+ text[ind]
            ind = ind+1
        i = ind
        if ind >= l:
            break

        question.append(q)
        options = []
        for oi in range(number_of_options-1):
            if ind >= l:
                break
            options.append(text[ind])
            ind = ind+1
            while ind < l and text[ind][0] != '(':
                if len(text[ind]) > 2:
                    if text[ind][2] == ')' and ( text[ind][1] == opion_check[oi]):
                        break
                options[oi] = options[oi] + " " + text[ind]
                ind = ind+1
                if ind >= l:
                    break
# options.append(text[ind])
# ind = ind+1
#
#         while text[ind][0] != '(':
#             if len(text[ind]) > 2:
#                 if text[ind][2] == ')':
#                     break
#             options[1] = options[1] + " " + text[ind]
#             ind = ind+1
#         options.append(text[ind])
#         ind = ind + 1
#
#         while text[ind][0] != '(':
#             if len(text[ind]) > 2:
#                 if text[ind][2] == ')':
#                     break
#             options[2] = options[2] + " " + text[ind]
#             ind = ind + 1
        if ind >= l:
            break
        options.append(text[ind])
        ind = ind + 1

        while text[ind].lower()[-1] != ".":

            options[3] = options[3] + " " + text[ind]
            ind = ind + 1
            if ind == l:
                break
        #ans = text[ind][7]
        question.append(options)
        #question.append(ans)
        i = ind -1
        questions[sect].append(question)
    i = i+1

print(questions[0])
print(text[i::])

