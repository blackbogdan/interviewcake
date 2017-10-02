__author__ = 'bkapusta'
Sort an array from lowest to highest without moving the -1

l =[-1, 4, 10, 3, -1, -1, 9]
#pre conditions:


#size of the list?


# ++++



def sort_list(lst):
  if len(lst) <2:
    return lst
  positions = []
  new_list = []
  for pos, item in enumerate(lst):
    if type(item) not in [float, int]:
      raise TypeError("Please make sure that all items in the list are intigers or floating point numbers. \
         Current element:{}. Element's position: {}".format(item, pos))
    if item == -1:
    #0
    #4
      positions.append(pos)
    else:
      new_list.append(item)
  new_list.sort()
  #[3, 4, 9, 10]
  for item in positions:
    new_list.insert(item, -1)
    #[0, 3, 4, 9, 10]
    # second [-1, 3, 4, 9, -1, 10]
    # third [-1, 3, 4, 9, -1, -1, 10]
  return new_list