import wx
import random
# global variables and generating random test length

questions_asked = 0
correct = 0
wrong = 0

for x in range(1):
    random = (random.randint(15, 25))

test_length = random

# Binary


class learn_binary_Frame(wx.Frame):

    # teach

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Learn Binary", size=(1000, 700))

        jpg = wx.Image("binarytodecimal.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

        next_button = wx.Button(self.bmap, label="Next", pos=(900, 650))
        next_button.Bind(wx.EVT_BUTTON, self.onNext)

    def onNext(self, event):

        frame = learn_binary_Frame_2()
        frame.Show()

    def onBack(self, event):
        from Title_Page import binary_Frame

        self.Destroy()

        frame = binary_Frame()
        frame.Show()


class learn_binary_Frame_2(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Learn Binary", size=(1000, 700))

        jpg = wx.Image("decimaltobinary.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    def onBack(self, event):
        self.Destroy()

        frame = learn_binary_Frame()
        frame.Show()


class binary_test_Frame(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Binary Test", size=(1000, 700))

        jpg = wx.Image("binarytestbg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (0, 0), (jpg.GetWidth(), jpg.GetHeight()))

        #-------------------------------------------
        import random

        binary_num = []
        binary_str = []

        # Generating random integer (1 or 0) to act as binary number
        for x in range(10):
            binary_num.append(random.randint(0, 1))  # Appending generated digit to array

        for e in binary_num:
            e = str(e)
            binary_str.append(e)

        joined_binary_str = (''.join(binary_str))  # Joining binary array to form the binary number

        power = 0
        total = 0

        binary_num.reverse()  # In order to multiply by increasing powers number is reversed (left to right rather than right to left)
        for e in binary_num:
            if e != 0:
                total += 2 ** power
            power += 1
        print(total)

        self.total = str(total)

        print(self.total)

        #-----------------------------------------------#

        instructions = wx.StaticText(self.bmap, label="What is" + " "+joined_binary_str+" " + "in decimal?", pos=(420, 40))
        self.msgTxt = wx.TextCtrl(self.bmap, value="", pos=(460, 70))

        submit_button = wx.Button(self.bmap, label="Submit", pos=(470, 110))
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
        print(questions_asked)
        print(test_length)

        # Retrieving usr answer from msgText variable
        value = self.msgTxt.GetValue()

        value = int(value)

        # Checking usr answer to calculated answer
        if value == self.total:
            wx.StaticText(self.bmap, label="Correct", pos=(420, 80))
            correct += 1  # Adding one to total correct answers for this test
            if questions_asked <= test_length:  # Checking if the number of questions asked is less then the generated test length
                frame = binary_test_Frame()
                frame.Show(True)
                self.Destroy()
            else:
                frame = score_Frame()
                frame.Show()

        else:
            wx.StaticText(self.bmap, label="Incorrect", pos=(420, 80))
            wrong += 1
            if questions_asked <= test_length:  # Checking if the number of questions asked is less then the generated test length
                frame = binary_test_Frame()
                frame.Show(True)
                self.Destroy()
            else:
                frame = score_Frame()
                frame.Show()

    def onBack(self, event):
        from Title_Page import binary_Frame

        frame = binary_Frame()
        frame.Show()

        self.Destroy()

#Hexadecimal


class learn_hexadecimal_Frame(wx.Frame):
    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Learn Hexadecimal", size=(1000, 700))

        jpg = wx.Image("hextobinary.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

        next_button = wx.Button(self.bmap, label="Next", pos=(900, 650))
        next_button.Bind(wx.EVT_BUTTON, self.onNext)

    def onNext(self, event):
        self.Destroy()

        frame = learn_hexadecimal_Frame_2()
        frame.Show()

    def onBack(self, event):
        from Title_Page import hexadecimal_Frame

        self.Destroy()

        frame = hexadecimal_Frame()
        frame.Show()


class learn_hexadecimal_Frame_2(wx.Frame):
    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Learn Hexadecimal", size=(1000, 700))

        jpg = wx.Image("binarytohex.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (0, 0), (jpg.GetWidth(), jpg.GetHeight()))

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    def onBack(self, event):
        self.Destroy()

        frame = learn_hexadecimal_Frame()
        frame.Show()


class hexadecimal_test_Frame(wx.Frame):
    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Hexadecimal Test", size=(1000, 700))

        jpg = wx.Image("hexadecimaltestbg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (0, 0), (jpg.GetWidth(), jpg.GetHeight()))

        # -----------------------------------------------

        import random

        ran = random.randrange(5 ** 10)
        hexadecimal_number = "%02x" % ran  # Generating random hexadecimal number

        print(hexadecimal_number)

        self.decimal_value = int(hexadecimal_number, 16)  # converting to base 16 (hexadecimal)

        print(self.decimal_value)

    # -----------------------------------------------

        instructions = wx.StaticText(self.bmap, label="What is" + " " + hexadecimal_number + " " + "in decimal?", pos=(420, 40))
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
        print(questions_asked)
        print(test_length)

        # Retrieving usr answer from msgText variable
        value = self.msgTxt.GetValue()

        value = int(value)

        # Checking usr answer to calculated answer
        if value == self.decimal_value:
            wx.StaticText(self.bmap, label="Correct", pos=(420, 80))
            correct += 1  # Adding one to total correct answers for this test
            if questions_asked <= test_length:  # Checking if the number of questions asked is less then the generated test length
                frame = hexadecimal_test_Frame()
                frame.Show(True)
                self.Destroy()
            else:
                frame = score_Frame()
                frame.Show()


        else:
            wx.StaticText(self.bmap, label="Incorrect", pos=(420, 80))
            wrong += 1
            if questions_asked <= test_length:  # Checking if the number of questions asked is less then the generated test length
                frame = hexadecimal_test_Frame()
                frame.Show(True)
                self.Destroy()
            else:
                frame = score_Frame()
                frame.Show()

    def onBack(self, event):
        from Title_Page import hexadecimal_Frame

        frame = hexadecimal_Frame()
        frame.Show()

        self.Destroy()


# Decimal

class learn_decimal_Frame(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Learn Decimal", size=(1000, 700))

        jpg = wx.Image("decimaltobinary.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    def onBack(self, event):
        from Title_Page import diffrent_number_systems

        self.Destroy()

        frame = diffrent_number_systems()
        frame.Show()


class decimal_test_Frame(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Decimal Test", size=(1000, 700))

        jpg = wx.Image("binarytestbg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (0, 0), (jpg.GetWidth(), jpg.GetHeight()))

        # -----------------------------------------------

        import random

        decimal_value = 0

        # generating random integer for conversion to binary
        for x in range(1):
            decimal_value = (random.randint(1, 100))

        self.binary_number = int(bin(decimal_value)[2:])  # Converting generated decimal to binary
        print(self.binary_number)

        decimal_value = str(decimal_value)
    # -----------------------------------------------

        instructions = wx.StaticText(self.bmap, label="What is" + " " + decimal_value + " " + "in binary?", pos=(420, 40))
        self.msgTxt = wx.TextCtrl(self.bmap, value="", pos=(420, 70))

        submit_button = wx.Button(self.bmap, label="Submit", pos=(420, 110))
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
        print(questions_asked)
        print(test_length)

        value = self.msgTxt.GetValue()

        value = int(value)

        # Checking usr answer to calculated answer
        if value == self.binary_number:
            wx.StaticText(self.bmap, label="Correct", pos=(420, 80))
            correct += 1  # Adding one to total correct answers for this test
            if questions_asked <= test_length:  # Checking if the number of questions asked is less then the generated test length
                frame = decimal_test_Frame()
                frame.Show(True)
                self.Destroy()
            else:
                frame = score_Frame()
                frame.Show()

        else:
            wx.StaticText(self.bmap, label="Incorrect", pos=(420, 80))
            wrong += 1
            if questions_asked <= test_length:  # Checking if the number of questions asked is less then the generated test length
                frame = decimal_test_Frame()
                frame.Show(True)
                self.Destroy()
            else:
                frame = score_Frame()
                frame.Show()

    def onBack(self, event):
        from Title_Page import decimal_Frame

        frame = decimal_Frame()
        frame.Show()

        self.Destroy()

# Score frame for user feedback/results


class score_Frame(wx.Frame):

    def __init__(self):
        global correct
        global wrong
        correct = str(correct)

        wx.Frame.__init__(self, None, wx.ID_ANY, "Test Score", size=(1000, 700))

        jpg = wx.Image("binarytestbg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        wx.StaticText(self.bmap, label="Correct:" + " " + str(correct), pos=(420, 240))
        wx.StaticText(self.bmap, label="With" + " " + str(wrong) + " " + "wrong answers", pos=(420, 280))


'''
Change Log:

~Migrated learn_binary_Frame_2 into learn decimal frame 23/2/18

~Added self.Destroy() to all open new frame functions to remove window build up 24/2/18

~Removed self.Destroy() from calls to score frame 27/2/18

~Added comments to describe sections of code 29/2/28

~Fixed commenting errors 1/3/18

'''