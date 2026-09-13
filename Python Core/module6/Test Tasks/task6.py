class Pagination:
    def __init__(self, data, items_on_page):
        self.data = data
        self.items_on_page = items_on_page
        self.each_page = [self.data[i:i + self.items_on_page] for i in range(0, len(self.data), self.items_on_page)]

    @property
    def item_count(self):
        return len(self.data)

    @property
    def page_count(self):
        length_d = len(self.each_page)

        return length_d

    def count_items_on_page(self, page_number):
        if self.page_count <= page_number:
            raise Exception("Invalid index. Page is missing.")
        length_of_item = len(self.each_page[page_number])

        return length_of_item

    def find_page(self, data):
        if data not in self.data:
            raise Exception(f"'{data}' is missing on the pages")

        my_lst = []
        start = 0
        while True:
            idx = self.data.find(data, start)
            if idx == -1:
                break
            start += 1
            start_page = idx // self.items_on_page
            end_page = (idx + len(data) - 1) // self.items_on_page

            if start_page == end_page:
                my_lst.append(start_page)
            else:
                my_lst.append(start_page)
                my_lst.append(end_page)
        my_lst = sorted(list(set(my_lst)))
        return my_lst

    def display_page(self, page_number):
        if self.page_count <= page_number:
            raise Exception("Invalid index. Page is missing.")
        return self.each_page[page_number]


