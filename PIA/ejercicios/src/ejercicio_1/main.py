
def process_numbers(nums):

    # Se revisa si no existe ningun numero de la lista
    if not nums:
        return []
        # Se retornan ordenados y sin duplicados los numeros positivos.
    return sorted(set(n for n in nums if n >= 0))

def main():
    ejemplo = [4, -1, 2, 4, 3, -5, 2]
    print(process_numbers(ejemplo))

if __name__ == "__main__":
    main()
