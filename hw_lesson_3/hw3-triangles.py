def return_triangle(tr_type, width):
    star_str = '*' * width
    space_str = ' ' * width
    counter = 0
    while width > 0:
        if tr_type == 1:
            print(star_str[0:width])
        elif tr_type == 2:
            print(star_str[0:counter + 1])
        elif tr_type == 3:
            print(space_str[0:counter] + star_str[0:width])
        else:
            print(space_str[0:width - 1] + star_str[0: counter + 1])
        width -= 1
        counter += 1


triangle_width = int(input('Input triangle width: '))
print('1)')
return_triangle(1, triangle_width)
print('2)')
return_triangle(2, triangle_width)
print('3)')
return_triangle(3, triangle_width)
print('4)')
return_triangle(4, triangle_width)