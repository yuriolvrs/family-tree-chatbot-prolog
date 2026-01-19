import util

# Processes a statement to determine intended relationship
def process_statement(statement, prolog):
    # Split the statement into individual words
    words = statement.split()

    # Look for valid keywords in the statement, 
    # then call the appropriate method based on its mapping
    keyword_mapping = {
        "siblings.": assert_siblings, 
        "brother": assert_brother, 
        "sister": assert_sister, 
        "father": assert_father, 
        "mother": assert_mother, 
        "parents": assert_parents, 
        "grandmother": assert_grandmother, 
        "grandfather": assert_grandfather, 
        "child": assert_child, 
        "children": assert_children, 
        "daughter": assert_daughter, 
        "son": assert_son, 
        "uncle": assert_uncle, 
        "aunt": assert_aunt
    }

    for word in words:
        if word in keyword_mapping:
            # Construct function call based on keyword
            keyword_mapping[word](words, prolog)
            break
    else:
        # No valid keywords found
        print("I don't understand.")

def assert_siblings(words, prolog):
    # Concatenate words from index 3 to 4 to get "are siblings."
    phrase = " ".join(words[3:5])

    # Check for valid statement pattern
    if len(words) == 5 and words[0].istitle() and words[1] == "and" and words[2].istitle() and phrase == "are siblings.":
        while True:
            sibling1, sibling2 = words[0].lower(), words[2].lower()
            
            # Construct Prolog facts to be asserted
            sibling_fact1 = f"sibling({sibling1}, {sibling2})"
            sibling_fact2 = f"sibling({sibling2}, {sibling1})"
            
            relationship_exists = list(prolog.query(sibling_fact1))
            is_consistent = util.check_sibling_consistency(sibling1, sibling2, prolog)
            
            if relationship_exists:
                # Does not make a duplicate assertion
                print("I already knew that!")
                break
            
            if is_consistent:
                # Assert siblings to Prolog database
                prolog.assertz(sibling_fact1)
                prolog.assertz(sibling_fact2)
                
                print("OK! I learned something.")
                break
            else:
                # Learned relationships aren't consistent with siblings being asserted
                print("That's impossible!")
                break
    else:
        # Sentence does not follow sibling statement pattern
        print("I don't understand.")

def assert_brother(words, prolog):
    # Concatenate words from index 1 to 4 to get "is a brother of"
    phrase = " ".join(words[1:5])

    # Check for valid statement pattern
    if len(words) == 6 and words[0].istitle() and phrase == "is a brother of" and words[5].istitle():
        while True:
            brother, sibling = words[0].lower(), words[5].lower()
            # Remove period at the end of sibling's name
            sibling = sibling[:-1]
            
            # Construct Prolog facts to be asserted
            brother_fact = f"brother({brother}, {sibling})"
            sibling_fact1 = f"sibling({brother}, {sibling})"
            sibling_fact2 = f"sibling({sibling}, {brother})"
            male_fact = f"male({brother})"
            
            relationship_exists = list(prolog.query(brother_fact))
            is_male = util.query_male(brother, prolog)
            is_female = util.query_female(brother, prolog)
            are_siblings = util.query_are_siblings(brother, sibling, prolog)
            is_consistent = util.check_sibling_consistency(brother, sibling, prolog)
            
            if relationship_exists:
                # Does not make a duplicate assertion
                print("I already knew that!")
                break
            
            if is_female or not is_consistent:
                print(f"That's impossible!")
                break
            
            if is_male:
                if not are_siblings:
                    # Assert siblings to Prolog database
                    prolog.assertz(sibling_fact1)
                    prolog.assertz(sibling_fact2)
                
                # Assert brothers to Prolog database
                prolog.assertz(brother_fact)
                
                print("OK! I learned something.")
                break
            else:
                # Assert brother as male to Prolog database
                prolog.assertz(male_fact)
                
                if not are_siblings:
                    # Assert siblings to Prolog database
                    prolog.assertz(sibling_fact1)
                    prolog.assertz(sibling_fact2)
                
                # Assert brothers to Prolog database
                prolog.assertz(brother_fact)
                
                print("OK! I learned something.")
                break
    else:
        # Sentence does not follow brother statement pattern
        print("I don't understand.")

