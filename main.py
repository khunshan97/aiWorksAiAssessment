import json
import pprint


def load_data():
    users = json.load(open('users.json', mode='r', encoding='utf-8'))
    organizations = json.load(open('organizations.json', mode='r', encoding='utf-8'))
    tickets = json.load(open('tickets.json', mode='r', encoding='utf-8'))
    return {'organizations': organizations, 'tickets': tickets, 'users': users}


def search_data(dataset, search_term, search_value):
    if search_term not in dataset[0]:
        print("This field doesn't exist")
        return None
    for item in dataset:
        if item[search_term] == search_value:
            return item
    return None


def select_modal():
    search_type = input('Select 1 for Users, 2 for Tickets, 3 for Organizations: ')
    if search_type == '1':
        search_type = 'users'
    elif search_type == '2':
        search_type = 'tickets'
    elif search_type == '3':
        search_type = 'organizations'
    else:
        print('Invalid input')
        exit()
    return search_type


def search():
    data = load_data()
    modal = select_modal()
    search_term = input("Enter Search term:")
    search_value = input("Enter Search value:")
    print('Searching for {} with a value of {} in {}'.format(search_term, search_value, modal))
    result = search_data(data[modal], search_term, search_value)
    pprint.pprint(result) if result else print('No result found')


def list_fields(data):
    for dataset in data:
        print('--------------------------------')
        print(dataset.capitalize())
        print('--------------------------------')
        for key in data[dataset][0]:
            print(key)
        print('--------------------------------\n\n\n\n')


def menu():
    print("\n")
    choice = input('Select options:\n৹ Type 1 to search\n৹ Type 2 to view fields\n৹ Type quit to exit:\n ')
    if choice == '1':
        search()
        menu()
    elif choice == '2':
        list_fields(load_data())
        menu()
    elif choice == 'quit':
        exit()
    else:
        menu()


if __name__ == '__main__':
    menu()
