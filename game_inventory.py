from operator import itemgetter

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']



def display_inventory(inventory):
    for item in inventory.keys():
        print(item, ":" , inventory[item])
    pass

def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    pass




def print_table(inventory,order):
    print('''
-----------------
item name | count
-----------------''')
    if order == "count,desc":
        newlist = sorted(inventory.items(), key=itemgetter(1), reverse=True)
        x = len(newlist)
        y = 0
        for i in range(x):
            if len(str(newlist[i][0])) > y:
                y = len(str(newlist[i][0]))
        for i in range(x):
            print(newlist[i][0].rjust(y), "|",  str(newlist[i][1]).rjust(4))
    if order == "count,asc":
        newlist = sorted(inventory.items(), key=itemgetter(1))
        x = len(newlist)
        y = 0
        for i in range(x):
            if len(str(newlist[i][0])) > y:
                y = len(str(newlist[i][0]))
        for i in range(x):
            print(newlist[i][0].rjust(y), "|",  str(newlist[i][1]).rjust(4))
    print('''
-----------------''')
    pass

def import_inventory(inventory, filename):
    f = open(filename, "r")
    l = f.readline()
    x = l.split(',')
    for item in x:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    print_table(inv)
    pass


def export_inventory(inventory, filename):
    f = open(filename, 'w+')
    for item in inventory:
        f.write(item + ",")
    pass