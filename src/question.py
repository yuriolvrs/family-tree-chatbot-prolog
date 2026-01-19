import util

def process_question(question, prolog):
    # Split the question into individual words
    words = question.split()

    keyword_mapping = {
        "siblings?": question_siblings,
        "siblings": question_siblings, 
        "sister": question_sister,
        "sisters": question_sister, 
        "brother": question_brother, 
        "brothers": question_brother,
        "mother": question_mother, 
        "father": question_father, 
        "parents": question_parents, 
        "grandmother": question_grandmother, 
        "grandfather": question_grandfather, 
        "daughter": question_daughter, 
        "daughters": question_daughter,
        "son": question_son, 
        "sons": question_son,
        "child": question_child, 
        "children": question_children, 
        "aunt": question_aunt,
        "uncle": question_uncle, 
        "relatives?": question_relatives
    }

    for word in words:
        if word in keyword_mapping:
            keyword_mapping[word](words, prolog)
            break

    else:
        print("I don't understand.")

def question_siblings(words, prolog):
    # check if first word is "Are" or "Who"
    if words[0] == "Are": # Are ___ and ___ siblings?
        if len(words) == 5 and words[1].istitle() and words[2] == "and" and words[3].istitle() and words[4] == "siblings?":
            person1, person2 = words[1].lower(), words[3].lower()
            are_siblings = util.query_are_siblings(person1, person2, prolog)

            if are_siblings:
                print(f"Yes, {person1.capitalize()} and {person2.capitalize()} are siblings.")
            else:
                print(f"No, {person1.capitalize()} and {person2.capitalize()} are not siblings.")
        else:
            # Sentence does not follow sibling question pattern
            print("I don't understand.")
    elif words[0] == "Who": # Who are the siblings of ___?
        phrase = " ".join(words[0:5])
        if len(words) == 6 and phrase == "Who are the siblings of" and words[5].istitle():
            person = words[5].lower()
            person = person[:-1]
            siblings_list = util.find_siblings(person, prolog)

            if siblings_list:
                if len(siblings_list) > 1:
                    last_sibling = siblings_list[-1]
                    siblings_list = siblings_list[:-1]
                    siblings_str = ', '.join(siblings_list) + f" and {last_sibling}"
                    print(f"{person.capitalize()}'s siblings are {siblings_str}.")
                else:
                    siblings_str = siblings_list[0]
                    print(f"{person.capitalize()}'s sibling is {siblings_str}.")
            else:
                print(f"I don't know if {person.capitalize()} has siblings.")
        else:
            # Sentence does not follow sibling question pattern
            print("I don't understand.")
    else:
        # Question doesn't start with "Are" or "Who"
        print("I don't understand.")

def question_sister(words, prolog):
    # # check if first word is "Is" or "Who"
    if words[0] == "Is": #Is __ a sister of __ ?
        if len(words) == 6 and words[1].istitle() and words[2] == "a" and words[3] == "sister" and words[4] == "of" and words[5].istitle():
            sister, sibling = words[1].lower(),words[5].lower()
            # Remove ? at the end of sibling's name
            sibling = sibling[:-1]
            are_sisters = util.query_sister(sister,sibling, prolog)

            if are_sisters:
                print(f"Yes, {sister.capitalize()} is a sister of {sibling.capitalize()}.")
            else:
                print(f"No, {sister.capitalize()} is not a sister of {sibling.capitalize()}.")
        else:
            # Sentence does not follow sibling question pattern
            print("I don't understand.") 
    elif words[0] == "Who":
        if len(words) == 6 and words[1]=="are" and words[2] == "the" and words[3] == "sisters" and words[4] == "of" and words[5].istitle():
            sister = words[5].lower()
            sister = sister[:-1]
            sister_list = util.find_sisters(sister,prolog)

            if sister_list:
                if len(sister_list) > 1:
                    last_sister = sister_list[-1]
                    sister_list = sister_list[:-1]
                    sister_str = ', '.join(sister_list) + f" and {last_sister}"
                    print(f"{sister.capitalize()}'s sisters are {sister_str}.")
                else:
                    sister_str = sister_list[0]
                    print(f"{sister.capitalize()}'s sister is {sister_str}.")
            else:
                print(f"I don't know if {sister.capitalize()} has sisters.")
        else:
            print("I don't understand.")
    else:
         # Question doesn't start with "Is" or "Who"
         print("I don't understand.")

