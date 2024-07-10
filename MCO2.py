import re
from pyswip.core import *
from pyswip.prolog import Prolog
from pyswip import *

def identify_query(prompt):
    sibling_bool = re.compile(r'Are \b[A-Z][a-z]+\b and \b[A-Z][a-z]+\b siblings\?')
    sibling_q = re.compile(r'Who are the siblings of \b[A-Z][a-z]+\b\?')
    sister_bool = re.compile(r'Is \b[A-Z][a-z]+\b a sister of \b[A-Z][a-z]+\b\?')
    sister_q = re.compile(r'Who are the sisters of \b[A-Z][a-z]+\b\?')
    brother_bool = re.compile(r'Is \b[A-Z][a-z]+\b a brother of \b[A-Z][a-z]+\b\?')
    brother_q = re.compile(r'Who are the brothers of \b[A-Z][a-z]+\b\?')
    mother_bool = re.compile(r'Is \b[A-Z][a-z]+\b the mother of \b[A-Z][a-z]+\b\?')
    mother_q = re.compile(r'Who is the mother of \b[A-Z][a-z]+\b\?')
    father_bool = re.compile(r'Is \b[A-Z][a-z]+\b the father of \b[A-Z][a-z]+\b\?')
    father_q = re.compile(r'Who is the father of \b[A-Z][a-z]+\b\?')
    parents_bool = re.compile(r'Are \b[A-Z][a-z]+\b and \b[A-Z][a-z]+\b the parents of \b[A-Z][a-z]+\b\?')
    parents_q = re.compile(r'Who are the parents of \b[A-Z][a-z]+\b\?')
    grandmother_bool = re.compile(r'Is \b[A-Z][a-z]+\b a grandmother of \b[A-Z][a-z]+\b\?')
    grandfather_bool = re.compile(r'Is \b[A-Z][a-z]+\b a grandfather of \b[A-Z][a-z]+\b\?')
    daughter_bool = re.compile(r'Is \b[A-Z][a-z]+\b a daughter of \b[A-Z][a-z]+\b\?')
    daughter_q = re.compile(r'Who are the daughters of \b[A-Z][a-z]+\b\?')
    son_bool = re.compile(r'Is \b[A-Z][a-z]+\b a son of \b[A-Z][a-z]+\b\?')
    son_q = re.compile(r'Who are the sons of \b[A-Z][a-z]+\b\?')
    child_bool = re.compile(r'Is \b[A-Z][a-z]+\b a child of \b[A-Z][a-z]+\b\?')
    children_q = re.compile(r'Who are the children of \b[A-Z][a-z]+\b\?')
    children_bool = re.compile(r'Are \b[A-Z][a-z]+\b, \b[A-Z][a-z]+\b and \b[A-Z][a-z]+\b children of \b[A-Z][a-z]+\b\?')
    aunt_bool = re.compile(r'Is \b[A-Z][a-z]+\b an aunt of \b[A-Z][a-z]+\b\?')
    uncle_bool = re.compile(r'Is \b[A-Z][a-z]+\b an uncle of \b[A-Z][a-z]+\b\?')
    relatives_bool = re.compile(r'Are \b[A-Z][a-z]+\b and \b[A-Z][a-z]+\b relatives\?')


    if sibling_bool.match(prompt):
        return "siblings bool"
    elif sibling_q.match(prompt):
        return "siblings query"
    elif sister_bool.match(prompt):
        return "sister bool"
    elif sister_q.match(prompt):
        return "sister query"
    elif brother_bool.match(prompt):
        return "brother bool"
    elif brother_q.match(prompt):
        return "brother query"
    elif mother_bool.match(prompt):
        return "mother bool"
    elif mother_q.match(prompt):
        return "mother query"
    elif father_bool.match(prompt):
        return "father bool"
    elif father_q.match(prompt):
        return "father query"
    elif parents_bool.match(prompt):
        return "parents bool"
    elif parents_q.match(prompt):
        return "parents query"
    elif grandmother_bool.match(prompt):
        return "grandmother bool"
    elif grandfather_bool.match(prompt):
        return "grandfather bool"
    elif daughter_bool.match(prompt):
        return "daughter bool"
    elif daughter_q.match(prompt):
        return "daughter query"
    elif son_bool.match(prompt):
        return "son bool"
    elif son_q.match(prompt):
        return "son query"
    elif child_bool.match(prompt):
        return "child bool"
    elif children_bool.match(prompt):
        return "children bool"
    elif children_q.match(prompt):
        return "children query"
    elif aunt_bool.match(prompt):
        return "aunt bool"
    elif uncle_bool.match(prompt):
        return "uncle bool"
    elif relatives_bool.match(prompt):
        return "relatives bool"
    else:
        return "Invalid Prompt!"


