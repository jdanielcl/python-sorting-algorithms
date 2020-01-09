class Sorting(list):

    def __selection_sort(self):
        pass

    def __recursive_selection_sort(self):
        pass

    def selection_sort(self, recursive=False, reverse=False):
        if recursive:
            return self.__recursive_selection_sort()
        return self.__selection_sort()
    
    def __bubble_sort(self):
        pass

    def __recursive_bubble_sort(self):
        pass

    def bubble_sort(self, recursive=False, reverse=False):
        if recursive:
            return self.__recursive_bubble_sort()
        return self.__bubble_sort()
    
    def __insertion_sort(self):
        pass

    def __recursive_insertion_sort(self):
        pass
    
    def insertion_sort(self, recursive=False, reverse=False):
        if recursive:
            return self.__recursive_insertion_sort()
        return self.__insertion_sort()
    
    def __merge_sort(self):
        pass
    
    def merge_sort(self, reverse=False):
        return self.__merge_sort()


if __name__ == '__main__':
    pass