def assert_sister(words, prolog):
    # Concatenate words from index 1 to 4 to get "is a sister of"
    phrase = " ".join(words[1:5])

    # Check for valid statement pattern
    if len(words) == 6 and words[0].istitle() and phrase == "is a sister of" and words[5].istitle():
        while True:
            sister, sibling = words[0].lower(), words[5].lower()
            # Remove period at the end of sibling's name
            sibling = sibling[:-1]
            
            # Construct Prolog facts to be asserted
            sister_fact = f"sister({sister}, {sibling})"
            sibling_fact1 = f"sibling({sister}, {sibling})"
            sibling_fact2 = f"sibling({sibling}, {sister})"
            female_fact = f"female({sister})"
            
            relationship_exists = list(prolog.query(sister_fact))
            is_male = util.query_male(sister, prolog)
            is_female = util.query_female(sister, prolog)
            are_siblings = util.query_are_siblings(sister, sibling, prolog)
            is_consistent = util.check_sibling_consistency(sister, sibling, prolog)
            
            if relationship_exists:
                # Does not make a duplicate assertion
                print("I already knew that!")
                break
            
            if is_male or not is_consistent:
                print(f"That's impossible!")
                break
            
            if is_female:
                if not are_siblings:
                    # Assert siblings to Prolog database
                    prolog.assertz(sibling_fact1)
                    prolog.assertz(sibling_fact2)
                
                # Assert sisters to Prolog database
                prolog.assertz(sister_fact)
                
                print("OK! I learned something.")
                break
            else:
                # Assert sister as female to Prolog database
                prolog.assertz(female_fact)
                
                if not are_siblings:
                    # Assert siblings to Prolog database
                    prolog.assertz(sibling_fact1)
                    prolog.assertz(sibling_fact2)
                
                # Assert sisters to Prolog database
                prolog.assertz(sister_fact)
                
                print("OK! I learned something.")
                break
    else:
        # Sentence does not follow sister statement pattern
        print("I don't understand.")

def assert_father(words, prolog):
    # Concatenate words from index 1 to 4 to get "is the father of"
    phrase = " ".join(words[1:5])

    # Check for valid statement pattern
    if len(words) == 6 and words[0].istitle() and phrase == "is the father of" and words[5].istitle():
        while True:
            father, child = words[0].lower(), words[5].lower()
            # Remove period at the end of child's name
            child = child[:-1]
            
            # Construct Prolog facts to be asserted
            father_fact = f"father({father}, {child})"
            parent_fact = f"parent({father}, {child})"
            male_fact = f"male({father})"
            child_fact = f"child({child}, {father})"
            
            relationship_exists = list(prolog.query(father_fact))
            is_female = util.query_female(father, prolog)
            is_male = util.query_male(father, prolog)
            is_consistent = util.check_parent_consistency(father, child, prolog)
            is_parent = util.query_parent(father, child, prolog)
            is_child = util.query_parent(child, father, prolog)
            
            if relationship_exists:
                # Does not make a duplicate assertion
                print("I already knew that!")
                break
            
            if is_female or not is_consistent:
                print(f"That's impossible!")
                break
            
            if is_male:
                if not is_parent:
                    # Assert father as parent to Prolog database
                    prolog.assertz(parent_fact)
                    
                if not is_child:
                    # Assert child to Prolog database
                    prolog.assertz(child_fact)
                    
                # Assert father to Prolog database
                prolog.assertz(father_fact)
                
                print("OK! I learned something.")
                break
            else:
                # Assert father as male to Prolog database
                prolog.assertz(male_fact)
                
                if not is_parent:
                    # Assert father as parent to Prolog database
                    prolog.assertz(parent_fact)
                    
                if not is_child:
                    # Assert child to Prolog database
                    prolog.assertz(child_fact)
                    
                # Assert father to Prolog database
                prolog.assertz(father_fact)
                
                print("OK! I learned something.")
                break
    else:
        # Sentence does not follow father statement pattern
        print("I don't understand.")

