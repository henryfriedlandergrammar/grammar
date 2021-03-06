import random
from verbFunctions import *
from NounFunctions import *
from POSObjects import *

# no modifiers on gerunds
# singular pural for determiners

# def displaySentence():
#     sentence=getSentence()
#     strSent=getStrSent(sentence)
#     print strSent
#     for i in xrange(len(sentence)):
#         word=sentence[i]
#         print 'Questions about the ith word.'
#         qs=word.getQA().keys()
#         ans=word.getQA().values()
#         print qs
#         for i in xrange(len(qs)):
#             question=qs[i]
#             inp=input(question)
#             if inp==ans[i]:
#                 print 'CORRECT'
#             else:
#                 print 'INCORRET'
#                 print 'CORRECT ANSWER '+ans[i]
        
        
#     print sentence

def getStrSent(sentence):
    w=sentence[0]
    word=w.getWord()
    w.setWord(word[0].upper()+word[1:])
    strSent=''
                 
    for word in sentence:
        if type(word)==str and word==",":
            strSent=strSent[:-1]+word+' '
        elif type(word) == str:
            strSent=strSent + word + ' '
        else: 
            w=word.getWord()
            strSent=strSent + w + ' '

    if strSent[-1] == ",":
        strSent = strSent[:-1]
    strSent = strSent[:-1] + '.'
    return strSent
    

    
def getSentence():
    init()
    # if freq.doFreq and not prob(4):
    #     getBase(index=1)
    # elif freq.ioFreq and not prob(4):
    #     getBase(index=2)
    
    return addDescriptors(getBase())

def getBase(index=-1):
    # sing = randBool()
    # subject = getRandSubject(sing=sing)
    # actionVerb = getRandActVerb(sing=sing)
    # do = getRandDO()
    # pa = getRandAdjective()
    
    # bases = [
    #     [subject,actionVerb],
    #     [subject,actionVerb,do],
    #     ]
    
    # if index!=-1 and not prob(4):
    #     index = random.randint(0,len(bases)-1)
    #     if index==1:
    #         makeRels1(bases[index])
    #     if index == 2:
    #         makeRels1(bases[index][:2])
    #         makeRels2(bases[index])
    #     if index == 3:
    #         makeRels1(bases[index][:2])
    #         makeRels3(bases[index])
    # #there are no words in base just line numbers of the file
    # #print bases[index]
    # print "HERE: ", bases[index]
    # return bases[index]

    types = ["simple", "compound", "complex"]

    current_type = random.choice(types)

    if current_type == "simple":
        return ["independent"]

    elif current_type == "compound":
        return ["independent", "conj", "independent"]

    else:
        return random.choice([["independent", "sub conj", "dependent"], ["sub conj", "dependent", "independent"]])

def makeRels1(base):
    base[0].setVerb(base[1])
    base[1].setSubject(base[0])

def makeRels2(base):
    base[2].setVerb(base[1])
def makeRels3(base):
    base[2].setModifies(base[0])

def addDescriptors(base):
    #should I add the words in this function?
    sentence = [] #final sentence descriptors
    for part in base:
        if part == "independent":
            sentence.extend(getIndependent())
        elif part == "conj":
            sentence.extend(getConj())
        elif part == "sub conj":
            sentence.extend(getSubConj())
        else:
            sentence.extend(getDependent())
    return sentence

def getIndependent():
    structure = ["subject", "predicate"]
    result = []

    result.extend(getSubject())
    result.extend(getPredicate())

    return result

def getSubject():
    return [getRandSubject()]

def getPredicate():
    return ["2"]

def getConj():
    return [random.choice(["for", "and", "nor", "but", "or", "yet", "so"])]

def getSubConj():
    return [random.choice(["after", "although", "as", "because", "before", "even though", "if", "since", "though", "unless", "until", "when", "whenever", "whereas", "wherever", "while"])]

def getDependent():
    return ["3"]

