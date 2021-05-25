import typing
import wikipedia
import re


def run():
    print("Thinking...")
    wikipedia.set_lang("en")

    for _ in range(10):
        # get the title from wikipedia
        title = wikipedia.random(pages=1)

        try:
            # get a summary from the title
            content = wikipedia.page(title).summary
        except wikipedia.exceptions.PageError:
            print(
                "INF: Page id {title} does not match any pages. Try another id.")
            continue
        else:
            break

    # delete contents in brackets
    re_del = re.compile(r"\(.*?\)")
    re_del_spaces = re.compile(r" {2}")
    content_without_brackets = re_del.sub("", content)

    # sentence split
    sentences = re_del_spaces.sub(
        " ", content_without_brackets).strip("\n").split(".")
    # remove blank index
    sentences = [sentence for sentence in sentences if not sentence == ""]
    # add a dot at the end of sentences
    sentences = [sentence+"." for sentence in sentences]
    # print("DEBUG INF:sentences:", sentences)

    ########### typing ###########
    print(f'TITLE: "{title}"')
    print()
    print(sentences[0])

    print()
    print("LET'S TYPE! >>")
    type_sentence = input()  # your answer

    # If your answer matches with the question.
    if sentences[0] == type_sentence:
        print()
        print("GRATE!")
    else:
        print()
        print("Ops! Wrong answer:_(")


if __name__ == "__main__":
    while True:
        run()
        print()
        while True:
            print("Continue?[y/n]")
            check = input(">>")
            if check in ["yes", "y"]:
                break
            elif check in ["no", "n"]:
                print("BYE!")
                exit()
