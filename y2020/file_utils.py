def get_input_data_as_int(file_name):
    with open(file_name) as f:
        content = [int(line.rstrip('\n')) for line in f]

    return content


def get_input_line_as_int(file_name):
    with open(file_name) as f:
        line = f.read()
        content = [int(int_val) for int_val in line]

    return content


def get_input_line(file_name):
    with open(file_name) as f:
        line = f.read()
        return line


def get_csv_input_data_as_int(file_name):
    with open(file_name) as f:
        for line in f:
            content = [int(no) for no in line.split(',')]

    return content


def get_input_data(file_name):
    with open(file_name) as f:
        content = [line.rstrip('\n') for line in f]

    return content


def get_input_data_newline_separated(file_name):
    content = []
    with open(file_name) as f:
        current_info = []
        for line in f:
            if line == '\n':
                content.append(current_info)
                current_info = []
                continue

            current_info.append(line.rstrip('\n'))

        content.append(current_info)

    # print(content)
    return content