def identify_statement(prompt):
    # Define regular expressions for different sentence patterns

    sibling_pat = re.compile(r'\b[A-Z][a-z]+\b and \b[A-Z][a-z]+\b are siblings\.')
    brother_pat = re.compile(r'\b[A-Z][a-z]+\b is a brother of \b[A-Z][a-z]+\b\.')
    sister_pat = re.compile(r'\b[A-Z][a-z]+\b is a sister of \b[A-Z][a-z]+\b\.')
    father_pat = re.compile(r'\b[A-Z][a-z]+\b is the father of \b[A-Z][a-z]+\b\.')
    mother_pat = re.compile(r'\b[A-Z][a-z]+\b is the mother of \b[A-Z][a-z]+\b\.')
    parents_pat = re.compile(r'\b[A-Z][a-z]+\b and \b[A-Z][a-z]+\b are the parents of \b[A-Z][a-z]+\b\.')
    grandmother_pat = re.compile(r'\b[A-Z][a-z]+\b is a grandmother of \b[A-Z][a-z]+\b\.')
    grandfather_pat = re.compile(r'\b[A-Z][a-z]+\b is a grandfather of \b[A-Z][a-z]+\b\.')
    child_pat = re.compile(r'\b[A-Z][a-z]+\b is a child of \b[A-Z][a-z]+\b\.')
    children_pat = re.compile(r'\b[A-Z][a-z]+\b, \b[A-Z][a-z]+\b and \b[A-Z][a-z]+\b are children of \b[A-Z][a-z]+\b\.')
    daughter_pat = re.compile(r'\b[A-Z][a-z]+\b is a daughter of \b[A-Z][a-z]+\b\.')
    son_pat = re.compile(r'\b[A-Z][a-z]+\b is a son of \b[A-Z][a-z]+\b\.')
    uncle_pat = re.compile(r'\b[A-Z][a-z]+\b is an uncle of \b[A-Z][a-z]+\b\.')
    aunt_pat = re.compile(r'\b[A-Z][a-z]+\b is an aunt of \b[A-Z][a-z]+\b\.')
    male_pat = re.compile(r'\b[A-Z][a-z]+\b is a male\.')
    female_pat = re.compile(r'\b[A-Z][a-z]+\b is a female\.')


    # Check if the input matches any of the patterns
    if sibling_pat.match(prompt):
        return "siblings"
    elif brother_pat.match(prompt):
        return "brother"
    elif sister_pat.match(prompt):
        return "sister"
    elif father_pat.match(prompt):
        return "father"
    elif mother_pat.match(prompt):
        return "mother"
    elif parents_pat.match(prompt):
        return "parents"
    elif grandmother_pat.match(prompt):
        return "grandmother"
    elif grandfather_pat.match(prompt):
        return "grandfather"
    elif child_pat.match(prompt):
        return "child"
    elif children_pat.match(prompt):
        return "children"
    elif daughter_pat.match(prompt):
        return "daughter"
    elif son_pat.match(prompt):
        return "son"
    elif uncle_pat.match(prompt):
        return "uncle"
    elif aunt_pat.match(prompt):
        return "aunt"
    elif male_pat.match(prompt):
        return "male"
    elif female_pat.match(prompt):
        return "female"
    else:
        return "Invalid Prompt!"