def assert_mother(words, prolog):
    # Concatenate words from index 1 to 4 to get "is the mother of"
    phrase = " ".join(words[1:5])

    # Check for valid statement pattern
    if len(words) == 6 and words[0].istitle() and phrase == "is the mother of" and words[5].istitle():
        while True:
            mother, child = words[0].lower(), words[5].lower()
            # Remove period at the end of child's name
            child = child[:-1]
            
            # Construct Prolog facts to be asserted
            mother_fact = f"mother({mother}, {child})"
            parent_fact = f"parent({mother}, {child})"
            female_fact = f"female({mother})"
            child_fact = f"child({child}, {mother})"
            
            relationship_exists = list(prolog.query(mother_fact))
            is_male = util.query_male(mother, prolog)
            is_female = util.query_female(mother, prolog)
            is_consistent = util.check_parent_consistency(mother, child, prolog)
            is_parent = util.query_parent(mother, child, prolog)
            is_child = util.query_parent(child, mother, prolog)
            
            if relationship_exists:
                # Does not make a duplicate assertion
                print("I already knew that!")
                break
            
            if is_male or not is_consistent:
                print(f"That's impossible!")
                break
            
            if is_female:
                if not is_parent:
                    # Assert mother as parent to Prolog database
                    prolog.assertz(parent_fact)
                    
                if not is_child:
                    # Assert child to Prolog database
                    prolog.assertz(child_fact)
                    
                # Assert mother to Prolog database
                prolog.assertz(mother_fact)
                
                print("OK! I learned something.")
                break
            else:
                # Assert mother as female to Prolog database
                prolog.assertz(female_fact)
                
                if not is_parent:
                    # Assert mother as parent to Prolog database
                    prolog.assertz(parent_fact)
                    
                if not is_child:
                    # Assert child to Prolog database
                    prolog.assertz(child_fact)
                    
                # Assert mother to Prolog database
                prolog.assertz(mother_fact)
                
                print("OK! I learned something.")
                break
    else:
        # Sentence does not follow mother statement pattern
        print("I don't understand.")

def assert_parents(words, prolog):
    # Concatenate words from index 3 to 6 to get "are the parents of"
    phrase = " ".join(words[3:7])
    
    # Check for valid statement pattern
    if len(words) == 8 and words[0].istitle() and words[1] == "and" and words[2].istitle() and phrase == "are the parents of" and words[7].istitle():
        while True:
            parent1, parent2, child = words[0].lower(), words[2].lower(), words[7].lower()
            # Remove period at the end of child's name
            child = child[:-1]
            
            # Construct Prolog facts to be asserted
            parent1_fact = f"parent({parent1}, {child})"
            parent2_fact = f"parent({parent2}, {child})"
            child1_fact = f"parent({child}, {parent1})"
            child2_fact = f"parent({child}, {parent2})"
            
            relationship1_exists = list(prolog.query(parent1_fact))
            relationship2_exists = list(prolog.query(parent2_fact))
            are_not_related = not util.query_are_related(parent1, parent2, prolog)
            is_consistent1 = util.check_parent_consistency(parent1, child, prolog) and are_not_related
            is_consistent2 = util.check_parent_consistency(parent2, child, prolog) and are_not_related
            is_child1 = util.query_parent(child, parent1, prolog)
            is_child2 = util.query_parent(child, parent2, prolog)
            learned_something = False;
            
            if relationship1_exists and relationship2_exists:
                # Does not make a duplicate assertion
                print("I already knew that!")
                break
            
            if not is_consistent1 and not is_consistent2:
                print("That's impossible!")
                break
            
            if not relationship1_exists:
                if is_consistent1:
                    if not is_child1:
                        prolog.assertz(child1_fact)
                        
                    prolog.assertz(parent1_fact)
                    learned_something = True
            
            if not relationship2_exists:
                if is_consistent2:
                    if not is_child2:
                        prolog.assertz(child2_fact)
                    prolog.assertz(parent2_fact)
                    learned_something = True
                    
            if learned_something:
                print("OK! I learned something.")
            else:
                print("That's impossible!")
            
            break

def assert_grandmother(words, prolog):
    # Concatenate words from index 1 to 4 to get "is a grandmother of"
    phrase = " ".join(words[1:5])
    
    # Check for valid statement pattern
    if len(words) == 6 and words[0].istitle() and phrase == "is a grandmother of" and words[5].istitle():
        while True:
            grandmother, grandchild = words[0].lower(), words[5].lower()
            grandchild = grandchild[:-1]
            
            # Construct Prolog facts to be asserted
            grandmother_fact = f"grandmother({grandmother}, {grandchild})"
            female_fact = f"female({grandmother})"
            grandchild_fact = f"grandchild({grandchild}, {grandmother})"
            
            relationship_exists = list(prolog.query(grandmother_fact))
            is_female = util.query_female(grandmother, prolog)
            is_male = util.query_male(grandmother, prolog)
            is_consistent = util.check_grandparent_consistency(grandmother, grandchild, prolog)
            is_grandchild = util.query_grandparent(grandmother, grandchild, prolog)
            
            if relationship_exists:
                # Does not make a duplicate assertion
                print("I already knew that!")
                break
            
            if is_male or not is_consistent:
                print(f"That's impossible!")
                break
            
            if is_female:
                if not is_grandchild:
                    prolog.assertz(grandchild_fact)
                
                prolog.assertz(grandmother_fact)
                print("OK! I learned something.")
                
                break
            else:
                if not is_grandchild:
                    prolog.assertz(grandchild_fact)
                    
                prolog.assertz(female_fact)
                prolog.assertz(grandmother_fact)
                print("OK! I learned something.")
                
                break
    else:
        # Wrong statement pattern
        print("I don't understand.")

