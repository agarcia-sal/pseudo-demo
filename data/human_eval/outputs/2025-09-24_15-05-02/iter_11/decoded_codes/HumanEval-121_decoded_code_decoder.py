def solution(list_of_integers):
    sum_of_odds_in_even_positions = 0
    for index, element in enumerate(list_of_integers):
        if index % 2 == 0 and element % 2 == 1:
            sum_of_odds_in_even_positions += element
    return sum_of_odds_in_even_positions