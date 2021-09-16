""" Fantasy Game Inventory"""

player1 = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'ruby']

def displayInventory(inventory):
    # function displaying all inventory and showing total numer of items
    total = 0
    print('Inventory:')
    for item in sorted(inventory.keys()):
        total += inventory[item]
        print('%-3s: %s' % (inventory[item], item))
    return 'Total number of items: %s' % total

def addToInventory(inventory, addedItems):
    # function adding items stored in a list to inventory
    for item in addedItems:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1


if __name__ == '__main__':
    print(displayInventory(player1))
    print(addToInventory(player1, dragonLoot))
    print(displayInventory(player1))