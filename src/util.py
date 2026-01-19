def check_sibling_consistency(sibling1, sibling2, prolog):
    is_same = check_is_same(sibling1, sibling2)
    have_different_parents = query_different_parents(sibling1, sibling2, prolog)
    is_parent = query_parent(sibling1, sibling2, prolog) or query_parent(sibling2, sibling1, prolog)
    is_grandparent = query_grandparent(sibling1, sibling2, prolog) or query_grandparent(sibling2, sibling1, prolog)
    is_auntle = query_auntle(sibling1, sibling2, prolog) or query_auntle(sibling2, sibling1, prolog) 
    are_cousins = query_cousins(sibling1, sibling2, prolog)
    
    return not(is_same or have_different_parents or is_parent or is_grandparent or is_auntle or are_cousins)

def check_parent_consistency(parent, child, prolog):
    is_same = check_is_same(parent, child)
    is_child = query_parent(child, parent, prolog)
    are_siblings = query_are_siblings(parent, child, prolog)
    has_two_parents = query_has_two_parents(child, prolog)
    is_grandparent = query_grandparent(parent, child, prolog) or query_grandparent(child, parent, prolog)
    is_auntle = query_auntle(parent, child, prolog) or query_auntle(child, parent, prolog) 
    are_cousins = query_cousins(parent, child, prolog) 
    
    is_related_to_parent = False
    parent2 = get_existing_parent(child, prolog)
    same_parent = check_is_same(parent, parent2)
    
    cant_add_parents = False
    if has_two_parents:
        parents = find_parents(child, prolog)
        if parent not in parents:
            cant_add_parents = True
    
    if parent2 and not has_two_parents and not same_parent and query_are_related(parent, parent2, prolog):
        is_related_to_parent = True
    
    return not(is_same or is_child or are_siblings or is_related_to_parent or is_grandparent or is_auntle or are_cousins or cant_add_parents)

def check_grandparent_consistency(grandparent, grandchild, prolog):
    is_same = check_is_same(grandparent, grandchild)
    is_child = query_parent(grandparent, grandchild, prolog) or query_parent(grandchild, grandparent, prolog)
    are_siblings = query_are_siblings(grandparent, grandchild, prolog)
    has_four_grandparents = query_has_four_grandparents(grandchild, prolog)
    is_grandparent = query_grandparent(grandchild, grandparent, prolog)
    is_auntle = query_auntle(grandparent, grandchild, prolog) or query_auntle(grandchild, grandparent, prolog) 
    are_cousins = query_cousins(grandparent, grandchild, prolog)
    
    cant_add_gparents = False
    if has_four_grandparents:
        gparents = find_grandparents(grandchild, prolog)
        if grandparent not in gparents:
            cant_add_gparents = True
    
    return not(is_same or is_child or are_siblings or is_grandparent or is_auntle or are_cousins or cant_add_gparents)

def check_auntle_consistency(auntle, nibling, prolog):
    is_same = check_is_same(auntle, nibling)
    is_child = query_parent(auntle, nibling, prolog) or query_parent(nibling, auntle, prolog)
    are_siblings = query_are_siblings(auntle, nibling, prolog)
    is_grandparent = query_grandparent(nibling, auntle, prolog) or query_grandparent(auntle, nibling, prolog)
    is_auntle = query_auntle(nibling, auntle, prolog)
    are_cousins = query_cousins(auntle, nibling, prolog)
    
    return not(is_same or is_child or are_siblings or is_grandparent or is_auntle or are_cousins)

def query_female(person, prolog):
    return bool(list(prolog.query(f"female({person}).")))

def query_male(person, prolog):
    return bool(list(prolog.query(f"male({person}).")))

def check_is_same(person1, person2):
    return person1 == person2

def query_share_same_parent(person1, person2, prolog):
    query = f"parent(P, {person1}), parent(P, {person2})"
    return bool(list(prolog.query(query)))

def get_existing_parent(person, prolog):
    query = f"parent(Parent, {person})"
    result = list(prolog.query(query))
    
    return result[0]['Parent'] if result else None

def query_has_two_parents(person, prolog):
    query = f"parent(_, {person})"
    result = list(prolog.query(query))
    
    return len(result) == 2 

def query_has_four_grandparents(person, prolog):
    query = f"grandparent(_, {person})"
    result = list(prolog.query(query))
    
    return len(result) == 4 

def query_are_siblings(person1, person2, prolog):
    query1 = f"sibling({person1}, {person2})"
    query2 = f"sibling({person2}, {person1})"
    
    return bool(list(prolog.query(query1))) and bool(list(prolog.query(query2)))

def query_parent(parent, child, prolog):
    query = f"parent({parent}, {child})"
    return bool(list(prolog.query(query)))

def query_parents(p1, p2, child, prolog):
    query1 = f"parent({p1}, {child})"
    query2 = f"parent({p2}, {child})"
    return bool(list(prolog.query(query1)) and list(prolog.query(query2)))

