class Question:
    
    def __init__(self, A, B, C):
        self.A = A 
        self.B = B
        self.C = C
    
    def text(self): 
        print("Question in text and list of answers")

class One(Question):

    def text(self): 
        print("How are you now?")
    
    def choices(self):
        self.A = "I feel pretty good, life is fantastic"
        self.B = "I'm alright"
        self.C = "The worst feeling that I ever have"
        print("A: " + self.A + "\n" + "B: " + self.B + "\n" + "C: " + self.C)
   
class Two(Question):

    def text(self):
        print("How often do you feel bad?")

    def choices(self):
        self.A = "Once or few times in a month"
        self.B = "Once or few times in a week"
        self.C = "Every single day in my life"
        print("A: " + self.A + "\n" + "B: " + self.B + "\n" + "C: " + self.C)

class Three(Question):
     
    def text(self):
        print("Are you feeling stressful?")

    def choices(self):
        self.A = "No, never"
        self.B = "Sometimes"
        self.C = "I'm suffering from stress for a long time"
        print("A: " + self.A + "\n" + "B: " + self.B + "\n" + "C: " + self.C)

class Four(Question):
    
    def text(self):
        print("If you do have stress, do you know where the stress came from?")

    def choices(self):
        self.A = "I don't have stress"
        self.B = "Yes"
        self.C = "No"
        print("A: " + self.A + "\n" + "B: " + self.B + "\n" + "C: " + self.C)

class Five(Question):
    
    def text(self):
        print("If you do have stress, do you know how to deal with it?")

    def choices(self):
        self.A = "I don't have stress"
        self.B = "Yes"
        self.C = "No"
        print("A: " + self.A + "\n" + "B: " + self.B + "\n" + "C: " + self.C)

class Six(Question):

    def text(self):
        print("Will you tell your friends and family if you do feel stressful?")

    def choices(self):
        self.A = "Yes, I've talked with some of them"
        self.B = "Not yet, but I will" 
        self.C = "I won't"
        print("A: " + self.A + "\n" + "B: " + self.B + "\n" + "C: " + self.C)

class Seven(Question):

    def text(self):
        print("Is there anything you are passionate about to do?")

    def choices(self):
        self.A = "Yes, I have a lot"
        self.B = "One thing"
        self.C = "None"
        print("A: " + self.A + "\n" + "B: " + self.B + "\n" + "C: " + self.C)

class Eight(Question):

    def text(self): 
        print("Do you have friends that you like to hang out with")

    def choices(self):
        self.A = "A lot"
        self.B = "One or two"
        self.C = "None"
        print("A: " + self.A + "\n" + "B: " + self.B + "\n" + "C: " + self.C)

class Nine(Question):

    def text(self):
        print("Do you like your job/school?")

    def choices(self):
        self.A = "Yes"
        self.B = "I'm ok with it"
        self.C = "Not at all"
        print("A: " + self.A + "\n" + "B: " + self.B + "\n" + "C: " + self.C)

class Ten(Question):

    def text(self):
        print("Do you like yourself?")

    def choices(self):
        self.A = "Definitely"
        self.B = "Fine"
        self.C = "No"
        print("A: " + self.A + "\n" + "B: " + self.B + "\n" + "C: " + self.C)

class Eleven(Question):

    def text(self):
        print("How often do you stay up?")

    def choices(self):
        self.A = "Never"
        self.B = "Few times in a weak"
        self.C = "Everyday"
        print("A: " + self.A + "\n" + "B: " + self.B + "\n" + "C: " + self.C)

class Twelve(Question):

    def text(self):
        print("If you do stay up, do you know why?")

    def choices(self):
        self.A = "I don't stay up"
        self.B = "Yes"
        self.C = "No"
        print("A: " + self.A + "\n" + "B: " + self.B + "\n" + "C: " + self.C)

class Thirteen(Question):

    def text(self):
        print("What does tomorrow means to you?")

    def choices(self):
        self.A = "Another wonderful day"
        self.B = "A new day"
        self.C = "Another day that makes me suffer"
        print("A: " + self.A + "\n" + "B: " + self.B + "\n" + "C: " + self.C)

class Fourteen(Question):

    def text(self):
        print("If you have a chance, do you want to live the same life?")

    def choices(self):
        self.A = "Yes"
        self.B = "Kind of"
        self.C = "No"
        print("A: " + self.A + "\n" + "B: " + self.B + "\n" + "C: " + self.C)

class Fifteen(Question):

    def text(self):
        print("Do you think mental health is important?")

    def choices(self):
        self.A = "Yes"
        self.B = "Sort of"
        self.C = "No"
        print("A: " + self.A + "\n" + "B: " + self.B + "\n" + "C: " + self.C)

class Sixteen(Question):

    def text(self):
        print("Do you think feeling sad is equal to have a mental health issue?")

    def choices(self):
        self.A = "It's not the same"
        self.B = "They're related"
        self.C = "Yes"
        print("A: " + self.A + "\n" + "B: " + self.B + "\n" + "C: " + self.C)

class Seventeen(Question):

    def text(self):
        print("Do you always feel tired of your life?")

    def choices(self):
        self.A = "No"
        self.B = "Sometimes"
        self.C = "Yes"
        print("A: " + self.A + "\n" + "B: " + self.B + "\n" + "C: " + self.C)

class Eighteen(Question):

    def text(self):
        print("Do you think doctors are actually going to help you?")

    def choices(self):
        self.A = "Yes, they are professional"
        self.B = "I guess"
        self.C = "No, they can't help"
        print("A: " + self.A + "\n" + "B: " + self.B + "\n" + "C: " + self.C)

class Nineteen(Question):

    def text(self):
        print("Have you ever think about suicide?")

    def choices(self):
        self.A = "No"
        self.B = "Once or Twice"
        self.C = "Oftenly"
        print("A: " + self.A + "\n" + "B: " + self.B + "\n" + "C: " + self.C)

class Twenty(Question):

    def text(self):
        print("What brought you here?")

    def choices(self):
        self.A = "Just for fun"
        self.B = "Try to do a test"
        self.C = "I need help"
        print("A: " + self.A + "\n" + "B: " + self.B + "\n" + "C: " + self.C)