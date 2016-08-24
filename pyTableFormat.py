class TableFormat:
    """
    Class helper for building tableformat outputs.
    """

    def __init__(self, l_attributes, l_values, dict_extend_values=None, l_ignore_attrs=None):
        self.dict_extend_values = dict_extend_values
        self.ignore_attrs = l_ignore_attrs
        (self.attributes, self.values_raw) = self.cull_ignored(l_attributes, l_values)
        self.attributes_lengths = []
        self.values_trunc = []
        self.fmt_shell = '{{{0}:{1}}}'
        self.fmt = self.gen_fmt()
        self.truncate_values()
        self.string_values = self.gen_string()
        self.string_header = self.gen_header()

    def cull_ignored(self, attributes, values):
        scope = len(attributes)
        topop = []
        for i in range(0, scope):
            w_attr = attributes[i]
            if w_attr in self.ignore_attrs:
                topop.append(i)
        new_attr = []
        new_values = []
        for i in range(0, scope):
            if i not in topop:
                new_attr.append(attributes[i])
                new_values.append(values[i])
        return new_attr, new_values

    def gen_fmt(self):
        """
        Generates the format string (e.g., {0:4}{1:15})
        based on the length of the attribute names
        :return: fmt_string
        """
        fmt_string = ''
        for attr in self.attributes:
            self.attributes_lengths.append(len(attr))
        width = len(self.attributes)
        for i in range(0, width):
            try:
                field_length = self.dict_extend_values[self.attributes[i]]
            except:
                field_length = self.attributes_lengths[i] + 2
            fmt_string += self.fmt_shell.format(str(i), str(field_length))
        return fmt_string

    def truncate_values(self):
        """
        Truncates the values a little smaller than the column widths
        :return:
        """
        scope = len(self.attributes)
        for i in range(0, scope):
            try:
                width = self.dict_extend_values[self.attributes[i]]
            except:
                width = self.attributes_lengths[i]
            value_raw = str(self.values_raw[i])
            value_trunc = value_raw[:width]
            self.values_trunc.append(value_trunc)

    def gen_string(self):
        """
        Generates the string of formatted values.
        :return: format_string
        """
        format_string = self.fmt.format(*self.values_trunc) + '\n'
        return format_string

    def gen_header(self):
        """
        Generates the header using the attribute names formatted by column
        :return: header
        """
        header = self.fmt.format(*self.attributes) + '\n'
        return header

class Table_Formattable_Object():
    dump_ignore_attrs = [] #  add strings here of property objs to ignore in dump
    dict_extend_values = {} # add dict strings here of property objs to expand width
    # e.g., {'name': 50, 'age': 5, 'gender': 2}
    def dumpself_tableformat_header(self):
        msg = ''
        attributes = []
        values = []
        for attr in dir(self):
            if (
                    '__' not in attr and
                    'instancemethod' not in str(type(getattr(self, attr))) and
                    'dict' not in str(type(getattr(self, attr))) and
                    'dump_ignore_attrs' not in attr):
                attributes.append(attr)
                values.append(str(getattr(self, attr)))
        format_helper = TableFormat(attributes, values, self.dict_extend_values, self.dump_ignore_attrs)
        msg += format_helper.string_header
        return msg

    def dumpself_tableformat(self):
        msg = ''
        attributes = []
        values = []
        for attr in dir(self):
            if (
                    '__' not in attr and
                    'instancemethod' not in str(type(getattr(self, attr))) and
                    'dict' not in str(type(getattr(self, attr))) and
                    'dump_ignore_attrs' not in attr):
                attributes.append(attr)
                values.append(str(getattr(self, attr)))
        format_helper = TableFormat(attributes, values, self.dict_extend_values, self.dump_ignore_attrs)
        msg += format_helper.string_values
        return msg
    def dumpself_csv_header(self):
        msg = ''
        attributes = []
        values = []
        for attr in dir(self):
            if (
                    '__' not in attr and
                    'instancemethod' not in str(type(getattr(self, attr))) and
                    'dict' not in str(type(getattr(self, attr))) and
                    'dump_ignore_attrs' not in attr):
                attributes.append(attr)
                values.append(str(getattr(self, attr)))
                if attr != 'whois_result':
                    msg += attr + ','
        msg += '\n'
        return msg
    def dumpself_csv(self):
        msg = ''
        attributes = []
        values = []
        for attr in dir(self):
            if (
                    '__' not in attr and
                    'instancemethod' not in str(type(getattr(self, attr))) and
                    'dict' not in str(type(getattr(self, attr))) and
                    'dump_ignore_attrs' not in attr):
                attributes.append(attr)
                values.append(str(getattr(self, attr)))
                if attr != 'whois_result':
                    msg += '"' + str(getattr(self, attr)) + '"' + ','
        msg += '\n'
        return msg