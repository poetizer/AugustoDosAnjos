from textgenrnn import textgenrnn
import jamspell

weigths = 'augusto-dos-anjos.hdf5'

textgen = textgenrnn(weigths)

# Descomente para treinar um novo modelo, ou melhorar.
#
# textgen.train_from_file('Eu/eu - augusto dos anjos.txt', num_epochs=100)
# textgen.save(weigths)


def gen(temp):
    return list(map(str.strip, textgen.generate(n=14, temperature=temp, return_as_list=True)))


corrector = jamspell.TSpellCorrector()
corrector.LoadLangModel(
    'drummond-dos-anjos.bin')

gen = gen(1.0)
poema = []

for verso in gen:
    novo_verso = corrector.FixFragment(verso)

    poema.append(novo_verso)

print('\n'.join(poema))
