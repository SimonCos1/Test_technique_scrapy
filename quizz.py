"""
EXERCICE 1
Lancer le Doctest dans un terminal -> python3 -m doctest -v quizz.py

Résultats :
2 items passed all tests:
   3 tests in quizz.sum_all
   4 tests in quizz.sum_fibo
7 tests in 3 items.
7 passed and 0 failed.
Test passed.
"""


def sum_all(elements):
    """EXERCICE 1
    sum of all elements between the two numbers and these two numbers

    :param list elements: list of 2 numbers

    :return: The sum of given numbers.

    >>> sum_all([1, 4])
    10
    >>> sum_all([4, 1])
    10
    >>> sum_all([5, 10])
    45
    """
    elements = sorted(elements)
    elements[1] += 1

    return sum(list(range(elements[0], elements[1])))


"""
EXERCICE 2
J'ai pris le parti ici de ne pas ajouter les tests pour ne pas alourdir inutilement la lecture du code. L'idée étant bien de se concentrer sur l'algo. 
Le code ci-dessous est la version que j'ai codé dans un premier temps. Un code "naïf" qui s'exécute très bien en une fois, mais pas forcément adapté pour 
le lancement de multiples instances. 
J'ai noté les axes d'amélioration que j'ai vu par la suite en commentaires. 
"""


def sum_fibo(number):
    """EXERCICE 2
    It calculates the SUM of the IMPAIRED numbers of the Fibonacci sequence smaller or equal to the integer passed in parameter.

    :param list fibo_elements: list of the sequence's 2 first numbers.
    :param int number: entry of the function.

    :return: The sum of given numbers.

    >>> sum_fibo(4)
    5
    >>> sum_fibo(5)
    10
    >>> sum_fibo(12)
    10
    >>> sum_fibo(13)
    23
    """

    fibo_elements = [1, 1]

    while fibo_elements[-1] <= number:
        fibo_elements.append(fibo_elements[-1] + fibo_elements[-2])

    # purge du dernier élément de le liste si l'élément > number. Cette opération sera exécutée qu'une seule fois.
    if fibo_elements[-1] > number:
        fibo_elements.pop()

    # On fait une passe sur la liste pour supprimer les nombres pairs puis on reste dans le flow du programme pour calculer la somme des valeurs.
    return sum([i for i in fibo_elements if i % 2 != 0])


"""
Axes d'améliorations :
-> Stocker les suites déjà calculées et prugées des chiffres impaires, dans un fichier externe (ou en BDD) 
pour ne pas avoir à recalculer/nettoyer inutilement toute la suite à chaque itération. 
Ainsi le chargement de la suite de chiffres pourra être fait en mémoire une seule fois et servir à plusieurs itérations.

-> Charger la suite déjà calculée sous forme de tuple pour une utilisation mémoire et une rapidité améliorée.

-> Scynder la suite en deux listes ou tuples (L1 et L2) et utililser un algorithme récursif : 
si number <= max(L1)
    rechercher number dans L1 / 2 de la même manière puis une fois number trouvé, charger la suite fico voulue
sinon
    rechercher number dans L2 / 2 de la même manière puis une fois number trouvé, charger la suite fico voulue

De cette manière, nous parcourerons toujours que la moitié de la liste de valeurs existantes.
Cet algorithme de complexité O(Log n) réduit fortement le nombre d'opérations pour arriver au résultat. 
Pour 1000 entrées dans la liste, il nous faudra au plus 10 opérations pour trouver number.
"""
