from django import template


register = template.Library()


@register.filter()
def separate_by_line(long_sentence: str) -> str:
    sentences = long_sentence.split("\n")
    all_sents = ""
    for sentence in sentences:
        all_sents = """<p>""" + sentence + """<\\p>"""
    return all_sents


@register.filter()
def remove_tires(line: str) -> str:
    return line.replace("----", """<br>""")

