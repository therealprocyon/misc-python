#!/usr/bin/env python3
import platform
import array
import json


def main():

#    print("Hello, world!")

    os_name = platform.uname()
    array_uname_1 = ["System", "Node", "Release", "Version", "Machine",\
                    "Processor"]
    array_uname_2 = []
    for i in os_name:
        array_uname_2.append(i)
        
#    print(array_uname_1 + array_uname_2)

    dictionary_uname = dict(zip(array_uname_1,array_uname_2))
#    print(dictionary_uname)

    json_uname = json.dumps(dictionary_uname)
#    print(json_uname)

    with open('uname.json', 'a+') as file:
        file.write(f'{json_uname}')


if __name__ == "__main__":
    main()
