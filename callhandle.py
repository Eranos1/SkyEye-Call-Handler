def handle_call(members, all_flights): # Two string arrays. Members contain all members of one flight, eg {"VIKING 11", "VIKING 12"}. all_flights contains all flights currently active, eg. ({"VIKING 11", "VIKING 12"}, {"DARKSTAR", "PYTHON 11", "PYTHON 21", "VIKING 21", "VIKING 22"})
    flight_name = _find_flight_name(members)
    #num_members = len(members)
    is_same_flight = _check_same_flight(members, flight_name)
    is_same_flight_element = _check_same_element(members, flight_name)
    if(is_same_flight_element and is_same_flight_element):
        flight_number = _find_flight_number(members, flight_name)
        return flight_name + " " + flight_number + " FLIGHT"
    if(is_same_flight and is_same_flight_element == False):
        return flight_name + " FLIGHT"
    if(is_same_flight == False and is_same_flight_element == False):
        return _combine_list(members)
    return

def _find_flight_name(members): # Single string array containing all members of a single flight. eg. {"VIKING 11", "VIKING 12"}
    first_member = members[0]
    flight_name_loc = first_member.find(" ")
    return first_member[:flight_name_loc]
def _check_same_element(members, flight_name): # members is a single string array containing all members of a single flight. eg. {"VIKING 11", "VIKING 12"}. flight_name is a string containing the flight name, eg. "VIKING"
    first_member = members[0]
    flight_name_length = len(flight_name)
    flight_numbers = [""] * len(members)
    for x in range(0, len(members)):
        cur_mem = members[x]
        flight_numbers[x] = cur_mem[flight_name_length+1:]
    for x in range(0, len(flight_numbers)):
        flight_numbers[x] = flight_numbers[x].lstrip()
    first_mem_number = flight_numbers[0]
    first_mem_fnum = first_mem_number[0]
    all_same = True
    for x in range(0, len(flight_numbers)):
        cur_flight_num = flight_numbers[x]
        if(cur_flight_num[0] != first_mem_fnum):
            all_same = False
    return all_same
def _check_same_flight(members, flight_name): # Checks if all members of call are of the same flight
    same_flight = True
    for x in range(0, len(members)):
        cur_mem = members[x]
        if(cur_mem[:len(flight_name)] != flight_name):
            same_flight = False
    return same_flight

def _find_flight_number(members, flight_name): # Finds the flight number of a group of aircraft that are the same flight, to properly address
    first_member = members[0]
    return first_member[len(flight_name)+1:len(flight_name)+2]

def _combine_list(members):
    combined_list = ""
    for x in range(0, len(members)):
        combined_list = combined_list + " " + members[x]
    return combined_list.lstrip()