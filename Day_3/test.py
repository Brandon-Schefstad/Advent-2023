from answer import my_function_to_run

input_text = open("input.txt", "r").readlines()
input_text_test = open("input_test.txt", "r").readlines()

rows = input_text
rows_columns = []
for row in rows:
    rows_columns.append(list(enumerate(row)))

rows_test = input_text_test
rows_columns_test = []
for row_test in rows_test:
    rows_columns_test.append(list(row_test))

input = rows_columns

# expected = [['854','362','271','732','838','24']]
# assert my_function_to_run(input) == expected


# expected = [['854','362','271','732','838','24'],['854','362','271','732','838','24'],['854','362','271','732','838','24']]
# assert my_function_to_run(input_text_test) == expected
def test_capture_numbers_asterisks():
    expected = 553815
    assert my_function_to_run(input_text_test) == expected