def question_brother(words, prolog):
    # # check if first word is "Is", or "Who"
    if words[0] == "Is":
        if len(words)== 6 and words[1].istitle() and words[2] == "a" and words[3] == "brother" and words[4] == "of" and words[5].istitle():
            brother, sibling = words[1].lower(), words[5].lower()
            sibling = sibling[:-1]
            are_brothers = util.query_brothers(brother, sibling, prolog)

            if are_brothers:
                print(f"Yes, {brother.capitalize()} is a brother of {sibling.capitalize()}.")
            else:
                print(f"No, {brother.capitalize()} is not a brother of {sibling.capitalize()}.")
        else:
            print("I don't understand.")
    elif words[0] == "Who":
        if len(words)== 6 and words[1]=="are" and words[2] == "the" and words[3] == "brothers" and words[4] == "of" and words[5].istitle():
            brother = words[5].lower()
            brother = brother[:-1]
            brother_list = util.find_brothers(brother,prolog)

            if brother_list:
                if len(brother_list)>1:
                    last_brother = brother_list[-1]
                    brother_list = brother_list[:-1]
                    brother_str = ', '.join(brother_list) + f" and {last_brother}"
                    print(f"{brother.capitalize()}'s brothers are {brother_str}.")
                else:
                    brother_str = brother_list[0]
                    print(f"{brother.capitalize()}'s brother is {brother_str}.")
            else: 
                print(f"I don't know if {brother.capitalize()} has brothers.")
        else:
            print("I don't understand.")

    else:
    #     # Question doesn't start with "Is", or "Who"
         print("I don't understand.")

def question_mother(words, prolog):
    # check if first word is "Is", or "Who"
    if words[0] == "Is":
        if len(words)==6 and words[1].istitle() and words[2] == "the" and words[3] == "mother" and words[4] == "of" and words[5].istitle():
            mom,child = words[1].lower(), words[5].lower()
            child = child[:-1]
            is_mother = util.query_mother(mom,child,prolog)

            if is_mother:
                print(f"Yes, {mom.capitalize()} is the mother of {child.capitalize()}.")
            else:
                print(f"No, {mom.capitalize()} is not the mother of {child.capitalize()}.")
        else:
            print("I don't understand.")
    elif words[0] == "Who":
        if len(words) == 6 and words[1]=="is" and words[2] == "the" and words[3] == "mother" and words[4] == "of" and words[5].istitle():
            child = words[5].lower()
            child = child[:-1]
            get_mother = util.find_mother(child,prolog)

            if get_mother:
                mother_str = get_mother
                print(f"{mother_str.capitalize()} is the mother of {child.capitalize()}.")
            else:
                print(f"I don't know who {child.capitalize()}'s mother is.")
        else:
            print("I don't understand.")

    else:
        # Question doesn't start with "Is", or "Who"
        print("I don't understand.")

def question_father(words, prolog):
    # check if first word is "Is", or "Who"
    if words[0] == "Is":
        if len(words) == 6 and words[1].istitle() and words[2] == "the" and words[3] == "father" and words[4] == "of" and words[5].istitle():
            papa,child = words[1].lower(), words[5].lower()
            child = child[:-1]
            is_papa = util.query_father(papa,child,prolog)

            if is_papa:
                print(f"Yes, {papa.capitalize()} is the father of {child.capitalize()}.")
            else:
                print(f"No, {papa.capitalize()} is not the father of {child.capitalize()}.")
        else:
            print("I don't understand.")

    elif words[0] == "Who":
        if len(words) == 6 and words[1]=="is" and words[2] == "the" and words[3] == "father" and words[4] == "of" and words[5].istitle():
            child = words[5].lower()
            child = child[:-1]
            is_father = util.find_father(child, prolog)
            if is_father:
                father_str = is_father
                print(f"{father_str.capitalize()} is the father of {child.capitalize()}.")
            else:
                print(f"I don't know who {child.capitalize()}'s father is.")
        else:
            print("I don't understand.")
    else:
        # Question doesn't start with "Is", or "Who"
        print("I don't understand.")

