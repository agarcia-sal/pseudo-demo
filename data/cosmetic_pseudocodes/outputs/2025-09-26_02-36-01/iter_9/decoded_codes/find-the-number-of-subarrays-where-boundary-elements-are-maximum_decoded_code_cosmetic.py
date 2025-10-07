class Solution:
    def numberOfSubarrays(self, tuples):
        def custom_max(sequence):
            current_max = sequence[0]
            iterator = 1
            while iterator < len(sequence):
                if sequence[iterator] > current_max:
                    current_max = sequence[iterator]
                iterator += 1
            return current_max

        class DefaultListDict:
            def __init__(self):
                self.dict_obj = {}

            def get_or_create(self, key):
                if key not in self.dict_obj:
                    self.dict_obj[key] = []
                return self.dict_obj[key]

            def items(self):
                return self.dict_obj.items()

            def values(self):
                return self.dict_obj.values()

            def __contains__(self, key):
                return key in self.dict_obj

            def __getitem__(self, key):
                return self.dict_obj[key]

            def __setitem__(self, key, value):
                self.dict_obj[key] = value

        def dictionary_with_default_list():
            return DefaultListDict()

        def list_of_values(dict_obj):
            temp_list = []
            for _, v in dict_obj.items():
                temp_list.append(v)
            return temp_list

        def subarray_extractor(arr, start_index, final_index):
            result_list = []
            pos_var = start_index
            while pos_var <= final_index:
                result_list.append(arr[pos_var])
                pos_var += 1
            return result_list

        mapping_dictionary = dictionary_with_default_list()
        enumerator_index = 0
        while enumerator_index < len(tuples):
            element_value = tuples[enumerator_index]
            mapping_dictionary.get_or_create(element_value).append(enumerator_index)
            enumerator_index += 1

        total_count = 0
        value_lists = list_of_values(mapping_dictionary)
        outer_counter = 0
        while outer_counter < len(value_lists):
            current_indices = value_lists[outer_counter]
            len_indices = len(current_indices)
            inner_i = 0
            while inner_i < len_indices:
                inner_j = inner_i
                while inner_j < len_indices:
                    start_pos = current_indices[inner_i]
                    end_pos = current_indices[inner_j]
                    temp_subarray = subarray_extractor(tuples, start_pos, end_pos)
                    max_in_subarray = custom_max(temp_subarray)
                    if max_in_subarray == tuples[start_pos]:
                        total_count += 1
                    inner_j += 1
                inner_i += 1
            outer_counter += 1

        return total_count