
def golf_score_input():
    golf_score = open('golf.txt','a')
    nextline = 'y'
    while nextline == 'y' or nextline == 'Y':
        label = input('Point player:')
        quantity = float(input('Put the quantity of points:'))
        golf_score.write(label + '\n')
        golf_score.write(str(quantity) + '\n')
        nextline = input('Continue? "y" - yes, rest means "no"')
    golf_score.close()

def golf_score_show():
    golf_score = open('golf.txt', 'r')
    description = golf_score.readline()
    while description != '':
        quant = float(golf_score.readline())
        description = description.rstrip('\n')
        print('Player:', description)
        print('Points quantity:', quant)
        description = golf_score.readline()
    golf_score.close()

if __name__ == '__main__':
    #golf_score_input()
    golf_score_show()