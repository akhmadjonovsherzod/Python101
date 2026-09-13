from typing import List

def check(row_start:int, row_end:int, column_start:int, column_end:int) -> List[List[int]]:
    new_table = []

    for row_i in range(row_start, row_end + 1):
        current_row = []

        for col_i in range(column_start, column_end + 1):
            result = row_i * col_i
            current_row.append(result)
        new_table.append(current_row)
    return new_table
