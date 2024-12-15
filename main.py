import callhandle as ch
print(ch.handle_call(["VIKING 11", "VIKING 12", "VIKING 13"], ["DARKSTAR", "PYTHON 11", "PYTHON 21", "VIKING 21", "VIKING 22"])) # One Element
print(ch.handle_call(["VIKING 11", "VIKING 12", "VIKING 21"], ["DARKSTAR", "PYTHON 11", "PYTHON 21", "VIKING 21", "VIKING 22"])) # Two element
print(ch.handle_call(["VIKING 11", "VIKING 12", "PYTHON 21"], ["DARKSTAR", "PYTHON 11", "PYTHON 21", "VIKING 21", "VIKING 22"])) # Not all same flight
print(ch._find_flight_name(["VIKING 11", "VIKING 12", "VIKING 13"]))
print(ch._find_flight_name(["PYTHON 11", "PYTHON 12", "PYTHON 13"]))
print(ch._check_same_flight(["VIKING 11", "VIKING 12", "VIKING 13"], "VIKING"))
print(ch._check_same_flight(["VIKING 11", "VIKING 12", "PYTHON 13"], "VIKING"))