def init():
    class Struct: pass
    global freq
    freq = Struct()
    freq.relProFreq=False
    freq.adjFreq=False
    freq.adverbFreq=False
    freq.doFreq=False
    freq.ioFreq=False
    freq.participleFreq=False #add participles
    freq.gerundFreq=False
    
def increaseRelProFreq():
    freq.relProFreq=True
    
def increaseAdverbFreq():
    freq.adverbFreq=True

def increaseDOFreq():
    freq.doFreq=True

def increaseParticipleFreq():
    freq.participleFreq=True

def increaseGerundFreq():
    freq.gerundFreq=True

def increaseFreq(pos):
    if pos == 'relative pronoun' or pos == 0:
        increaseRelProFreq()
    if pos == 'adverb' or pos == 1:
        increaseAdverbFreq()
    if pos == 'participle' or pos == 2:
        increaseParticipleFreq()
    if pos == 'gerund' or pos == 3:
        increaseGerundFreq()
    if pos == 'direct object' or pos==4:
        increaseDOFreq()

def addDescriptorsVerb(word):
    sentence=[]
    if word=='action verb':
        if prob(5):
            adv = getRandAdverb(word)
            if prob(3):
                sentence += [Adverb('very',adv)]
            sentence += [adv]
        sentence += [word]
    return sentence

def addDescriptorsNoun(word):
    sentence=[]
    if not word.isPronoun():
        if not word.isName() and not word.isGerund:
            sentence += [getRandDeterminer(word)]
            if prob(5) or (freq.adjFreq and not prob(5)): # add an adjective if not a name
                adj=getRandAdjective()
                if prob(5) or (freq.adverbFreq and not prob(5)):
                    sentence += [getRandAdverb(adj)]
                sentence += [adj]
        sentence += [word]
        if prob(3) or (freq.relProFreq and not prob(5)): # add relative clause
            # the clause itself is stored inside the rel pro
            # returns list
            relativePro,nec = getRandRelPro(word)
            sentence += relativePro
            if not nec:
                sentence+=[',']
    else:
        sentence += [getRandSubjPron(word)]
    return sentence

def getRandSubjPron(word):
    pronouns = [['we','they'],['I','you','he','she','it']]
    
    word.setWord(random.choice(pronouns[int(word.isSingular())]))
    w=word.getWord()
    if w == 'we' or w == 'I':
        word.setPerson(1)
    elif w == 'you':
        word.setPerson(2)
    else:
        word.setPerson(3)
    word.setIsPronoun(True)
    return word

def prob(upper):
    return not random.randint(0,upper)

def randBool():
    return bool(random.randint(0,1))

def getRandAdverb(modifies):
    return Adverb("happily", modifies)
    #return Adverb(random.randint(0,1),modifies)

def getRandRelPro(antec):
    nec = randBool()
    index = random.randint(0,1)
    typ = ['object', 'subject'][random.randint(0,1)]
    if antec.isName():
        relPros = ['who','whose']
        if antec == 'subject':
            relPro[0] = 'whom'
    else:
        relPros = ['which','that']
        nec = bool(index)
    relPron = relPros[index]
    if relPron == 'whose': typ = 'possessive'
    clause = getClause(typ)
    res = [relPro(relPron, antecedent = antec, necessary = nec)]
    res += clause
    if not nec: res=[',']+res #adds commas for unneccessary clauses
    return res,nec

def getClause(typ):
    if typ == 'possessive':
        return getBase()
    elif typ == 'subject':
        return [getRandActVerb(), getRandObjPP()]
    else:
        return [getRandSubject(),getRandActVerb()]

#DOES NOT WORK
def getRandDeterminer(modifies):
    print('determiner')    
    # that singular
    determiners = [['an' if isVowel(modifies.getWord()[0]) else 'a', 'the'],
                   ['this','that','these','those'],
                   ['my','your','his','her','its','our','their']]
    typ=random.randint(0,len(determiners)-1)
    # randomly choosing demonstrative pronoun article or possessive pronoun
    if typ == 0:
        function = 'article'
        if modifies.isSingular():
            index=2
        else:
            index = random.randint(0,len(determiners[typ])-1)
    elif typ == 1:
        function = 'demonstrative pronoun'
        if modifies.isSingular():
            index = random.randint(0,1)
        else:
            index = random.randint(2,3)
    elif typ == 2:
        function = 'possessive pronoun'
        index = random.randint(0,len(determiners[typ])-1)
    
    return Determiner(determiners[typ][index], modifies = modifies,
                      funct = function)

    