def question_parents(words, prolog):
    # check if first word is "Are" or "Who"
    if words[0] == "Are":
        #
        if len(words) == 8 and words[1].istitle() and words[2] == "and" and words[3].istitle() and words[4] == "the" and words[5] == "parents" and words[6] == "of" and words[7].istitle():
            p1,p2,child = words[1].lower(), words[3].lower(), words[7].lower()
            child = child[:-1]
            are_parents = util.query_parents(p1, p2, child,prolog)

            if are_parents:
                print(f"Yes, {p1.capitalize()} and {p2.capitalize()} are the parents of {child.capitalize()}.")
            else:
                print(f"No, {p1.capitalize()} and {p2.capitalize()} are not the parents of {child.capitalize()}.")
    elif words[0] == "Who":
        if len(words) == 6 and words[1]=="are" and words[2] == "the" and words[3] == "parents" and words[4] == "of" and words[5].istitle():
            child = words[5].lower()
            child = child[:-1]
            parent_list = util.find_parents(child,prolog)

            if parent_list:
                if len(parent_list) > 1:
                    last_parent = parent_list[-1]
                    parent_list = parent_list[:-1]
                    parent_str = ', '.join(parent_list) + f" and {last_parent}"
                    print(f"{parent_str} are the parents of {child.capitalize()}.")
                else:
                    parent_str = parent_list[0]
                    print(f"{parent_str} is a parent of {child.capitalize()}. I don't know who their other parent is.")
            else:
                print(f"I don't know who {child.capitalize()}'s parents are.")
        else:
            # Sentence does not follow parent question pattern
            print("I don't understand.")

def question_grandmother(words, prolog):
    # check if first word is "Is"
    if words[0] == "Is":
        if len(words)==6 and words[1].istitle() and words[2] == "a" and words[3] == "grandmother" and words[4] == "of" and words[5].istitle():
            grandmom,grandchild = words[1].lower(), words[5].lower()
            grandchild = grandchild[:-1]
            is_grandmother = util.query_grandmother(grandmom,grandchild,prolog)

            if is_grandmother:
                print(f"Yes, {grandmom.capitalize()} is a grandmother of {grandchild.capitalize()}.")
            else:
                print(f"No, {grandmom.capitalize()} is not a grandmother of {grandchild.capitalize()}.")
        else:
            print("I don't understand.")
    else:
        # Question doesn't start with "Is"
        print("I don't understand.")

def question_grandfather(words, prolog):
    # check if first word is "Is"
    if words[0] == "Is":
        if len(words)==6 and words[1].istitle() and words[2] == "a" and words[3] == "grandfather" and words[4] == "of" and words[5].istitle():
            granddad,grandchild = words[1].lower(), words[5].lower()
            grandchild = grandchild[:-1]
            is_grandfather = util.query_grandfather(granddad,grandchild,prolog)

            if is_grandfather:
                print(f"Yes, {granddad.capitalize()} is a grandfather of {grandchild.capitalize()}.")
            else:
                print(f"No, {granddad.capitalize()} is not a grandfather of {grandchild.capitalize()}.")
        else:
            print("I don't understand.")
    else:
        # Question doesn't start with "Is"
        print("I don't understand.")

