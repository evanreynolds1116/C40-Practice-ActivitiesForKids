# Define four Python functions named run, swing, slide, and hide_and_seek. Each function should take varying number of children's names as the argument.

def run(*kids):
    for kid in kids:
        print(f'{kid} ran like a fool')

run("Pam", "Sam", "Andrea", "Will")

def swing(*kids):
    for kid in kids:
        print(f'{kid} likes to swing')

swing("Marybeth", "Ariel", "Kevin", "Courtney")

def slide(*kids):
    for kid in kids:
        print(f'{kid} likes to slide')

slide("Mike", "Jack", "Jennifer", "Earl")

def hide(*kids):
    for kid in kids:
        print(f'{kid} is hiding')

hide("Henry", "Heather", "Hayley", "Hugh")