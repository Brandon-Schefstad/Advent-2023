import re
def my_function_to_run(input):
    part_numbers = []
    number_list = []
    for row in input:
        number_list.append(get_number_list(row))
   
    for index, row in enumerate(number_list):
        start_index = 0
        for number in row:
          if is_part_number(number, index, input, start_index):
            part_numbers.append(int(number))
          new_start_index = input[index].find(number,start_index) + len(number)
          start_index = new_start_index
    #is_gear   
    print(part_numbers)
    return sum(part_numbers)

def is_part_number(number, index, input, start_index):
  row_from_above = ""
  row_from_below = ""
  row_from_input = input[index]
  first_digit_index = row_from_input.find(number, start_index)
  span_of_number = first_digit_index + len(number)

  left_border = first_digit_index == 0
  top_border = index == 0

  right_border = span_of_number == len(row_from_input) -1
  down_border = index == len(input) - 1
  if not top_border:
      row_from_above = input[index - 1]
  if not down_border:
      row_from_below = input[index + 1]

  one_step_behind = row_from_input[first_digit_index - 1]
  one_step_above = row_from_above[first_digit_index:span_of_number]
  one_step_forward = row_from_input[span_of_number]
  one_step_below = row_from_below[first_digit_index:span_of_number]
  
  # print(number, left_border, top_border, right_border, down_border )
  top_left_diagonal = (
      row_from_above[first_digit_index - 1]
      if not left_border and not top_border
      else "."
  )
  top_right_diagonal = (
      row_from_above[span_of_number]
      if not right_border and not top_border
      else "."
  )
  bottom_right_diagonal = (
      row_from_below[span_of_number]
      if not right_border and not down_border
      else "."
  )
  bottom_left_diagonal = (
      row_from_below[first_digit_index - 1]
      if not left_border and not down_border
      else "."
  )

  search_string = "".join(
      [
          one_step_behind,
          top_left_diagonal,
          one_step_above,
          top_right_diagonal,
          one_step_forward,
          bottom_right_diagonal,
          one_step_below,
          bottom_left_diagonal,
      ]
  )
  # approved_chars= ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", '\n', '']
  # part_number = False
  # for char in search_string:
  #     if char in approved_chars:
  #         pass
  #     else:
  #         part_number = True
          
  #         break
  # return part_number
  print(search_string)
  return "*" in search_string


def get_number_list(row):
    return_nums = []
    integers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    num_string = ""
    for index, char in enumerate(row):
        if char in integers:
            num_string += char
        elif char not in integers and len(num_string):
            return_nums.append(num_string)
            num_string = ""
        elif index == len(row)-1 and char != '\n':
            return_nums.append([])
        else:
            pass
    return return_nums
