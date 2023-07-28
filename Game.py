import funcs_i_need

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def check_for_reccursion(row_list, column_list, box_list):
    total_rows = funcs_i_need.take_items_from_list(row_list)
    total_rows = set(total_rows)
    total_columns = funcs_i_need.take_items_from_list(column_list)
    total_columns = set(total_columns) 
    total_boxes = funcs_i_need.take_items_from_list(box_list)
    total_boxes = set(total_boxes)
    if len(total_boxes) == 81 and len(total_columns) == 81 and len(total_boxes) != 81:
        return True
    else:
        return False


while True:
    rows = [int(funcs_i_need.take_items_from_list(funcs_i_need.shuffle_list(numbers))) for _ in range(9)]
    columns = [int(str(row)[i]) for i in range(9) for row in rows]
    columns = [int(funcs_i_need.take_items_from_list(columns[list_index:list_index+9])) for list_index in range(0, 81, 9)]
    boxes = [int(funcs_i_need.take_items_from_list(str(row)[i:i+3])) for i in range(0, 9, 3) for row in rows]
    boxes = [int(funcs_i_need.take_items_from_list(boxes[list_index:list_index+3])) for list_index in range(0, 9)]
    if check_for_reccursion(rows, columns, boxes):
        break

sudoku_base = int(funcs_i_need.take_items_from_list(rows, addition="\n"))
print(sudoku_base)