def assert_grandfather(words, prolog):
    # Concatenate words from index 1 to 4 to get "is a grandfather of"
    phrase = " ".join(words[1:5])
    
    # Check for valid statement pattern
    if len(words) == 6 and words[0].istitle() and phrase == "is a grandfather of" and words[5].istitle():
        while True:
            grandfather, grandchild = words[0].lower(), words[5].lower()
            grandchild = grandchild[:-1]
            
            # Construct Prolog facts to be asserted
            grandfather_fact = f"grandfather({grandfather}, {grandchild})"
            male_fact = f"male({grandfather})"
            grandchild_fact = f"grandchild({grandchild}, {grandfather})"
            
            relationship_exists = list(prolog.query(grandfather_fact))
            is_female = util.query_female(grandfather, prolog)
            is_male = util.query_male(grandfather, prolog)
            is_consistent = util.check_grandparent_consistency(grandfather, grandchild, prolog)
            is_grandchild = util.query_grandparent(grandfather, grandchild, prolog)
            
            if relationship_exists:
                # Does not make a duplicate assertion
                print("I already knew that!")
                break
            
            if is_female or not is_consistent:
                print(f"That's impossible!")
                break
            
            if is_male:
                if not is_grandchild:
                    prolog.assertz(grandchild_fact)
                    
                prolog.assertz(grandfather_fact)
                print("OK! I learned something.")
                
                break
            else:
                if not is_grandchild:
                    prolog.assertz(grandchild_fact)
                    
                prolog.assertz(male_fact)
                prolog.assertz(grandfather_fact)
                print("OK! I learned something.")
                
                break
    else:
        # Wrong statement pattern
        print("I don't understand.")

def assert_child(words, prolog):
    # Concatenate words from index 1 to 4 to get "is a child of"
    phrase = " ".join(words[1:5])
    
    # Check for valid statement pattern
    if len(words) == 6 and words[0].istitle() and phrase == "is a child of" and words[5].istitle():
        while True:
            child, parent = words[0].lower(), words[5].lower()
            parent = parent[:-1]
            
            # Construct Prolog facts to be asserted
            child_fact = f"child({child}, {parent})"
            parent_fact = f"parent({parent}, {child})"
            
            relationship_exists = list(prolog.query(child_fact))
            is_consistent = util.check_parent_consistency(parent, child, prolog)
            is_parent = util.query_parent(parent, child, prolog)
            
            if relationship_exists:
                # Does not make a duplicate assertion
                print("I already knew that!")
                break
            
            if is_consistent:
                if not is_parent:
                    prolog.assertz(parent_fact)
                    
                prolog.assertz(child_fact)
                print("OK! I learned something")
                break
            else:
                print("That's impossible!")
                break
    else:
        # Wrong statement pattern
        print("I don't understand.")