def question_daughter(words, prolog):
    # check if first word is "Is", or "Who"
    if words[0] == "Is":
        if len(words) == 6 and words[1].istitle() and words[2] == "a" and words[3] == "daughter" and words[4] == "of" and words[5].istitle():
            kiddie,parent = words[1].lower(),words[5].lower()
            # Remove ? at the end of sibling's name
            parent = parent[:-1]
            is_daughter = util.query_daughter(kiddie,parent,prolog)

            if is_daughter:
                print(f"Yes, {kiddie.capitalize()} is a daughter of {parent.capitalize()}.")
            else:
                print(f"No, {kiddie.capitalize()} is not a daughter of {parent.capitalize()}.")
        else:
            print("I don't understand.")
    elif words[0] == "Who":
        if len(words) == 6 and words[1]=="are" and words[2] == "the" and words[3] == "daughters" and words[4] == "of" and words[5].istitle():
            parent = words[5].lower()
            parent = parent[:-1]
            daughter_list = util.find_daughter(parent,prolog)

            if daughter_list:
                if len(daughter_list)>1:
                    last_daughter = daughter_list[-1]
                    daughter_list=daughter_list[:-1]
                    daughter_str = ', '.join(daughter_list) + f" and {last_daughter}."
                    print(f"{parent.capitalize()}'s daughters are {daughter_str}.")
                else:
                    daughter_str = daughter_list[0]
                    print(f"{parent.capitalize()}'s daughter is {daughter_str}.")
            else: 
                print(f"I don't know is {parent.capitalize()} has daughters.")
        else:
            print("I don't understand.")
    else:
        # Question doesn't start with "Is", or "Who"
        print("I don't understand.")

def question_son(words, prolog):
    # check if first word is "Is", or "Who"
    if words[0] == "Is":
        if len(words) == 6 and words[1].istitle() and words[2] == "a" and words[3] == "son" and words[4] == "of" and words[5].istitle():
            kiddie, parent = words[1].lower(),words[5].lower()
            parent = parent[:-1]
            is_son= util.query_son(kiddie,parent,prolog)

            if is_son:
                print(f"Yes, {kiddie.capitalize()} is a son of {parent.capitalize()}.")
            else:
                print(f"No, {kiddie.capitalize()} is not a son of {parent.capitalize()}.")
        else:
                print("I don't understand.")
    elif words[0] == "Who":
        if len(words) == 6 and words[1]=="are" and words[2] == "the" and words[3] == "sons" and words[4] == "of" and words[5].istitle():
            parent = words[5].lower()
            parent = parent[:-1]
            son_list = util.find_sons(parent,prolog)

            if son_list:
                if len(son_list)>1:
                    last_son = son_list[-1]
                    son_list=son_list[:-1]
                    son_str = ', '.join(son_list) + f" and {last_son}"
                    print(f"{parent.capitalize()}'s sons are {son_str}.")
                else:
                    son_str = son_list[0]
                    print(f"{parent.capitalize()}'s son is {son_str}.")
            else: 
                print(f"I don't know if {parent.capitalize()} has sons.")
        else:
            print("I don't understand.")
    else:
        # Question doesn't start with "Are", "Is", or "Who"
        print("I don't understand.")

def question_child(words, prolog):
    # check if first word is "Is"
    if words[0] == "Is":
        if len(words) == 6 and words[1].istitle() and words[2] == "a" and words[3] == "child" and words[4] == "of" and words[5].istitle():
            kiddie, parent = words[1].lower(),words[5].lower()
            # Remove ? at the end of parent's name
            parent = parent[:-1]
            is_child = util.query_child(kiddie,parent,prolog)

            if is_child:
                print(f"Yes, {kiddie.capitalize()} is a child of {parent.capitalize()}.")
            else:
                print(f"No, {kiddie.capitalize()} is not a child of {parent.capitalize()}.")
        else:
                print("I don't understand.")
    else:
         # Question doesn't start with "Is"
         print("I don't understand.")

