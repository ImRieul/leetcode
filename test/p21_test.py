import unittest
from problem.p21_merge_two_sorted_lists import Solution, ListNode


def create_list_node(data_list):
    if not data_list:
        return None

    head = ListNode(data_list[0])
    curr = head
    for i in range(1, len(data_list)):
        curr.next = ListNode(data_list[i])
        curr = curr.next

    return head


def compare_list_node(list1, list2):
    while list1 and list2:
        if list1.val != list2.val:
            return False
        list1 = list1.next
        list2 = list2.next

    return list1 is None and list2 is None


class MyTestCase(unittest.TestCase):
    def test_example1(self):
        data_list1 = create_list_node([1, 2, 4])
        data_list2 = create_list_node([1, 3, 4])

        input_data = {
            'list1': data_list1,
            'list2': data_list2
        }

        output_data = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))

        self.assertTrue(compare_list_node(output_data, Solution().mergeTwoLists(**input_data)))

    def test_example2(self):
        data_list1 = create_list_node([])
        data_list2 = create_list_node([])

        input_data = {
            'list1': data_list1,
            'list2': data_list2
        }

        output_data = None

        self.assertTrue(compare_list_node(output_data, Solution().mergeTwoLists(**input_data)))

    def test_example3(self):
        data_list1 = create_list_node([])
        data_list2 = create_list_node([0])

        input_data = {
            'list1': data_list1,
            'list2': data_list2
        }

        output_data = ListNode(0)

        self.assertTrue(compare_list_node(output_data, Solution().mergeTwoLists(**input_data)))


if __name__ == '__main__':
    unittest.main()
