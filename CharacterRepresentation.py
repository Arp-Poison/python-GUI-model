# Importing modules

import wx
import random

# global variables and generating random test length

questions_asked = 0
correct = 0
wrong = 0

for x in range(1):
    random = (random.randint(15, 25))

test_length = random
# ASII

# Demonstrate & Teach

# Defining frame


class learn_ASCII_Frame(wx.Frame):
# Defining constructor
    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Learn ASCII", size=(1000, 700))

        # Defining path to background image, image type, converting it to bitmap, defining its anchors
        jpg = wx.Image("images/asciipage1.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

        next_button = wx.Button(self.bmap, label="Next", pos=(900, 650))
        next_button.Bind(wx.EVT_BUTTON, self.onNext)

    def onNext(self, event):
        frame = learn_ASCII_Frame_2()
        frame.Show()

        self.Destroy()

    def onBack(self, event):
        from Title_Page import ASCII_Frame

        frame = ASCII_Frame()
        frame.Show()

        self.Destroy()


class learn_ASCII_Frame_2(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Learn ASCII", size=(1000, 700))

        # Defining path to background image, image type, converting it to bitmap, defining its anchors
        jpg = wx.Image("images/asciipage2.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    def onBack(self, event):

        frame = learn_ASCII_Frame()
        frame.Show()

        self.Destroy()


    #Test
class ASCII_test_Frame(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "ASCII test", size=(1000, 700))

        # Defining path to background image, image type, converting it to bitmap, defining its anchors
        jpg = wx.Image("images/asciitestbg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

        # -------------------------------------------
        # Importing modules
        import random
        import string

        # generation of random word
        word = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(5))
        print(word)

        # Retrieving ascii value code for letters in generated word
        ascii = [ord(c) for c in word]
        ascii = str(ascii)
        self.ascii = ascii.strip('[]')
        print(self.ascii)
        # -------------------------------------------

        # Display to screen question + answer text box
        instructions = wx.StaticText(self.bmap, label="What is the ASCII value of" + " " + word + " " + "?", pos=(420, 40))
        self.msgTxt = wx.TextCtrl(self.bmap, value="", pos=(460, 70))

        # Defining submit button to submit usr answer
        submit_button = wx.Button(self.bmap, label="Submit", pos=(480, 110))
        submit_button.Bind(wx.EVT_BUTTON, self.onSubmit)

    def onSubmit(self, event):
        # Defining global variables (used to avoid overwriting variables after frame calls)
        global questions_asked
        global test_length
        global correct
        global wrong
        questions_asked += 1
        print(questions_asked)
        print(test_length)

        # Retrieving usr answer from msgText variable
        value = self.msgTxt.GetValue()

        value = int(value)

        # Checking usr answer to calculated answer
        if value == self.ascii:
            wx.StaticText(self.bmap, label="Correct", pos=(420, 80))
            correct += 1  # Adding one to total correct answers for this test
            if questions_asked <= test_length:  # Checking if the number of questions asked is less then the generated test length

                frame = ASCII_test_Frame()  # Call to execute this frame again displaying new question
                frame.Show(True)
                self.Destroy()
            else:
                frame = score_Frame()
                frame.Show()
                self.Destroy()

        else:
            wx.StaticText(self.bmap, label="Incorrect", pos=(420, 80))
            wrong += 1  # Adding one to total wrong answers for this test
            if questions_asked <= test_length:  # Checking if the number of questions asked is less then the generated test length

                frame = ASCII_test_Frame()  # Call to execute this frame again displaying new question
                frame.Show(True)
                self.Destroy()
            else:
                frame = score_Frame()
                frame.Show()
                self.Destroy()

    def onBack(self, event):
        from Title_Page import ASCII_Frame

        frame = ASCII_Frame()
        frame.Show()

        self.Destroy()


# Unicode
    # Demonstraight & Teach

class learn_unicode_Frame(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Learn Unicode", size=(1000, 700))

        # Defining path to background image, image type, converting it to bitmap, defining its anchors
        jpg = wx.Image("images/unicodepage1.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

        next_button = wx.Button(self.bmap, label="Next", pos=(900, 650))
        next_button.Bind(wx.EVT_BUTTON, self.onNext)

    def onNext(self, event):
        frame = learn_unicode_Frame_2()
        frame.Show()

        self.Destroy()

    def onBack(self, event):
        from Title_Page import Unicode_Frame

        frame = Unicode_Frame()
        frame.Show()

        self.Destroy()


class learn_unicode_Frame_2(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Learn Unicode", size=(1000, 700))

        # Defining path to background image, image type, converting it to bitmap, defining its anchors
        jpg = wx.Image("images/unicodepage2.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    def onBack(self, event):

        frame = learn_unicode_Frame()
        frame.Show()

        self.Destroy()

# Test


class unicode_test_Frame(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Unicode Test", size=(1000, 700))

        # Defining path to background image, image type, converting it to bitmap, defining its anchors
        jpg = wx.Image("images/unicodetestbg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        import random
        import string

        letter = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(1))
        self.hex_value = format(ord(letter), "x")
        print(self.hex_value)
        self.hex_value = str("U+00" + self.hex_value)


        # -------------------------------------------

        instructions = wx.StaticText(self.bmap, label="What is the Unicode value of " + letter + " " + "in U+00## form?", pos=(420, 40))
        self.msgTxt = wx.TextCtrl(self.bmap, value="", pos=(460, 70))

        submit_button = wx.Button(self.bmap, label="Submit", pos=(480, 110))
        submit_button.Bind(wx.EVT_BUTTON, self.onSubmit)

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    def onSubmit(self, event):
        # Defining global variables (used to avoid overwriting variables after frame calls)
        global questions_asked
        global test_length
        global correct
        global wrong
        questions_asked += 1

        # Retrieving usr answer from msgText variable
        value = self.msgTxt.GetValue()

        value = str(value)

        # Checking usr answer to calculated answer
        if value == self.hex_value:

            wx.StaticText(self.bmap, label="Correct", pos=(420, 150))
            correct += 1  # Adding one to total correct answers for this test
            if questions_asked <= test_length:  # Checking if the number of questions asked is less then the generated test length
                frame = unicode_test_Frame()  # Call to execute this frame again displaying new question
                frame.Show(True)
                self.Destroy()
            else:
                frame = score_Frame()
                frame.Show()
                self.Destroy()

        else:

            wx.StaticText(self.bmap, label="Incorrect", pos=(420, 150))
            wrong += 1
            if questions_asked <= test_length:  # Checking if the number of questions asked is less then the generated test length
                frame = unicode_test_Frame()  # Call to execute this frame again displaying new question
                frame.Show(True)
                self.Destroy()
            else:
                frame = score_Frame()
                frame.Show()
                self.Destroy()

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    def onBack(self, event):
        from Title_Page import Unicode_Frame

        frame = Unicode_Frame()
        frame.Show()

        self.Destroy()

# Defining Score frame to be displayed at the end of tests


class score_Frame(wx.Frame):

    def __init__(self):

        # Reterving global variables
        global correct
        global wrong
        correct = str(correct)

        wx.Frame.__init__(self, None, wx.ID_ANY, "Test Score", size=(1000, 700))

        jpg = wx.Image("images/asciitestbg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        # Display to screen
        wx.StaticText(self.bmap, label="Correct:" + " " + str(correct), pos=(420, 240))
        wx.StaticText(self.bmap, label="With" + " " + str(wrong) + " " + "wrong answers", pos=(420, 280))


'''
Change Log:

~Added self.Destroy() to all open new frame functions to remove window build up 24/2/18

~Moved self.Destroy() to after the new frame call to avoid failure to load errors resulting in total window loss 25/2/18

~Added varied test length to all test sections 27/2/18

~Added comments to describe sections of code 28/2/28

~Removed stubs and commented out code 29/2/28

~Fixed commenting errors 1/3/18

'''