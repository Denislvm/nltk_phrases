import itertools
from typing import Optional
from fastapi import FastAPI
from nltk import Tree
import json

app = FastAPI()

text = "The charming Gothic Quarter, or Barri " \
       "Gòtic, has narrow medieval streets filled with trendy bars, clubs and Catalan restaurants"

tree = Tree('S', [
    Tree('NP', [
        Tree('NP', [
            Tree('DT', ['The']),
            Tree('JJ', ['charming']),
            Tree('NNP', ['Gothic']),
            Tree('NNP', ['Quarter']),
        ]),
            Tree(',', [',']),
            Tree('CC', ['or']),
        Tree('NP', [
            Tree('NNP', ['Barri']),
            Tree('NNP', ['Gòtic']),
        ]),]),
        Tree(',', [',']),

    Tree('VP', [
        Tree('VBZ', ['has']),
        Tree('NP', [
           Tree('NP', [
            Tree('JJ', ['narrow']),
            Tree('JJ', ['medieval']),
            Tree('NNS', ['streets']),
                ]),
        Tree('VP', [
            Tree('VBN', ['filled']),
        Tree('PP', [
            Tree('IN', ['with']),
            Tree('NP', [
            Tree('NP', [
                Tree('JJ', ['trendy']),
                Tree('NNS', ['bars']),
            ]),
                Tree(',', [',']),
                Tree('NP', [
                    Tree('NNS', ['clubs']),
                ]),

                Tree('CC', ['and']),
                Tree('NP', [
                Tree('JJ', ['Catalan']),
                Tree('NNS', ['restaurants']),
            ]),
        ]),
        ]),
        ]),
    ]),
]),
])

paraphrase_elem = [i for i in tree.subtrees(lambda t: t.label() == 'NP' and len(t) > 4 and (',')
                                                      in t.leaves() or 'CC' in t.leaves())]
paraphrase_elem = paraphrase_elem[0]


@app.get('/paraphrase')
def get_paraphrase(tree: str, Limit: Optional[int] = 20):

    with open("output.json", "w") as f:
        for i in range(Limit):
            for i in itertools.islice(itertools.permutations(paraphrase_elem), Limit):
                trees = Tree('S', [
                    Tree('NP', [
                        Tree('NP', [
                            Tree('DT', ['The']),
                            Tree('JJ', ['charming']),
                            Tree('NNP', ['Gothic']),
                            Tree('NNP', ['Quarter']),
                        ]),
                        Tree(',', [',']),
                        Tree('CC', ['or']),
                        Tree('NP', [
                            Tree('NNP', ['Barri']),
                            Tree('NNP', ['Gòtic']),
                        ]), ]),
                    Tree(',', [',']),

                    Tree('VP', [
                        Tree('VBZ', ['has']),
                        Tree('NP', [
                            Tree('NP', [
                                Tree('JJ', ['narrow']),
                                Tree('JJ', ['medieval']),
                                Tree('NNS', ['streets']),
                            ]),
                            Tree('VP', [
                                Tree('VBN', ['filled']),
                                Tree('PP', [
                                    Tree('IN', ['with']),
                                    Tree('', i)]), ]), ]), ]), ])

                paraphrase_list = {"paraphrase": {"tree": str(trees).replace("\n", " ")}}
                json.dump(paraphrase_list, f)
                f.write("\n")
            return paraphrase_list

# for subtree in tree.subtrees():
#     if subtree.label() == 'NP' and len(subtree) > 4:
#         if ',' in subtree.leaves() or 'CC' in subtree.leaves():
#             paraphrase_el = subtree.leaves()
#
#             paraphrasable_indexes = [i for i, el in enumerate(paraphrase_el)]
#             # print(paraphrasable_indexes)
#             for i in range(len(paraphrase_el)):
#                 for j in range(i + 1, len(paraphrase_el)):
#                     paraphrase_el[i], paraphrase_el[j] = paraphrase_el[j], paraphrase_el[i]
#                     new_subtree = Tree(subtree.label(), paraphrase_el)
#                     # print(paraphrasable_elements)
#                     # for orig_idx, new_idx in zip(paraphrasable_indexes, paraphrasable_elements):
#                     #     paraphrasable_elements[orig_idx] = new_idx
#
#                     paraphrased_tree = Tree("NP", new_subtree)
                    # print(paraphrased_tree)