__author__ = 'John'

def reverse_string(string_in):
    return string_in[::-1]

#in place...
def reverse_words_in_place(string_in):

    string_in = reverse_string(string_in)

    i = 0
    while i < len(string_in):
        if string_in[i] != ' ':
            j = i
            while j < len(string_in):
                if string_in[j] == ' ':
                    break
                j = j + 1
            string_in = string_in[0:i] + string_in[i:j][::-1] + string_in[j:]
            i = j
        i = i + 1

    return string_in


#in place...
def reverse_words(string_in):
    str_list = string_in.split(" ")
    str_list = reversed(str_list)
    string_in = " ".join(str_list)
    return string_in



#in place...
def strip_whitespace(string_in):
    i = 0
    j = 0

    while i < len(string_in):
        if string_in[i] != ' ':
            string_in = string_in[0:j] + string_in[i:i+1] + string_in[i+1:]
            j += 1
            i = j
        else:
            i = i + 1

    return string_in

vowels = 'AEIOUaeiou'

#in place...
def vowels_at_end(string_in):
    i = 0
    j = 0

    while i < len(string_in):
        if not string_in[i] in vowels:
            l1 = string_in[i]
            string_in = string_in[0:j] + string_in[i] + string_in[i+1:]
            j += 1
            string_in = string_in[0:j] + l1 + string_in[j+1:]
            print(string_in)
            j += 1
        i = i + 1

    return string_in


str = reverse_words_in_place(" Hi I am a cow  ")


str = reverse_words(" Hi I am a cow  ")


str = strip_whitespace("Hi I am a cow  ")


str = vowels_at_end("Hi I am a cow  ")
print(str)