def query_grandparent(grandparent, grandchild, prolog):
    query = f"grandparent({grandparent}, {grandchild})"
    return bool(list(prolog.query(query)))

def query_different_parents(person1, person2, prolog):
    query = f"parent(P1, {person1.lower()}), parent(P2, {person1.lower()}), parent(P3, {person2.lower()}), parent(P4, {person2.lower()}), P1 \\= P2, P1 \\= P3, P1 \\= P4, P2 \\= P3, P2 \\= P4, P3 \\= P4"
    return bool(list(prolog.query(query)))

def find_siblings(person, prolog):
    query = f"sibling(Sibling, {person})"
    result = list(prolog.query(query))
    
    return list({result_item['Sibling'].capitalize() for result_item in result})

def find_sisters(sibling, prolog):
  query = f"sister(Sister, {sibling})"
  result = list(prolog.query(query))

  return list({result_item['Sister'].capitalize() for result_item in result})

def query_sister(sister, sibling, prolog):
  query = f"sister({sister},{sibling})"
  return bool(list(prolog.query(query)))

def find_brothers(sibling, prolog):
  query = f"brother(Brother, {sibling})"
  result = list(prolog.query(query))

  return list({result_item['Brother'].capitalize() for result_item in result})

def query_brothers(brother, sibling, prolog):
  query = f"brother({brother}, {sibling})"
  return bool(list(prolog.query(query)))

def query_mother(mother,child,prolog):
  query = f"mother({mother}, {child})"
  return bool(list(prolog.query(query)))

def query_father(father,child,prolog):
  query = f"father({father}, {child})"
  return bool(list(prolog.query(query)))

def query_are_related(person1, person2, prolog):
    # is_same = check_is_same(person1, person2)
    # is_parent = query_parent(person1, person2, prolog) or query_parent(person2, person1, prolog)
    # are_siblings = query_are_siblings(person1, person2, prolog)
    # # is_grandparent
    # # is_auntle 
    
    # return is_same or is_parent or are_siblings
    
    query = f"are_related({person1.lower()}, {person2.lower()})"
    return bool(list(prolog.query(query)))

def query_auntle(auntle, nibling, prolog):
    query = f"auntle({auntle}, {nibling})"
    return bool(list(prolog.query(query)))

def query_cousins(person1, person2, prolog):
    query = f"cousins({person1}, {person2})"
    return bool(list(prolog.query(query)))

def query_related_grandparents(grandparent, grandchild, prolog):
    query = f"grandparent(_, {grandchild})"
    gparents = list(prolog.query(query))
    related_count = 0
    
    if len(gparents) == 3:
        for gparent in gparents:
            if query_are_related(grandparent, gparent, prolog):
                related_count += 1
                if related_count == 3:
                    return True
    
    return False

def query_grandmother(grandmother, grandchild, prolog):
  query = f"grandmother({grandmother},{grandchild})"
  return bool(list(prolog.query(query)))

def query_grandfather(grandfather, grandchild, prolog):
  query = f"grandfather({grandfather},{grandchild})"
  return bool(list(prolog.query(query)))

def query_daughter(daughter, parent, prolog):
  query = f"daughter({daughter},{parent})"
  return bool(list(prolog.query(query)))

def query_son(son, parent, prolog):
  query = f"son({son},{parent})"
  return bool(list(prolog.query(query)))

def query_child(child, parent, prolog):
  query = f"child({child},{parent})"
  return bool(list(prolog.query(query)))

def query_aunt(aunt,kid, prolog):
  query = f"aunt({aunt}, {kid})"
  return bool (list(prolog.query(query)))

def query_uncle(uncle, kid, prolog):
  query = f"uncle({uncle},{kid})"
  return bool (list(prolog.query(query)))

def find_mother(child,prolog):
  query = f"mother(Mother, {child})"
  result = list(prolog.query(query))
  
  return result[0]['Mother'].capitalize() if result else None

def find_father(child,prolog):
  query = f"father(Father, {child})"
  result = list(prolog.query(query))
  
  return result[0]['Father'].capitalize() if result else None

def find_parents(child, prolog):
  query = f"parent(Parent, {child})"
  result = list(prolog.query(query))

  return list({result_item['Parent'].capitalize() for result_item in result})

def find_grandparents(child, prolog):
  query = f"grandparent(Gparent, {child})"
  result = list(prolog.query(query))

  return list({result_item['Gparent'].capitalize() for result_item in result})

def find_daughter(parent, prolog):
  query = f"daughter(Daughter, {parent})"
  result = list(prolog.query(query))
  
  return list({result_item['Daughter'].capitalize() for result_item in result})

def find_sons(parent,prolog):
  query = f"son(Son,{parent})"
  result = list(prolog.query(query))
  
  return list({result_item['Son'].capitalize() for result_item in result})

def find_children(parent,prolog):
  query = f"child(Child,{parent})"
  result = list(prolog.query(query))
  
  return list({result_item['Child'].capitalize() for result_item in result})
