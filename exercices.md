Partie Python
=============

**EXERCICE 1 :**

Écrire une fonction `sum_all`, qui prend en paramètre un tableau de 2 entiers.

La fonction doit retourner la somme de ces 2 nombres/bornes plus la somme des nombres entre ces deux bornes.

Exemples :
- `sum_all([1, 4]) = 10`
- `sum_all([4, 1]) = 10`
- `sum_all([5, 10]) = 45`

**EXERCICE 2 :**

Écrire une fonction `sum_fibo`, qui prend en paramètre un entier.

Elle calcule la SOMME des nombres IMPAIRS de la suite de Fibonacci plus PETITS OU EGAUX à l'entier passé en paramètre.

Les 2 premiers entiers de la suite de Fibonacci sont 1 et 1. Chaque nouvel entier dans la séquence est la somme des 2 entiers précédents.

Les 6 premiers nombres de la suite de Fibonacci sont donc 1, 1, 2, 3, 5, 8.

Exemple : `sum_fibo(4) = 5` (c'est-à-dire 1 + 1 + 3, car 2 bien inférieur à 4, mais pair ; 5 et les entiers suivants de la suite sont, eux, plus grands que 4).

Il arrive que l'on ait des problématiques de performance. Expliquez en quelques lignes ce que vous avez fait pour améliorer les performances de votre fonction, et/ou ce qu'on pourrait faire pour améliorer encore.

Partie Scrapy
=============

Avec [Scrapy](https://docs.scrapy.org/en/latest/), créer un script pour crawler le site https://www.lipsum.com/.

1. Créer une requête pour récupérer le contenu de cette page.

2. Créer une requête pour soumettre le formulaire de la page principale (bouton "Generate Lorem Ipsum"), demander la génération de 10 paragraphes.

3. Après soumission du formulaire, récupérer le 4ème paragraphe.

4. Récupérer la dernière phrase du paragraphe extrait, et l'afficher dans la sortie standard.