def assert_children(words, prolog):
    # Take all uppercase letters in the statement and store them in names[]
    names = []
    for word in words:
        if any(char.istitle() for char in word):
            names.append(word.lower())
            
    last_child_index = len(names) - 2
    
    #  Remove comma from the end of names except for the last child
    for index, name in enumerate(names):
        if name.endswith(',') or name.endswith('.'):
            names[index] = name[:-1]
        
    # Concatenate words to get "are children of"
    phrase = " ".join(words[len(names):len(words) - 1])
            
    if len(names) == len(words) - 4 and words[last_child_index] == "and" and phrase == "are children of" and words[len(words) - 1].istitle():
        # print("Names:", names)
        while True:
            children = names[:-1]
            parent = names[-1]
            learned_something = False
            already_know = False
            
            # children_facts = []
            # parent_facts = []
            
            for child in children:
                child_fact = f"child({child}, {parent})"
                parent_fact = f"parent({parent}, {child})"
                
                # children_facts.append(child_fact)
                # parent_facts.append(parent_fact)
                
                relationship_exists = list(prolog.query(child_fact))
                is_consistent = util.check_parent_consistency(parent, child, prolog)
                is_parent = util.query_parent(parent, child, prolog)
                
                if relationship_exists:
                    already_know = True
                elif is_consistent:
                    if not is_parent:
                        prolog.assertz(parent_fact)

                    prolog.assertz(child_fact)
                    learned_something = True
                
            if learned_something:
                print("OK! I learned something.")
            else:
                if not already_know:
                    print("That's impossible!")
                else:
                    print("I already knew that!")
                    
            break
    else:
        # Wrong statement pattern
        print("I don't understand.")
    

def assert_daughter(words, prolog):
    # Concatenate words from index 1 to 4 to get "is a daughter of"
    phrase = " ".join(words[1:5])
    
    # Check for valid statement pattern
    if len(words) == 6 and words[0].istitle() and phrase == "is a daughter of" and words[5].istitle():
        while True:
            daughter, parent = words[0].lower(), words[5].lower()
            parent = parent[:-1]

            # Construct Prolog facts to be asserted
            daughter_fact = f"daughter({daughter}, {parent})"
            child_fact = f"child({daughter}, {parent})"
            parent_fact = f"parent({parent}, {daughter})"
            female_fact = f"female({daughter})"

            # Condition variables
            relationship_exists = list(prolog.query(daughter_fact))
            is_male = util.query_male(daughter, prolog)
            is_female = util.query_female(daughter, prolog)
            is_consistent = util.check_parent_consistency(parent, daughter, prolog)
            is_child = util.query_parent(daughter, parent, prolog)
            is_parent = util.query_parent(parent, daughter, prolog)
            
            if relationship_exists:
                # Does not make a duplicate assertion
                print("I already knew that!")
                break
            
            if is_male or not is_consistent:
                print(f"That's impossible!")
                break
            
            if is_female:
                if not is_child:
                    # Assert daughter as child to Prolog database
                    prolog.assertz(child_fact)
                    
                if not is_parent:
                    # Assert parent to Prolog database
                    prolog.assertz(parent_fact)
                    
                # Assert daughter to Prolog database
                prolog.assertz(daughter_fact)
                print("OK! I learned something.")
                break
            else:
                # Assert daughter as female to Prolog database
                prolog.assertz(female_fact)
                
                if not is_child:
                    # Assert daughter as child to Prolog database
                    prolog.assertz(child_fact)
                    
                if not is_parent:
                    # Assert parent to Prolog database
                    prolog.assertz(parent_fact)
                    
                # Assert daughter to Prolog database
                prolog.assertz(daughter_fact)
                print("OK! I learned something.")
                break
    else:
        # Wrong statement pattern
        print("I don't understand.")

def assert_son(words, prolog):
    # Concatenate words from index 1 to 4 to get "is a son of"
    phrase = " ".join(words[1:5])
    
    # Check for valid statement pattern
    if len(words) == 6 and words[0].istitle() and phrase == "is a son of" and words[5].istitle():
        while True:
            son, parent = words[0].lower(), words[5].lower()
            parent = parent[:-1]

            # Construct Prolog facts to be asserted
            son_fact = f"son({son}, {parent})"
            child_fact = f"child({son}, {parent})"
            parent_fact = f"parent({parent}, {son})"
            male_fact = f"male({son})"

            # Condition variables
            relationship_exists = list(prolog.query(son_fact))
            is_male = util.query_male(son, prolog)
            is_female = util.query_female(son, prolog)
            is_consistent = util.check_parent_consistency(parent, son, prolog)
            is_child = util.query_parent(son, parent, prolog)
            is_parent = util.query_parent(parent, son, prolog)
            
            if relationship_exists:
                # Does not make a duplicate assertion
                print("I already knew that!")
                break
            
            if is_female or not is_consistent:
                print(f"That's impossible!")
                break
            
            if is_male:
                if not is_child:
                    # Assert son as child to Prolog database
                    prolog.assertz(child_fact)
                    
                if not is_parent:
                    # Assert parent to Prolog database
                    prolog.assertz(parent_fact)
                    
                # Assert son to Prolog database
                prolog.assertz(son_fact)
                print("OK! I learned something.")
                break
            else:
                # Assert son as female to Prolog database
                prolog.assertz(male_fact)
                
                if not is_child:
                    # Assert son as child to Prolog database
                    prolog.assertz(child_fact)
                    
                if not is_parent:
                    # Assert parent to Prolog database
                    prolog.assertz(parent_fact)
                    
                # Assert son to Prolog database
                prolog.assertz(son_fact)
                print("OK! I learned something.")
                break
    else:
        # Wrong statement pattern
        print("I don't understand.")

