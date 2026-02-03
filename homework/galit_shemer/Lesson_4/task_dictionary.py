def main():
    my_dict = {
        'tuple': (1, 2, 3, 4, 5),
        'list': [10, 20, 30, 40, 50],
        'dict': {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': 4,
            'e': 5
        },
        'set': {100, 200, 300, 400, 500}
    }

    print(my_dict['tuple'][-1])

    my_dict['list'].append(60)
    my_dict['list'].pop(1)

    my_dict['dict'][('i am a tuple',)] = 'value'
    my_dict['dict'].pop('a')

    my_dict['set'].add(600)
    my_dict['set'].remove(100)

    print("tuple:", my_dict['tuple'])
    print("list:", my_dict['list'])
    print("dict:", my_dict['dict'])
    print("set:", my_dict['set'])


if __name__ == "__main__":
    main()
