import args

# def compile_hex():
#     output_string = ''
#     for i in args.getArgsFirst():
#         output_string += hex(ord(i))
#     print(output_string)
#     return output_string

def compile_hex(text):
    output_string = ''
    for i in text:
        output_string += hex(ord(i))
    print(output_string)
    return output_string


if __name__ == '__main__':
    main()
