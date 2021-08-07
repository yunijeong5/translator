from translate import Translator
import sys

# with open(sys.argv[1]) as original:
#     for line in original:
#         text += original.readline()

try:
    with open(sys.argv[1]) as original:
        text = original.read()
        translator = Translator(to_lang='ko')
        with open('./test-ko.txt', mode='w') as translation:
            translation.write(translator.translate(text))
except FileNotFoundError as err:
    print(f'Check your file directory: {err}')

