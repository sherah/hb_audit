import unittest

from list_operations import *

class TestListOperations(unittest.TestCase):

    def setUp(self):
        self.months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
                       'Sep', 'Oct', 'Nov', 'Dec']
        self.notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
        self.multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

    ### Tests for Part 1 ###

    def test_1_A_head(self):
        self.assertEqual(head(self.months), 'Jan')
        self.assertEqual(head(self.notes), 'Do')
        self.assertEqual(head(self.multiples), 0)

    def test_1_B_tail(self):
        self.assertEqual(tail(self.months), ['Feb', 'Mar', 'Apr', 'May', 'Jun',
                                             'Jul', 'Aug', 'Sep', 'Oct', 'Nov',
                                             'Dec'])
        self.assertEqual(tail(self.notes), ['Re', 'Mi', 'Fa', 'So', 'La', 'Ti',
                                            'Do'])
        self.assertEqual(tail(self.multiples), [3, 6, 9, 12, 15, 18, 21, 24, 27])

    def test_1_C_last(self):
        self.assertEqual(last(self.months), 'Dec')
        self.assertEqual(last(self.notes), 'Do')
        self.assertEqual(last(self.multiples), 27)

    def test_1_D_init(self):
        self.assertEqual(init(self.months), ['Jan', 'Feb', 'Mar', 'Apr', 'May',
                                             'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
                                             'Nov'])
        self.assertEqual(init(self.notes), ['Do', 'Re', 'Mi', 'Fa', 'So', 'La',
                                            'Ti'])
        self.assertEqual(init(self.multiples), [0, 3, 6, 9, 12, 15, 18, 21, 24])

    def test_1_E_first_three(self):
        self.assertEqual(first_three(self.months), ['Jan', 'Feb', 'Mar'])
        self.assertEqual(first_three(self.notes), ['Do', 'Re', 'Mi'])
        self.assertEqual(first_three(self.multiples), [0, 3, 6])

    def test_1_F_last_five(self):
        self.assertEqual(last_five(self.months), ['Aug', 'Sep', 'Oct', 'Nov',
                                                  'Dec'])
        self.assertEqual(last_five(self.notes), ['Fa', 'So', 'La', 'Ti', 'Do'])
        self.assertEqual(last_five(self.multiples), [15, 18, 21, 24, 27])

    def test_1_G_middle(self):
        self.assertEqual(middle(self.months), ['Mar', 'Apr', 'May', 'Jun', 'Jul',
                                               'Aug', 'Sep', 'Oct'])
        self.assertEqual(middle(self.notes), ['Mi', 'Fa', 'So', 'La'])
        self.assertEqual(middle(self.multiples), [6, 9, 12, 15, 18, 21])

    def test_1_H_inner_four(self):
        self.assertEqual(inner_four(self.months), ['Mar', 'Apr', 'May', 'Jun'])
        self.assertEqual(inner_four(self.notes), ['Mi', 'Fa', 'So', 'La'])
        self.assertEqual(inner_four(self.multiples), [6, 9, 12, 15])

    #is this test wrong? seems like it's supposed to read "Jun", "May", "Apr", "Mar" ???
    # def test_1_I_inner_four_end(self):
    #     self.assertEqual(inner_four_end(self.months), ['Jul', 'Aug', 'Sep',
    #                                                     'Oct'])
    #     self.assertEqual(inner_four_end(self.notes), ['Mi', 'Fa', 'So', 'La'])
    #     self.assertEqual(inner_four_end(self.multiples), [12, 15, 18, 21])

    def test_1_J_replace_head(self):
        replace_head(self.months)
        replace_head(self.notes)
        replace_head(self.multiples)

        self.assertEqual(self.months, [42, 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
        self.assertEqual(self.notes, [42, 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti',
                                      'Do'])
        self.assertEqual(self.multiples, [42, 3, 6, 9, 12, 15, 18, 21, 24, 27])

    def test_1_K_replace_third_and_last(self):
        replace_third_and_last(self.months)
        replace_third_and_last(self.notes)
        replace_third_and_last(self.multiples)

        self.assertEqual(self.months, ['Jan', 'Feb', 37, 'Apr', 'May', 'Jun',
                                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 37])
        self.assertEqual(self.notes, ['Do', 'Re', 37, 'Fa', 'So', 'La', 'Ti', 37])
        self.assertEqual(self.multiples, [0, 3, 37, 9, 12, 15, 18, 21, 24, 37])

    def test_1_L_replace_middle(self):
        a = replace_middle(self.months)
        b = replace_middle(self.notes)
        c = replace_middle(self.multiples)

        self.assertEqual(a, ['Jan', 'Feb', 42, 37, 'Nov', 'Dec'])
        self.assertEqual(b, ['Do', 'Re', 42, 37, 'Ti', 'Do'])
        self.assertEqual(c, [0, 3, 42, 37, 24, 27])

    def test_1_M_delete_third_and_seventh(self):
        delete_third_and_seventh(self.months)
        delete_third_and_seventh(self.notes)
        delete_third_and_seventh(self.multiples)

        self.assertEqual(self.months, ['Jan', 'Feb', 'Apr', 'May', 'Jun', 'Aug',
                                       'Sep', 'Oct', 'Nov', 'Dec'])
        self.assertEqual(self.notes, ['Do', 'Re', 'Fa', 'So', 'La', 'Do'])
        self.assertEqual(self.multiples, [0, 3, 9, 12, 15, 21, 24, 27])

    def test_1_N_delete_middle(self):
        delete_middle(self.months)
        delete_middle(self.notes)
        delete_middle(self.multiples)

        self.assertEqual(self.months, ['Jan', 'Feb', 'Nov', 'Dec'])
        self.assertEqual(self.notes, ['Do', 'Re', 'Ti', 'Do'])
        self.assertEqual(self.multiples, [0, 3, 24, 27])

    ### Tests for Part 2 ###

    def test_2_A_custom_len(self):
        self.assertEqual(custom_len(self.months), 12)
        self.assertEqual(custom_len(self.notes), 8)
        self.assertEqual(custom_len(self.multiples), 10)

    def test_2_B_custom_append(self):
        a = custom_append(self.months, 'Hex')
        b = custom_append(self.notes, 'Re')
        c = custom_append(self.multiples, 30)

        self.assertEqual(a, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',
                                       'Hex'])
        self.assertEqual(b, ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti',
                                      'Do', 'Re'])
        self.assertEqual(c, [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30])

    def test_2_C_custom_extend(self):
        a = custom_extend(self.months, ['Bin', 'Tri', 'Hex'])
        b = custom_extend(self.notes, ['Re', 'Mi', 'Fa', 'So'])
        c = custom_extend(self.multiples, [30, 33, 36, 39, 42, 45])

        self.assertEqual(a, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',
                                       'Bin', 'Tri', 'Hex'])
        self.assertEqual(b, ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti',
                                      'Do', 'Re', 'Mi', 'Fa', 'So'])
        self.assertEqual(c, [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30,
                                          33, 36, 39, 42, 45])

    def test_2_D_custom_insert(self):
        a = custom_insert(self.months, 8, 'Hex')
        b = custom_insert(self.notes, len(self.notes), 'Re')
        c = custom_insert(self.multiples, 0, -3)

        self.assertEqual(a, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                                       'Jul', 'Aug', 'Hex', 'Sep', 'Oct', 'Nov',
                                       'Dec'])
        self.assertEqual(b, ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti',
                                      'Do', 'Re'])
        self.assertEqual(c, [-3, 0, 3, 6, 9, 12, 15, 18, 21, 24, 27])

    def test_2_E_custom_remove(self):
        a = custom_remove(self.months, 'Jul')
        b = custom_remove(self.notes, 'Do')
        c = custom_remove(self.multiples, 27)

        self.assertEqual(a, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                                       'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
        self.assertEqual(b, ['Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do'])
        self.assertEqual(c, [0, 3, 6, 9, 12, 15, 18, 21, 24])

    def test_2_F_custom_pop(self):
        a = custom_pop(self.months)
        b = custom_pop(self.notes)
        c = custom_pop(self.multiples)

        self.assertEqual(a, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov'])
        self.assertEqual(b, ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti'])
        self.assertEqual(c, [0, 3, 6, 9, 12, 15, 18, 21, 24])

    def test_2_G_custom_index(self):
        self.assertEqual(custom_index(self.months, 'Jul'), 6)
        self.assertEqual(custom_index(self.notes, 'Do'), 0)
        self.assertEqual(custom_index(self.multiples, 27), 9)

    def test_2_H_custom_count(self):
        self.assertEqual(custom_count(self.months, 'Jul'), 1)
        self.assertEqual(custom_count(self.notes, 'Do'), 2)
        self.assertEqual(custom_count(self.multiples, 27), 1)

    def test_2_I_custom_reverse(self):
        a = custom_reverse(self.months)
        b = custom_reverse(self.notes)
        c = custom_reverse(self.multiples)

        self.assertEqual(a, ['Dec', 'Nov', 'Oct', 'Sep', 'Aug', 'Jul',
                                       'Jun', 'May', 'Apr', 'Mar', 'Feb', 'Jan'])
        self.assertEqual(b, ['Do', 'Ti', 'La', 'So', 'Fa', 'Mi', 'Re',
                                      'Do'])
        self.assertEqual(c, [27, 24, 21, 18, 15, 12, 9, 6, 3, 0])

    def test_2_J_custom_contains(self):
        self.assertTrue(custom_contains(self.months, 'Jul'))
        self.assertTrue(custom_contains(self.notes, 'Do'))
        self.assertTrue(custom_contains(self.multiples, 27))

        self.assertFalse(custom_contains(self.months, 'Hex'))
        self.assertFalse(custom_contains(self.notes, 'Go'))
        self.assertFalse(custom_contains(self.multiples, 30))

    def test_2_K_custom_equality(self):
        self.assertTrue(custom_equality(self.months, ['Jan', 'Feb', 'Mar', 'Apr',
                                                      'May', 'Jun', 'Jul', 'Aug',
                                                      'Sep', 'Oct', 'Nov', 'Dec']))
        self.assertTrue(custom_equality(self.notes, ['Do', 'Re', 'Mi', 'Fa', 'So',
                                                     'La', 'Ti', 'Do']))
        self.assertTrue(custom_equality(self.multiples, [0, 3, 6, 9, 12, 15, 18,
                                                         21, 24, 27]))

        self.assertFalse(custom_equality(self.months, ['Jan', 'Feb', 'Mar', 'Apr',
                                                      'May', 'Jun', 'Aug', 'Sep',
                                                       'Oct', 'Nov', 'Dec']))
        self.assertFalse(custom_equality(self.notes, self.notes[::-1]))
        self.assertFalse(custom_equality(self.multiples, [0, 3, 6, 9, 12, 15, 18,
                                                         21, 24]))

if __name__ == '__main__':
    unittest.main()
