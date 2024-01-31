def is_anagram(first_string, second_string):
    """Verifica se duas strings são anagramas."""
    # Obtendo as strings ordenadas, ignorando maiúsculas/minúsculas
    ordered_first_string = "".join(sort_string(first_string.lower()))
    ordered_second_string = "".join(sort_string(second_string.lower()))
    # Verificando se as strings ordenadas são iguais
    result = ordered_first_string == ordered_second_string
    # Verificando se uma das strings é vazia, tornando o resultado False
    if first_string == "" or second_string == "":
        result = False

    return ordered_first_string, ordered_second_string, result


def sort_string(string):
    if len(string) <= 1:
        return string

    ordered = string[0]
    order_left = [x for x in string[1:] if x <= ordered]
    order_right = [x for x in string[1:] if x > ordered]

    return sort_string(order_left) + [ordered] + sort_string(order_right)
