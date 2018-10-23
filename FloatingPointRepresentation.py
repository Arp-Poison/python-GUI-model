import wx

import random

# global variables

questions_asked = 0
correct = 0
wrong = 0

for x in range(1):
    random = (random.randint(15, 25))

test_length = random

# real number representation section


class learn_real_number_representation_Frame(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Real Number Representation", size=(1000, 700))

        jpg = wx.Image("images/floatingpage1.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

        next_button = wx.Button(self.bmap, label="Next", pos=(900, 650))
        next_button.Bind(wx.EVT_BUTTON, self.onNext)

    def onNext(self, event):
        frame = learn_real_number_representation_Frame_2()
        frame.Show()

    def onBack(self, event):
        from Title_Page import real_number_representation_Frame

        self.Destroy()

        frame = real_number_representation_Frame()
        frame.Show()


class learn_real_number_representation_Frame_2(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Real Number Representation", size=(1000, 700))

        jpg = wx.Image("images/floatingpage2.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    def onBack(self, event):

        self.Destroy()

        frame = learn_real_number_representation_Frame()
        frame.Show()


class real_number_representation_test_Frame(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Real Number Representation Test", size=(1000, 700))

        jpg = wx.Image("images/binarytestbg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        # -----------------------------------------------
        # Failed attempt at random generation and conversion of binary floating point numbers
        import random
        import struct

        #decimal_value = 0

        #for x in range(1):
            #decimal_value = (random.randint(-1000000000, 1000000000))

        #print(decimal_value)

        #self.binary_number = (bin(decimal_value)[2:])
        #print(self.binary_number)
        #if self.binary_number[0] == 'b':
            #self.binary_number = self.binary_number[:1] + '0' + self.binary_number[1:]
        '''
        binary_num = '{:032b}'.format(decimal_value)
        binary_num = str(binary_num)
        if binary_num[0] == "-":
            binary_num = binary_num.replace('-', "1")
            print("called")

        self.binary_num = binary_num
        print(binary_num)
        self.binary_num = int(self.binary_num, 2)
        floating_point = struct.unpack('f', struct.pack('I', self.binary_num))[0]

        print(floating_point)
        #sign = self.binary_num[0]
        #exponent = self.binary_num[1:9]
        #mantissa = self.binary_num[9:]

        #print(sign, exponent, mantissa)

        # -----------------------------------------------

        instructions = wx.StaticText(self.bmap, label="What is the decimal value of" + " " + binary_num + " " + "?", pos=(300, 40))
        self.msgTxt = wx.TextCtrl(self.bmap, value="", pos=(420, 70))

        submit_button = wx.Button(self.bmap, label="Submit", pos=(420, 110))
        submit_button.Bind(wx.EVT_BUTTON, self.onSubmit)

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)
        '''
        # Hard coded questions

        wx.StaticText(self.bmap, label="What is -1.11001 x2^1101 in IEE 754 single precision floating point 32 bit standard (binary)?", pos=(300, 40))
        self.Q1 = wx.TextCtrl(self.bmap, value="", pos=(420, 70))

        submit_button = wx.Button(self.bmap, label="Submit", pos=(420, 100))
        submit_button.Bind(wx.EVT_BUTTON, self.onSubmit)

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    def onSubmit(self, event):
        global correct
        global wrong

        # Retrieving usr answer from msgText variable
        value1 = self.Q1.GetValue()

        # Checking usr answer to calculated answer
        if value1 == "11100101011001000000000000000000":
            wx.StaticText(self.bmap, label="Correct", pos=(420, 300))
            correct += 1  # Adding one to total correct answers for this test
        else:
            wrong += 1

        frame = score_Frame()
        frame.Show()

    def onBack(self, event):
        from Title_Page import real_number_representation_Frame

        frame = real_number_representation_Frame()
        frame.Show()

        self.Destroy()


class learn_limitations_Frame(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Limitations", size=(1000, 700))

        jpg = wx.Image("images/limitations.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    def onBack(self, event):
        from Title_Page import limitations_Frame

        frame = limitations_Frame()
        frame.Show()

        self.Destroy()


class limitations_test_Frame(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Limitations Test", size=(1000, 700))

        jpg = wx.Image("images/binarytestbg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        wx.StaticText(self.bmap, label="What is the main limitation of IEE 754 single precision floating point 32 bit standard?", pos=(300, 40))
        self.Q1 = wx.TextCtrl(self.bmap, value="", pos=(420, 70))

        submit_button = wx.Button(self.bmap, label="Submit", pos=(420, 100))
        submit_button.Bind(wx.EVT_BUTTON, self.onSubmit)

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    def onSubmit(self, event):

        # Defining global variables (used to avoid overwriting variables after frame calls)
        global correct
        global wrong

        # Retrieving usr answer from msgText variable
        value1 = self.Q1.GetValue()

        # Checking usr answer to calculated answer
        if value1 == "The range of numbers that can be represented":
            wx.StaticText(self.bmap, label="Correct", pos=(420, 300))
            correct += 1  # Adding one to total correct answers for this test
        else:
            wrong += 1

        frame = score_Frame()
        frame.Show()

    def onBack(self, event):
        from Title_Page import limitations_Frame

        frame = limitations_Frame()
        frame.Show()

        self.Destroy()


class score_Frame(wx.Frame):

    def __init__(self):
        global correct
        global wrong
        correct = str(correct)

        wx.Frame.__init__(self, None, wx.ID_ANY, "Test Score", size=(1000, 700))

        jpg = wx.Image("images/binarytestbg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        wx.StaticText(self.bmap, label="Correct:" + " " + str(correct), pos=(420, 240))
        wx.StaticText(self.bmap, label="With" + " " + str(wrong) + " " + "wrong answers", pos=(420, 280))


'''
Change Log:

~Added self.Destroy() to all open new frame functions to remove window build up 24/2/18

~Moved self.Destroy() to after new frame open call to avoid errors resulting in loss of all windows

~Combined small decimal number representation and large decimal number representation into one section

~Added integer vs non integer values into real number representation section

~Added comments to describe sections of code 28/2/28  

~Fixed commenting errors 1/3/18

'''