def extract_names(prompt):
    # Define a regular expression pattern to match names
    pattern = re.compile(r'(\b[A-Z][a-z]+\b)')  # Assumes names start with an uppercase letter

    # Find all matches in the sentence
    names = pattern.findall(prompt)
    realNames = [name for name in names if name.lower() not in ["is", "are", "who"]]

    return realNames

def check_duplicates(names):
    seen_names = set()
    for name in names:
        if name in seen_names:
            return True  # Duplicate name found
        seen_names.add(name)
    return False  # All names are unique

def process_sentence(sentence):
    extracted_names = extract_names(sentence)
    return check_duplicates(extracted_names)

def result_writer(result, names, text):
    '''
      Sample format for @param text: "* is !a friend of *."
      if result is true
        Eren is a friend of Armin.
      else
        Eren is not a friend of Armin.
    '''
    # Replaces instances of '*' with the names in order
    for name in names:
        text = text.replace('*', name, 1)

    # Replaces instance of '!'
    if result:
        text = text.replace('!', '')
    else:
        text = text.replace('!', 'NOT ')

    print(text)
    return text

def chatbot():
    prolog = Prolog()

    prolog.consult("ud_relationships.pl")
    list_result = []
    print("Welcome to the FAMILY RELATIONSHIP CHATBOT!")
    print("Press e to exit")
    # define the rules
    while True:
        prompt = input("> ")
        # get the names
        names = extract_names(prompt)
        if prompt.lower() == "e":
            break

        pattern = ""
        # identify the sentence pattern
        if process_sentence(prompt):
            pattern = "same name"
        elif '?' in prompt:
            pattern = identify_query(prompt)
        else:
            pattern = identify_statement(prompt)

        valid = True
        match pattern:
            case "siblings":
                if not list(prolog.query(f"relatives('{names[0]}', '{names[1]}')")):
                    prolog.assertz(f"siblings('{names[0]}', '{names[1]}')")
                    prolog.assertz(f"siblings('{names[1]}', '{names[0]}')")
                else:
                    print("Either there is already a relationship or the prompt is invalid. Please check logic.")
                    valid=False
            case "brother":
                #if they have no previous relationship
                if not list(prolog.query(f"relatives('{names[0]}', '{names[1]}')")) and not list(prolog.query(f"female('{names[0]}')")):
                    prolog.assertz(f"siblings('{names[0]}', '{names[1]}')")
                    prolog.assertz(f"siblings('{names[1]}', '{names[0]}')")
                    prolog.assertz(f"male('{names[0]}')")
                else:
                    #if they have a relationship but they were not declared as female, so they can be male
                    if not list(prolog.query(f"female('{names[0]}')")) and not list(prolog.query(f"male('{names[0]}')")):
                        prolog.assertz(f"male('{names[0]}')")
                    else: #if they were declared female, they cannot be brother
                        print("Either there is already a relationship or the prompt is invalid. Please check logic.")
                        valid=False
            case "sister":

                if not list(prolog.query(f"relatives('{names[0]}', '{names[1]}')")) and not list(prolog.query(f"male('{names[0]}')")):
                    prolog.assertz(f"siblings('{names[0]}', '{names[1]}')")
                    prolog.assertz(f"siblings('{names[1]}', '{names[0]}')")
                    prolog.assertz(f"female('{names[0]}')")
                else:
                    if not list(prolog.query(f"male('{names[0]}')")) and not list(prolog.query(f"female('{names[0]}')")):
                        prolog.assertz(f"female('{names[0]}')")
                    else: #if they were declared male, they cannot be sister
                        print("Either there is already a relationship or the prompt is invalid. Please check logic.")
                        valid=False
            case "father":
                if not list(prolog.query(f"relatives('{names[0]}', '{names[1]}')")) and not list(prolog.query(f"female('{names[0]}')")) and len(list(prolog.query(f"father(X, '{names[1]}')"))) == 0:
                    prolog.assertz(f"parent('{names[0]}', '{names[1]}')")
                    prolog.assertz(f"male('{names[0]}')")
                else:
                    if not list(prolog.query(f"female('{names[0]}')")) and not list(prolog.query(f"male('{names[0]}')")) and not list(prolog.query(f"relatives('{names[0]}', '{names[1]}')")) and len(list(prolog.query(f"father(X, '{names[1]}')"))) == 0 or list(prolog.query(f"parent('{names[0]}', '{names[1]}'), not(male('{names[0]}')), not(female('{names[0]}'))")):
                        prolog.assertz(f"male('{names[0]}')")
                    else: #if they were declared female, they cannot be father
                        print("Either there is already a relationship or the prompt is invalid. Please check logic.")
                        valid=False

            case "mother":
                if not list(prolog.query(f"relatives('{names[0]}', '{names[1]}')")) and not list(prolog.query(f"male('{names[0]}')")) and len(list(prolog.query(f"mother(X, '{names[1]}')"))) == 0:
                    prolog.assertz(f"parent('{names[0]}', '{names[1]}')")
                    prolog.assertz(f"female('{names[0]}')")
                else:
                    if not list(prolog.query(f"male('{names[0]}')")) and not list(prolog.query(f"female('{names[0]}')")) and not list(prolog.query(f"relatives('{names[0]}', '{names[1]}')")) and len(list(prolog.query(f"mother(X, '{names[1]}')"))) == 0 or list(prolog.query(f"parent('{names[0]}', '{names[1]}'), not(male('{names[0]}')), not(female('{names[0]}'))")):
                        prolog.assertz(f"female('{names[0]}')")
                    else: #if they were declared male, they cannot be sister
                        print("Either there is already a relationship or the prompt is invalid. Please check logic.")
                        valid=False
            case "parents":
                if not list(prolog.query(f"relatives('{names[0]}', '{names[2]}')")) and not list(prolog.query(f"relatives('{names[1]}', '{names[2]}')")) and len(list(prolog.query(f"parent(X, '{names[2]}')"))) == 0:
                    prolog.assertz(f"parent('{names[0]}', '{names[2]}')")
                    prolog.assertz(f"parent('{names[1]}', '{names[2]}')")
                else:
                    print("Either there is already a relationship or the prompt is invalid. Please check logic.")
                    valid=False

            case "grandmother":
                if not list(prolog.query(f"relatives('{names[0]}', '{names[1]}')")) and not list(prolog.query(f"male('{names[0]}')")):
                    prolog.assertz(f"grandparent('{names[0]}', '{names[1]}')")
                    prolog.assertz(f"female('{names[0]}')")
                else:
                    print("Either there is already a relationship or the prompt is invalid. Please check logic.")
                    valid=False
            case "grandfather":
                if not list(prolog.query(f"relatives('{names[0]}', '{names[1]}')")) and not list(prolog.query(f"male('{names[0]}')")):
                    prolog.assertz(f"grandparent('{names[0]}', '{names[1]}')")
                    prolog.assertz(f"male('{names[0]}')")
                else:
                    print("Either there is already a relationship or the prompt is invalid. Please check logic.")
                    valid=False
            case "child":
                if not list(prolog.query(f"relatives('{names[0]}', '{names[1]}')" )) and len(list(prolog.query(f"parent(X, '{names[0]}')"))) < 2:
                    prolog.assertz(f"parent('{names[1]}', '{names[0]}')")
                else:
                    print("Either there is already a relationship or the prompt is invalid. Please check logic.")
                    valid=False
            case "children":
                valid = True
                for x in range( 3):
                    if list(prolog.query(f"relatives('{names[3]}', '{names[x]}')")) and len(list(prolog.query(f"parent(X, '{names[x]}')"))) == 2:
                        valid = False
                if(valid == True):
                    prolog.assertz(f"parent('{names[3]}', '{names[0]}')")
                    prolog.assertz(f"parent('{names[3]}', '{names[1]}')")
                    prolog.assertz(f"parent('{names[3]}', '{names[2]}')")
                else:
                    print("Either there is already a relationship or the prompt is invalid. Please check logic.")
                    

            case "daughter":
                if not list(prolog.query(f"relatives('{names[0]}', '{names[1]}')")) and not list(prolog.query(f"male('{names[0]}')")) and len(list(prolog.query(f"parent(X, '{names[0]}')"))) < 2:
                    prolog.assertz(f"parent('{names[1]}', '{names[0]}')")
                    prolog.assertz(f"female('{names[0]}')")
                else:
                    if not list(prolog.query(f"male('{names[0]}')")) and not list(prolog.query(f"female('{names[0]}')")) and not list(prolog.query(f"relatives('{names[0]}', '{names[1]}')")) or list(prolog.query(f"parent('{names[1]}', '{names[0]}'), not(male('{names[0]}')), not(female('{names[0]}'))")):
                        prolog.assertz(f"female('{names[0]}')")
                    else: #if they were declared male, they cannot be sister
                        print("Either there is already a relationship or the prompt is invalid. Please check logic.")
                        valid=False
            case "son":
                if not list(prolog.query(f"relatives('{names[0]}', '{names[1]}')")) and not list(prolog.query(f"female('{names[0]}')")) and len(list(prolog.query(f"parent(X, '{names[0]}')"))) < 2:
                    prolog.assertz(f"parent('{names[1]}', '{names[0]}')")
                    prolog.assertz(f"male('{names[0]}')")
                else:
                    if not list(prolog.query(f"male('{names[0]}')")) and not list(prolog.query(f"female('{names[0]}')")) and not list(prolog.query(f"relatives('{names[0]}', '{names[1]}')")) or list(prolog.query(f"parent('{names[1]}', '{names[0]}'), not(male('{names[0]}')), not(female('{names[0]}'))")):
                        prolog.assertz(f"male('{names[0]}')")
                    else: #if they were declared male, they cannot be sister
                        print("Either there is already a relationship or the prompt is invalid. Please check logic.")
                        valid=False
            case "uncle":
                if not list(prolog.query(f"relatives('{names[0]}', '{names[1]}')")) and not list(prolog.query(f"female('{names[0]}')")):
                    prolog.assertz(f"uncle('{names[0]}', '{names[1]}')")
                    prolog.assertz(f"male('{names[0]}')")
                else:
                    print("Either there is already a relationship or the prompt is invalid. Please check logic.")
                    valid=False
            case "aunt":
                if not list(prolog.query(f"relatives('{names[0]}', '{names[1]}')")) and not list(prolog.query(f"male('{names[0]}')")):
                    prolog.assertz(f"aunt('{names[0]}', '{names[1]}')")
                    prolog.assertz(f"female('{names[0]}')")
                else:
                    print("Either there is already a relationship or the prompt is invalid. Please check logic.")
                    valid=False
            case "male":
                if not list(prolog.query(f"female('{names[0]}')")) and not list(prolog.query(f"male('{names[0]}')")):
                    prolog.assertz(f"male('{names[0]}')")
                else:
                    print("Either there is already a relationship or the prompt is invalid. Please check logic.")
                    valid=False
            case "female":
                if not list(prolog.query(f"male('{names[0]}')")) and not list(prolog.query(f"female('{names[0]}')")):
                    prolog.assertz(f"female('{names[0]}')")
                else:
                    print("Either there is already a relationship or the prompt is invalid. Please check logic.")
                    valid=False
            case "same name":
                print("Cannot be the same person!")
            case "Invalid Prompt!":
                print("Invalid Prompt!")

        res = 0

        match pattern:
            case "siblings bool":
                result_writer(list(prolog.query(f"siblings('{names[0]}', '{names[1]}')")), names, "* and * are !siblings.")
            case "brother bool":
                if list(prolog.query(f"siblings('{names[0]}', '{names[1]}')")):
                    if list(prolog.query(f"female('{names[0]}')")):
                        print(names[0] + " is a sibling of " + names[1] + ", but they are a brother.")
                        res = 2
                    elif not list(prolog.query(f"male('{names[0]}')")):
                        print(names[0] + " is a sibling of " + names[1] + ", but their gender is unknown.")
                        res = 2
                    else: res = 1
                if res != 2: result_writer(res, names, "* is !a brother of *.")
            case "sister bool":
                if list(prolog.query(f"siblings('{names[0]}', '{names[1]}')")):
                    if list(prolog.query(f"male('{names[0]}')")):
                        print(names[0] + " is a sibling of " + names[1] + ", but they are a sister.")
                        res = 2
                    elif not list(prolog.query(f"female('{names[0]}')")):
                        print(names[0] + " is a sibling of " + names[1] + ", but their gender is unknown.")
                        res = 2
                    else: res = 1
                if res != 2: result_writer(res, names, "* is !a sister of *.")
            case "father bool": 
                if list(prolog.query(f"parent('{names[0]}', '{names[1]}')")):
                    if list(prolog.query(f"female('{names[0]}')")):
                        print(names[0] + " is a parent of " + names[1] + ", but they are the mother.")
                        res = 2
                    elif not list(prolog.query(f"male('{names[0]}')")):
                        print(names[0] + " is a parent of " + names[1] + ", but their gender is unknown.")
                        res = 2
                    else: res = 1
                if res != 2: result_writer(res, names, "* is !the father of *.")
            case "mother bool":
                if list(prolog.query(f"parent('{names[0]}', '{names[1]}')")):
                    if list(prolog.query(f"male('{names[0]}')")):
                        print(names[0] + " is a parent of " + names[1] + ", but they are the father.")
                        res = 2
                    elif not list(prolog.query(f"female('{names[0]}')")):
                        print(names[0] + " is a parent of " + names[1] + ", but their gender is unknown.")
                        res = 2
                    else: res = 1
                if res != 2: result_writer(res, names, "* is !the mother of *.")
            case "parents bool":
                new_names = []
                for i in range(2):
                    if list(prolog.query(f"parent('{names[i]}', '{names[2]}')")):
                        new_names.append(names[i])
                
                match len(new_names):
                    case 0:
                        print("None of them are parents of " + names[2] + ".")
                    case 1:
                        print("Only " + new_names[0] + " is a parent of " + names[2] + ".")
                    case 2:
                        result_writer(True, names, "* and * are !parents of *.")
            case "grandmother bool":
                if list(prolog.query(f"grandparent('{names[0]}', '{names[1]}')")):
                    if list(prolog.query(f"male('{names[0]}')")):
                        print(names[0] + " is a grandparent of " + names[1] + ", but they are the grandfather.")
                        res = 2
                    elif not list(prolog.query(f"female('{names[0]}')")):
                        print(names[0] + " is a grandparent of " + names[1] + ", but their gender is unknown.")
                        res = 2
                    else: res = 1
                if res != 2: result_writer(res, names, "* is !the grandmother of *.")
            case "grandfather bool":
                if list(prolog.query(f"grandparent('{names[0]}', '{names[1]}')")):
                    if list(prolog.query(f"female('{names[0]}')")):
                        print(names[0] + " is a grandparent of " + names[1] + ", but they are the grandmother.")
                        res = 2
                    elif not list(prolog.query(f"male('{names[0]}')")):
                        print(names[0] + " is a grandparent of " + names[1] + ", but their gender is unknown.")
                        res = 2
                    else: res = 1
                if res != 2: result_writer(res, names, "* is !the grandfather of *.")
            case "child bool":
                result_writer(list(prolog.query(f"child('{names[0]}', '{names[1]}')")), names, "* is !a child of *.")
            case "children bool":
                new_names = []
                for i in range(3):
                    if list(prolog.query(f"parent('{names[3]}', '{names[i]}')")):
                        new_names.append(names[i])
                
                match len(new_names):
                    case 0:
                        print("None of them are children of " + names[3] + ".")
                    case 1:
                        print("Only " + new_names[0] + " is a child of " + names[3] + ".")
                    case 2:
                        print("Only " + new_names[0] + " and " + new_names[1] + " are children of " + names[3] + ".")
                    case 3:
                        result_writer(True, names, "*, * and * are !children of *.")
            case "daughter bool":
                if list(prolog.query(f"parent('{names[1]}', '{names[0]}')")):
                    if list(prolog.query(f"male('{names[0]}')")):
                        print(names[0] + " is a child of " + names[1] + ", but they are a son.")
                        res = 2
                    elif not list(prolog.query(f"female('{names[0]}')")):
                        print(names[0] + " is a child of " + names[1] + ", but their gender is unknown.")
                        res = 2
                    else: res = 1
                if res != 2: result_writer(res, names, "* is !the daughter of *.")
            case "son bool":
                if list(prolog.query(f"parent('{names[1]}', '{names[0]}')")):
                    if list(prolog.query(f"female('{names[0]}')")):
                        print(names[0] + " is a child of " + names[1] + ", but they are a daughter.")
                        res = 2
                    elif not list(prolog.query(f"male('{names[0]}')")):
                        print(names[0] + " is a child of " + names[1] + ", but their gender is unknown.")
                        res = 2
                    else: res = 1
                if res != 2: result_writer(res, names, "* is !the son of *.")
            case "uncle bool":
                result_writer(list(prolog.query(f"uncle('{names[0]}', '{names[1]}')")), names, "* is !an uncle of *.")
            case "aunt bool":
                result_writer(list(prolog.query(f"aunt('{names[0]}', '{names[1]}')")), names, "* is !an aunt of *.")
            case "relatives bool":
                result_writer(list(prolog.query(f"relatives('{names[0]}', '{names[1]}')")), names, "* is !a relative of *.")

        match pattern:
            case "siblings query": 
                list_result = list(prolog.query(f"siblings('{names[0]}', X)"))
            case "brother query":
                list_result = list(prolog.query(f"brother(X, '{names[0]}')"))
            case "sister query":
                list_result = list(prolog.query(f"sister(X, '{names[0]}')"))
            case "father query":
                list_result = list(prolog.query(f"father(X, '{names[0]}')"))
            case "mother query":
                list_result = list(prolog.query(f"mother(X, '{names[0]}')"))
            case "parents query":
                list_result = list(prolog.query(f"parent(X, '{names[0]}')"))
            case "children query":
                list_result = list(prolog.query(f"child(X, '{names[0]}')"))
            case "daughter query":
                list_result = list(prolog.query(f"daughter(X, '{names[0]}')"))
            case "son query":
                list_result = list(prolog.query(f"son(X, '{names[0]}')"))
            case "uncle query":
                list_result = list(prolog.query(f"uncle(X, '{names[0]}')"))
            case "aunt query":
                list_result = list(prolog.query(f"aunt(X, '{names[0]}')"))

        values_list = [value for dictionary in list_result for value in dictionary.values()]
        real_list = list(set(values_list))

        if "bool" not in pattern and pattern != "Invalid Prompt!" and pattern != "same name" and "query" not in pattern and valid == True:
            print("I learned something!")
        elif "query" in pattern:
            if len(real_list) > 0:
                for result in real_list:
                    print(result)
            else:
                print("This person has no relatives of that type.")



# Call the function to display the welcome message
chatbot()

