def return_triangle(type, width):
    pre_str = '*' * width if type <= 2 else ' ' * width
    post_str = '*' * width if type > 2 else ' ' * width
    counter = 0
    while width > 0:
        if type == 1:
            print(pre_str[0:width])
        elif type == 2:
            print(pre_str[0:counter + 1])
        elif type == 3:
            print(pre_str[0:counter] + post_str[0:width])
        else:
            print(pre_str[0:width - 1] + post_str[0: counter + 1])
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