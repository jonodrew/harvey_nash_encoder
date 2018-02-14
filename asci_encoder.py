"""
Convert each letter to ASCII value
Convert that integer to binary
concatenate all of those binary numbers
Convert that number back to its 32-bit value
    floor divide the 32-bit value by 85
    pass on the result
    store the remainder
repeat until no remainder
add 33 to each new integer
convert that number back to ASCII
"""
from typing import Union, List


def convert_to_ascii_value(character_to_convert: Union[str, int]) -> int:
    """this function converts a character to its ASCII value"""
    return ord(str(character_to_convert))


def convert_to_binary(int_to_convert: int) -> str:
    return str(bin(int_to_convert))


def concatenate_binary_numbers(list_of_binary_numbers: List[str]) -> str:
    long_word = "".join([word for word in list_of_binary_numbers])
    return long_word.replace('b', '')


def convert_word_to_binary_string(word_to_convert: str) -> str:
    return concatenate_binary_numbers([convert_to_binary(convert_to_ascii_value(letter)) for letter in word_to_convert])


def convert_binary_to_32_bit(binary_word: str) -> int:
    return int(binary_word, 2)


def algorithm_step(thirty_two_bit_int: int, output_list: List[int]) -> List[int]:
    if thirty_two_bit_int <= 1:
        output_list.reverse()
        return output_list
    else:
        output_list.append(thirty_two_bit_int % 85)
        return algorithm_step(thirty_two_bit_int//85, output_list)


def add_33_to_each_number_in_list(list_of_ints: List[int]) -> List[int]:
    return [indie_int + 33 for indie_int in list_of_ints]


def convert_int_to_ascii(int_to_convert: int) -> str:
    return chr(int_to_convert)


def convert_list_of_ints_to_ascii(list_of_ints: List[int])->str:
    return ''.join([convert_int_to_ascii(indie_int) for indie_int in list_of_ints])


def encode_function(string_to_encode: str)-> str:
    converted_word = convert_word_to_binary_string(string_to_encode)
    word_in_32_bits = convert_binary_to_32_bit(converted_word)
    list_of_values = algorithm_step(word_in_32_bits, [])
    list_of_values_plus_33 = add_33_to_each_number_in_list(list_of_values)
    return convert_list_of_ints_to_ascii(list_of_values_plus_33)
