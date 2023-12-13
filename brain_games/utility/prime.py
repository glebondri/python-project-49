def is_prime_number(number: int) -> bool:
    """Returns whether a given number prime or not
    :param number:
    :return: Whether a given number prime or not"""

    last_index = number + 1
    prime_numbers = list(range(2, last_index + 1))

    '''
     2  3  4  5  6  7  8  9  10
    11 12 13 14 15 16 17 18 19 20
          ->     ...
    '''
    for index in range(2, last_index):
        '''
         >>2<<  3  4  5  6  7  8  9  10
          11   12 13 14 15 16 17 18 19 20
              ->     ...
        '''
        if index in prime_numbers:

            for n in prime_numbers:
                '''
                "is number in list is multiple to given number?"

                >>2<<  3  [4]  5  [6]  7  [8]  9  [10]
                 11  [12] 13 [14] 15 [16] 17 [18] 19 [20]
                    ->     ...
                '''

                if n != index and n % index == 0:
                    '''removing all the 'multiple' numbers'''
                    prime_numbers.remove(n)

    return number in prime_numbers
