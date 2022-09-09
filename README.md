# Project Openclassroom : Développez une application Web en utilisant Django
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)  [![forthebadge](https://forthebadge.com/images/badges/built-by-developers.svg)](http://forthebadge.com).

This project aims to create an algorithm that will seek to find among a list of actions, the best possible combination in the but to generate the most profit possible within a limit of a budget defined.


### library and tools

- https://www.djangoproject.com/ Django
- https://pypi.org/project/Pillow/ Pillow


### Prerequisites

Avoir python sur son OS, et créer un environement virtuel avant de faire la suite

you have to install the requirements with the command ``pip3 install -r requirements.txt``


## Launching

Une fois le projet bien configuré, executer la commande ``python3 manage.py makemigration`` puis ``python3 manage.py migrate`` afin d'installer la base de donnée.

Si vous souhaitez lancer le projet pour pouvoir parcourir le site, executer la commande ``python3 manage.py runserver``


## Functional

Once you have launched the algorithm, you will have a result in about 2s for the bruteforce, and -1s for the optimized (the time varies according to the number of actions), and then there will be a print which will give you the gain obtained, the action list chosen, and the budget spent

If you want to see the time you have to uncomment lines 60, 63, 64 for the bruteforce file, and lines 42, 45, 48 for the optimized file, this will add the information of the execution time of the algorithm in your console

If you want to re-generate the complexity graphs, use the command ``python3 -m mccabe --dot bruteforce.py | dot -Tpng -o annexe/bruteforce.png`` for the bruteforce file, and the command ``python3 -m mccabe --dot optimized.py | dot -Tpng -o annexe/optimized.png`` for the optimized file, but you have to get graphviz one you're computer

## Warning

I had a problem with the format of the files that were provided to me, some had the values ​​written ``5%`` while others had ``5``, with the pandas library it's a problem because in the first case, pandas will understand it ``0.05`` or in the second ``5``. To manage this problem, I calculated the average of the percentages, and put a condition ``if average percent > 1`` we will ``value * 0.01``, this allows to manage this format problem.
Be careful though, in the potential case where the average of the percentages is less than 1, the code will have a problem because it will not multiply them by their true value, for example if we have a value equal to ``0.8``, it will calculate it as ``80%`` and not ``0.8%``.


## Made with

* [Visual Studio Code](https://code.visualstudio.com/) - Code editor


## Author

* **Hadrien Louppe Herbet** _alias_ [@herbetelem](https://github.com/herbetelem)
