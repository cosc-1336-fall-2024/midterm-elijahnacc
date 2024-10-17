#write functions here, don't add input('') statements here!
#changed the name of this file, and other similarly named files because the compiler got confused with the modules

def test_config():
    return True

def reverse_string(string1):

    reverse = ''
    length = len(string1) - 1

    while length >= 0:
        reverse += string1[length]
        length -= 1

    return reverse