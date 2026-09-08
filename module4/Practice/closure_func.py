def format_message(format_string):
    frmt_string = format_string

    def inner_function(message):
        print(frmt_string.format(message))

    return inner_function  #this is closure function - you return it inside the outer function

