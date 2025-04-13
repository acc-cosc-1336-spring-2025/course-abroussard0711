#


def add_inventory(widgets, widget_name, quantity):

    if widget_name in widgets:
        widgets[widget_name] += quantity
        
    else:
        widgets[widget_name] = quantity


def remove_widget_inventory (widgets, widget_name):

    if widget_name in widgets:
        del widgets [widget_name]
        return 'Record deleted.'
    else:
        print ('Widget not found.')
    
    
def print_inventory (widgets):
    print ('\nCurrent Inventory:')
    if not widgets:
        print ('Inventory is empty')
    else:
        for name, qty in widgets.items ():
            print ('{name}, {qty}')
    print ()