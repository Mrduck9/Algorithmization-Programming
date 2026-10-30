"""Ходкин 9/3-РПО-24/2"""

# Время: как растёт число операций с ростом входа.
TIME = {
    "01_find_pass": "O(n)",
    "02_first_and_last": "O(1)",
    "03_has_duplicate_badges": "O(n^2)",
    "04_has_duplicate_badges_fast": "O(n)",
    "05_three_cheapest": "O(n log n)",
    "06_find_receipt": "O(log n)",
    "07_average_and_spikes": "O(n)",
    "08_closest_pair_distance": "O(n^2)",
    "09_word_counts": "O(n)",
    "10_unique_keep_order": "O(n^2)",
    "11_halving_steps": "O(log n)",
    "12_merge_sorted": "O(n + m)",
}

# Память: сколько функция занимает дополнительно к тому, что ей передали.
SPACE = {
    "01_find_pass": "O(1)",
    "02_first_and_last": "O(1)",
    "03_has_duplicate_badges": "O(1)",
    "04_has_duplicate_badges_fast": "O(n)",
    "05_three_cheapest": "O(n)",
    "06_find_receipt": "O(1)",
    "07_average_and_spikes": "O(1)",
    "08_closest_pair_distance": "O(1)",
    "09_word_counts": "O(n)",
    "10_unique_keep_order": "O(n)",
    "11_halving_steps": "O(1)",
    "12_merge_sorted": "O(n + m)",
}

# Худший случай двух фрагментов — одной строкой: при каком входе
# работы больше всего и почему.
WORST_CASE = {
    "01_find_pass": "O(n), так как искомого пропуска может не оказаться на входе, "
                    "либо он будет находиться в конце списка",
    "04_has_duplicate_badges_fast": "O(n), так как в списке может не быть повторяющихся элементов, "
                                    "и тогда алгоритм полностью пройдёт входной список один раз",
}
