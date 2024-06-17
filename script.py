# do various stuff here
from datasets import load_dataset

# I choose this because its simple & all stories are small & different, good to test for context based retrieval
dataset = load_dataset("mintujupally/ROCStories")['train']
# print(dataset[0])

story = ""
for each_story in dataset['text']:
    story += each_story + "\n"

with open("rocstories.txt", "w") as f:
    f.write(story)