def question_children(words, prolog):
    # check if first word is "Are", or "Who"
    if words[0] == "Who":
        if len(words)==6 and words[1] == "are" and words[2] == "the" and words[3] == "children" and words[4] == "of" and words[5].istitle():
            parent = words[5].lower()
            parent = parent[:-1]
            children_list = util.find_children(parent,prolog)

            if children_list:
                if len(children_list) > 1:
                    last_children = children_list[-1]
                    children_list = children_list[:-1]
                    children_str = ', '.join(children_list) + f" and {last_children}"
                    print(f"{children_str} are the children of {parent.capitalize()}.")
                else:
                    children_str = children_list[0]
                    print(f"{children_str} is a child of {parent.capitalize()}.")
            else:
                print(f"I don't know if {parent.capitalize()} has children.")
        else:
            print("I don't understand.")
    elif words[0] == "Are":
        names = []
        for word in words:
            if any(char.istitle() for char in word) and word != "Are":
                names.append(word.lower())
                
        last_child_index = len(names) - 2
        
        for index, name in enumerate(names):
            if name.endswith(',') or name.endswith('?'):
                names[index] = name[:-1]
                
        if len(names) == len(words) - 4 and words[last_child_index + 1] == "and" and words[last_child_index + 3] == "children" and words[last_child_index + 4] == "of" and words[len(words) - 1].istitle():
            children = names[:-1]
            parent = names[-1]
            are_children = True
            
            for child in children:
                is_child = util.query_child(child, parent, prolog)
                
                if not is_child:
                    are_children = False
                    break
                
            if are_children:
                last_child = children[-1]
                children = children[:-1]
                children = [child.capitalize() for child in children]
                children_str = ', '.join(children) + f" and {last_child.capitalize()}"
                print(f"Yes, {children_str} are children of {parent.capitalize()}.")
            else:
                print(f"No, at least one of them is not {parent.capitalize()}'s child.")
        else:
            print("I don't understand.")
    else:
        # Question doesn't start with "Are" or "Who"
        print("I don't understand.")

def question_aunt(words, prolog):
    # check if first word is "Is"
    if words[0] == "Is":
        if len(words) == 6 and words[1].istitle() and words[2] == "an" and words[3] == "aunt" and words[4] == "of" and words[5].istitle():
            aunt, kid = words[1].lower(),words[5].lower()
            # Remove ? at the end
            kid = kid[:-1]
            is_auntie = util.query_aunt(aunt,kid,prolog)

            if is_auntie:
                print(f"Yes, {aunt.capitalize()} is an aunt of {kid.capitalize()}.")
            else:
                print(f"No, {aunt.capitalize()} is not an aunt of {kid.capitalize()}.")
        else:
                print("I don't understand.")
    else:
        # Question doesn't start with "Is"
        print("I don't understand.")

def question_uncle(words, prolog):
    # check if first word is "Is"
    if words[0] == "Is":
        if len(words) == 6 and words[1].istitle() and words[2] == "an" and words[3] == "uncle" and words[4] == "of" and words[5].istitle():
            uncle, kid = words[1].lower(),words[5].lower()
            # Remove ? at the end
            kid = kid[:-1]
            is_uncle = util.query_uncle(uncle,kid, prolog)

            if is_uncle:
                print(f"Yes, {uncle.capitalize()} is an uncle of {kid.capitalize()}.")
            else:
                print(f"No, {uncle.capitalize()} is not an uncle of {kid.capitalize()}.")
        else:
            # Sentence does not follow uncle question pattern
                print("I don't understand.")
    else:
        # Question doesn't start with "Is"
        print("I don't understand.")

def question_relatives(words, prolog):
    # check if first word is "Are"
    if words[0] == "Are":
        if len(words) == 5 and words[1].istitle() and words[2] == "and" and words[3].istitle() and words[4] == "relatives?":
            person1,person2 = words[1].lower(),words[3].lower()
            are_related = util.query_are_related(person1,person2,prolog)

            if are_related:
                print(f"Yes, {person1.capitalize()} and {person2.capitalize()} are relatives.")
            else:
                print(f"No, {person1.capitalize()} and {person2.capitalize()} are not relatives.")
        else:
            # Sentence does not follow relatives question pattern
                print("I don't understand.")
    else:
        # Question doesn't start with "Are"
        print("I don't understand.")
