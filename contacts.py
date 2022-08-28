
from typing import Dict, List


def add_contact(contact: str, contacts: Dict[str, int]):
    for i in range(len(contact) + 1):
        contacts[contact[:i]] = 1


def find_partial(contact: str, contacts: Dict[str, int]) -> int:
    if contact not in contacts:
        return 0

    contacts[contact] += 1
    return contacts[contact]


def contacts(queries: List[List[str]]) -> List[int]:
    contacts: Dict[str, int] = {}    
    results: List[int] = []

    for query in queries:
        if query[0] == 'add':
            add_contact(query[1], contacts)
        elif query[0] == 'find':
            result = find_partial(query[1], contacts)
            results.append(result)
    
    return results


if __name__ == '__main__':
    queries: List[List[str]] = []

    quantity = int(input("Ingresa la cantidad de consultas que realizaras: "))

    for i in range(quantity):
        query = input()
        queries.append(query.rstrip().split(" "))

    results = contacts(queries)

    print('\n'.join(map(str, results)))