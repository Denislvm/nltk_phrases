import itertools

from fastapi import FastAPI
from nltk import CFG, parse, ne_chunk
import nltk

app = FastAPI()


@app.get('/paraphrase')
def get_paraphrase(tree: str, limit: int = 5):
    text = "The charming Gothic Quarter, or Barri " \
           "Gòtic, has narrow medieval streets filled with trendy bars, clubs and Catalan restaurants"

    tag_pattern = r"NP: {((<DT>?<JJ>*<NN.*>+<IN>)?<DT>?<JJ>*<NN.*>+)}"
    sent_tokens = nltk.word_tokenize(text)
    text_tag = nltk.pos_tag(sent_tokens)
    # text_chunk = ne_chunk(text_tag)
    chunk_parser = nltk.RegexpParser(tag_pattern)
    chunk_result = chunk_parser.parse(text_tag)
    print(chunk_result)

    for subtree in chunk_result.subtrees():
        if subtree.label() == "NP":
            words = [word for word, tag in subtree.leaves()] #leaves - убирает labels у subtree
            permutations = itertools.permutations(words)
            permutations = list(permutations)[:limit]
            print(f"Original NP: {'.'.join(words)}")
            for permutation in permutations:
                print(f"Permutation: {''.join(permutation)}")

