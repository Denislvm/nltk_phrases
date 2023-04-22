import nltk
import json
from nltk import Tree
import itertools

text = "The charming Gothic Quarter, or Barri " \
       "Gòtic, has narrow medieval streets filled with trendy bars, clubs and Catalan restaurants"

# convert the string into a tree structure using the Tree nltk class
# tree_str = "(S (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter) (, ,) (CC or) (NNP Barri) (NNP Gòtic) (, ,)) (VP (VBZ has) (NP (JJ narrow) (JJ medieval) (NNS streets)) (VP (VBN filled) (PP (IN with) (NP (JJ trendy) (NNS bars) (, ,) (NNS clubs) (CC and) (JJ Catalan) (NNS restaurants))))))"
# root_tree = Tree.fromstring(tree_str)
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

# permutate paraphrase_elem
paraphrase_elem = paraphrase_elem[0]
# print(paraphrase_elem)
for i in itertools.permutations(paraphrase_elem):
    print(i)
# paraphrase_index = [i for i, el in enumerate(paraphrase_elem)]
# print(paraphrase_index)
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
#                     paraphrase_list = {"paraphrase": {
#                         "tree": str()
#                     }}
                    # print(paraphrased_tree)

                    # нужно чтобы вывод paraphrased_treeбыл в виде дерева (NP (NP (NNS clubs)) (, ,) (NP (JJ trendy) (NNS bars)) (CC and) (NP (JJ Catalan) (NNS restaurants)))))))
                    # print(paraphrased_tree.pformat(margin=1000000))



# with open("output2.json", "w") as f:
#     json.dump(paraphrase_list, f)