def isVowel(ch):
    return ch.lower() in set(['a','e','i','o','u'])

def getRandNoun(noun):
    if noun.isGerund():
        f = open('./POSLists/actionVerbs.txt')
        return addIng(getRandWord(f))
    else:
        if noun.isName():
            f = open('./POSLists/nameList.txt')
        else:
            f = open('./POSLists/nounList.txt')
        return getRandWord(f)+('s' if noun.isSingular() else '')
                

def getRandSubject(sing=randBool()):
                       
                       
    subj = Subject('', isSingular=sing,
                   isGerund = False,
                   isPronoun = prob(5),
                   name = False) #NEED TO CHANGE
    subj.setWord(getRandNoun(subj))
    return subj

def getRandOOP(prep):
    op = OP('',isSingular = randBool(), isGerund = prob(5) or (freq.gerundFreq and not prob(5)),
              isPronoun = prob(5), prep=prep,name = False) #NEED TO CHANGE
    op.setWord(getRandNoun(op))
    return op

def getRandDO():
    do = DO('',isPronoun = prob(5),name = False, isSingular = randBool(), isGerund = False)
    do.setWord(getRandNoun(do))
    return do

def getRandVerb(verb):
    # gets a random verb according to the predetermined, randomly generated criteria
    if verb.getFunct() == 'action verb':
        f = open('./POSLists/actionVerbs.txt')
        return getRandWord(f)
    else:
        f = open('./POSLists/linkingVerbs.txt')
        
def getPA():
    adj=Adjective('',function='predacate adjective')
    adj.setWord(getRandAdj())
    return adj

    
def getRandAdjective():
    f = open('./POSLists/adjectives.txt')
    return getRandWord(f)
        
def addIng(verb):
    if type(verb)==str:
        word=verb
    else:
        word = verb.getWord()
    # if the word ends in e and the second to last letter is not o e or y,
    # replace the e
    if word[-1]=='e' and (word[-2]!='o' and word[-2]!='e' and word[-2]!='y'):
        word = word[:-1]+'ing'
    # else just add ing
    else:
        word+='ing'
    if type(verb)==str:
        return word
    verb.setWord(word)

def testAddIng():
    assert(addIng(Verb('walk','action verb','past'))=='walking')
    assert(addIng(Verb('bake','action verb','present'))=='baking')
    assert(addIng(Verb('free','action verb','present'))=='freeing')

def addEd(verb):
    word = verb.getWord()
    word+='ed'
    verb.setWord(word)

def getRandActVerb(sing=randBool()):
    actV = ActionVerb('', getRandTense, isSingular=sing,isCompleted = randBool())
    actV.setWord(getRandVerb(actV))
    return actV
#---------------Tenses----------------#

def getPresentContinuous(verb):
    verb.addIng()
    if verb.isSingular():
        if verb.getPerson()==1:
            helpV='am'
        if verb.getPerson()==2:
            helpV='are'
        if verb.getPerson()==3:
            helpV='is'
    else:
        helpV='are'
    
    return helpingVerb(helpV,'present',verb,verb.isSingular)+verb

#def getPastContinuous(verb):

def getRandTense():
    return ['present','future','past'][random.randint(0,2)]

def getRandObjPP():
    #NEEDS TO RETURN OBJECT
    # get random objective personal pronouns
    pps = ['me']*3+['you','him','her','it','us']+3*['them']
    return pps[random.randint(0,len(pps)-1)]

def getRandPrepPhrase():
    f = open('prepList.txt')
    prep = getRandWord(f)
    prepPhrase = addDescriptorsNoun()

def getRandWord(f):
    return random.choice(f.readlines()).rstrip()

print(getSentence())
