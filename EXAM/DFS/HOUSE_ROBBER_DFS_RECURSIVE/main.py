from solve import *

if __name__ == "__main__":
    # Leer número de casas
    n = int(input().strip())

    # Leer cantidades de dinero en cada casa
    houses = list(map(int, input().strip().split()))

    # Llamar a la función solve
    houses, max_money = solve(houses)

    # Mostrar resultado
    if houses:
        print(f'{houses}:{max_money}')
    else:
        print('No solution')