def assert_uncle(words, prolog):
    # Concatenate words from index 1 to 4 to get "is an uncle of"
    phrase = " ".join(words[1:5])
    
    # Check for valid statement pattern
    if len(words) == 6 and words[0].istitle() and phrase == "is an uncle of" and words[5].istitle():
        while True:
            uncle, nibling = words[0].lower(), words[5].lower()
            nibling = nibling[:-1]

            # Construct Prolog facts to be asserted
            uncle_fact = f"uncle({uncle}, {nibling})"
            auntle_fact = f"auntle({uncle}, {nibling})"
            nibling_fact = f"nibling({nibling}, {uncle})"
            male_fact = f"male({uncle})"

            # Condition variables
            relationship_exists = list(prolog.query(uncle_fact))
            is_male = util.query_male(uncle, prolog)
            is_female = util.query_female(uncle, prolog)
            is_consistent = util.check_auntle_consistency(uncle, nibling, prolog)
            is_auntle = util.query_auntle(uncle, nibling, prolog)
            is_nibling = util.query_auntle(nibling, uncle, prolog)
            
            if relationship_exists:
                # Does not make a duplicate assertion
                print("I already knew that!")
                break
            
            if is_female or not is_consistent:
                print(f"That's impossible!")
                break
            
            if is_male:
                if not is_auntle:
                    prolog.assertz(auntle_fact)
                    
                if not is_nibling:
                    prolog.assertz(nibling_fact)
                    
                prolog.assertz(uncle_fact)
                print("OK! I learned something.")
                break
            else:
                prolog.assertz(male_fact)
                
                if not is_auntle:
                    prolog.assertz(auntle_fact)
                    
                if not is_nibling:
                    prolog.assertz(nibling_fact)
                    
                prolog.assertz(uncle_fact)
                print("OK! I learned something.")
                break
    else:
        # Wrong statement pattern
        print("I don't understand.")

def assert_aunt(words, prolog):
    # Concatenate words from index 1 to 4 to get "is an aunt of"
    phrase = " ".join(words[1:5])
    
    # Check for valid statement pattern
    if len(words) == 6 and words[0].istitle() and phrase == "is an aunt of" and words[5].istitle():
        while True:
            aunt, nibling = words[0].lower(), words[5].lower()
            nibling = nibling[:-1]

            # Construct Prolog facts to be asserted
            aunt_fact = f"aunt({aunt}, {nibling})"
            auntle_fact = f"auntle({aunt}, {nibling})"
            nibling_fact = f"nibling({nibling}, {aunt})"
            female_fact = f"female({aunt})"

            # Condition variables
            relationship_exists = list(prolog.query(aunt_fact))
            is_male = util.query_male(aunt, prolog)
            is_female = util.query_female(aunt, prolog)
            is_consistent = util.check_auntle_consistency(aunt, nibling, prolog)
            is_auntle = util.query_auntle(aunt, nibling, prolog)
            is_nibling = util.query_auntle(nibling, aunt, prolog)
            
            if relationship_exists:
                # Does not make a duplicate assertion
                print("I already knew that!")
                break
            
            if is_male or not is_consistent:
                print(f"That's impossible!")
                break
            
            if is_female:
                if not is_auntle:
                    prolog.assertz(auntle_fact)
                    
                if not is_nibling:
                    prolog.assertz(nibling_fact)
                    
                prolog.assertz(aunt_fact)
                print("OK! I learned something.")
                break
            else:
                prolog.assertz(female_fact)
                
                if not is_auntle:
                    prolog.assertz(auntle_fact)
                    
                if not is_nibling:
                    prolog.assertz(nibling_fact)
                    
                prolog.assertz(aunt_fact)
                print("OK! I learned something.")
                break
    else:
        # Wrong statement pattern
        print("I don't understand.")
    
