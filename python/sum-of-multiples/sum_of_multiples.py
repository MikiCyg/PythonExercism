def sum_of_multiples(limit, multiples):
    return sum([i for i in range(limit) if any([i % multiples == 0 for multiples in multiples])])



