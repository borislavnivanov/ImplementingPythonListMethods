from typing import Any
from multipledispatch import dispatch

lst: list = []


def main():
    global lst
    lst = input('Enter initial list values (comma-separated): ').strip().split(',')

    while True:
        display_menu()
        command = input('Enter your choice (1-12): ')

        match command:
            case '1':
                element = input('Enter new element: ')
                if not element:
                    print('no element provided returning to menu')
                    continue
                lst = append(lst, element)

            case '2':
                element_list: list = input('Enter additional values (comma-separated): ').strip().split(',')
                try:
                    extend(lst, element_list)
                except TypeError as e:
                    print(f'New element must be iterable object - {e}')

            case '3':
                element = input('Enter new element: ')
                if not element:
                    print('No element provided returning to menu')
                    continue
                try:
                    place = int(input('Enter index: '))
                except TypeError:
                    print('Index must be a number')
                    continue
                lst = insert(lst, element, place)

            case '4':
                value = input('Enter value to remove: ')
                try:
                    lst = remove(lst, value)
                except ValueError as e:
                    print(f'Value not found {e}')

            case '5':
                try:
                    place = get_index()
                except ValueError:
                    print('Index must be an integer')
                else:
                    lst = pop(lst, place)

            case '6':
                clear(lst)

            case '7':
                value = input('Enter value to search: ')
                try:
                    start = int(input('Enter start index or press enter for none: '))
                    end = int(input('Enter end index or press enter for none: '))
                except ValueError:
                    print('Start and end must be integers')
                    continue
                try:
                    if start == '' or end == '':
                        x = index(lst, value)
                    else:
                        x = index(lst, value, start, end)
                except ValueError as e:
                    print(f'Value not found {e}')
                else:
                    print(f' Index for "{value}" is - {x}')

            case '8':
                mode = input('Are you looking for an int (press 1) or other (press 2)')
                value = input('Enter value to count: ')
                if mode == 1:
                    try:
                        value = int(value)
                    except ValueError:
                        print('that is not a number, try again')
                        continue
                return count(lst, value)

            case '9':
                lst = sort(lst)
            case '10':
                lst = reverse(lst)
            case '11':
                new_list = copy(lst)
            case '12':
                break

        print(lst)


def display_menu():
    print("\nChoose a list operation:")
    print("1. Append")
    print("2. Extend")
    print("3. Insert")
    print("4. Remove")
    print("5. Pop")
    print("6. Clear")
    print("7. Index")
    print("8. Count")
    print("9. Sort")
    print("10. Reverse")
    print("11. Copy")
    print("12. Exit")


def append(base_list: list, new_element: Any) -> list:
    base_list.append(new_element)
    return base_list


def extend(base_list: list, new_element) -> list | TypeError:
    base_list.extend(new_element)
    return base_list


def insert(base_list: list, new_element: Any, place: int) -> list | IndexError:
    if place > len(base_list):
        raise IndexError
    else:
        base_list.insert(place, new_element)
        return base_list


def remove(base_list: list, value: Any) -> list | ValueError:
    base_list.remove(value)
    return base_list


def pop(base_list: list, place: int) -> list | IndexError:
    base_list.pop(place)
    return base_list


def clear(base_list: list):
    base_list.clear()


@dispatch(list, Any)
def index(base_list: list, value: Any) -> int | ValueError:
    x = base_list.index(value)
    return x


@dispatch(list, Any, int)
def index(base_list: list, value: Any, start: int, end: int) -> int | ValueError:
    x = base_list.index(value, start, end)
    return x


def count(base_list: list, value: int) -> int:
    x = base_list.count(value)
    return x


def sort(base_list: list) -> list:
    base_list.sort()
    return base_list


def reverse(base_list: list) -> list:
    base_list.reverse()
    return base_list


def copy(base_list: list) -> list:
    return base_list.copy()


def get_index() -> int | ValueError:
    place = int(input('Enter index: '))
    return place


if __name__ == '__main__':
    main()
