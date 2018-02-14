import asci_encoder as ae


def test_ascii_converter():
    assert ae.convert_to_ascii_value('A') == 65
    assert ae.convert_to_ascii_value('a') == 97
    assert ae.convert_to_ascii_value(7) == 55
    assert ae.convert_to_ascii_value('s') == 115


def test_binary_converter():
    assert ae.convert_to_binary(65) == '0b1000001'
    assert ae.convert_to_binary(97) == '0b1100001'
    assert ae.convert_to_binary(55) == '0b110111'
    assert '0b1110011' == ae.convert_to_binary(ae.convert_to_ascii_value('s'))


def test_concatenator():
    assert ae.concatenate_binary_numbers(['0b1000001', '0b1100001', '0b110111']) == '01000001011000010110111'
    assert '01110011011101010111001001100101' == ae.concatenate_binary_numbers([ae.convert_to_binary(115),
                                                                                ae.convert_to_binary(117),
                                                                                ae.convert_to_binary(114),
                                                                                ae.convert_to_binary(101)])


def test_convert_binary_32bit():
    assert ae.convert_binary_to_32_bit('10000011100001110111') == 538743


def test_loop_32bit():
    assert [0] == ae.algorithm_step(85, [])
    assert [37, 9, 17, 44, 22] == ae.algorithm_step(1937076837, [])


def test_convert_word_to_binary_string():
    assert ae.convert_word_to_binary_string('Aa7') == '01000001011000010110111'


def test_add_33_to_list_of_ints():
    assert ae.add_33_to_each_number_in_list([1, 2, 3]) == [34, 35, 36]
    assert ae.add_33_to_each_number_in_list([-1, -2, -3]) == [32, 31, 30]


def test_encode_function():
    assert ae.encode_function('sure') == 'F*2M7'
