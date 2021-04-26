print("-- DISCLAIMER --")
print("This project was made in just a few hours and")
print("very insecure, it is reccomended not to use it.\n")
print("If you do, however, want to use it, use it at your")
print("own risk.\n")
print("You are also only allowed to make one password saved.")
print("passwords.json will automatically be created")
print("-- DISCLAIMER --")

try:
    import json
    print("Module 'json' imported successfully")
except ImportError:
    print("Unable to import module 'json', try updating or re-installing module 'json'")

def w_p_s(service, password):
    dmp_j = {
        service: password
    }

    with open('passwords.json', 'w') as j_f:
        json.dump(dmp_j, j_f, indent=4, sort_keys=True)

while True:
    try:
        print("Service and password (space seperated)")
        s_p = input()
        s_p_l = list(s_p.split(' '))

        if len(s_p_l) > 2 or len(s_p_l) < 2:
            print('Correct usage: service password')
        else:
            w_p_s(s_p_l[0], s_p_l[1])
            print("Set service and password to", s_p_l[0], ":", s_p_l[1])
    except KeyboardInterrupt:
        print(" CTRL + C pressed; operation ended")
        break
    
