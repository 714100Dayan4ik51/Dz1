from num2words import num2words

def number_to_words(num):
    words = num2words(num, lang='ru')
    ending = num % 10
    if ending == 1 and num % 100 != 11:
        end = " рубль"
    elif 1 < ending < 5 and (num % 100 < 10 or num % 100 > 21):
        end = " рубля"
    else:
        end = " рублей"
    result = words.capitalize() + end
    return result


def main():
    while True:
        try:
            num = int(input("Введите сумму денег от 1 до 100 000 - "))
            print(number_to_words(num))
            break
        except ValueError:
            print("Вы должны ввести число от 1 до 100 000, поробуйте снова. ")
main()
