import wx
import random

#global variables

questions_asked = 0
correct = 0
wrong = 0

for x in range(1):
    random = (random.randint(15, 25))

test_length = random
#Sign and modulus


class learn_sign_modulus_Frame(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Learn Sign & Modulus", size=(1000, 700))

        jpg = wx.Image("images/signmod.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    def onBack(self, event):
        from Title_Page import sign_modulus

        self.Destroy()

        frame = sign_modulus()
        frame.Show()


class sign_modulus_test_Frame(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Sign & Modulus Test", size=(1000, 700))

        jpg = wx.Image("images/signmodtestbg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        # -----------------------------------------------
        import random

        decimal_value = 0

        for x in range(1):
            decimal_value = (random.randint(-100, 100))

        print(decimal_value)

        self.binary_number = (bin(decimal_value)[2:])
        print(self.binary_number)
        if self.binary_number[0] == 'b':
            self.binary_number = self.binary_number[:1] + '0' + self.binary_number[1:]
            self.sign = self.binary_number[1]
            string_of_bin = str(self.binary_number[1:])
            print(self.sign)
            self.answer = "negative"
            print(self.answer)

        else:
            print(self.binary_number)
            string_of_bin = str(self.binary_number)
            self.sign = (string_of_bin[0])
            print(self.sign)
            self.answer = "positive"
            print(self.answer)

        # -----------------------------------------------

        instructions = wx.StaticText(self.bmap, label="Use the sign of the binary number to determine weather it is positive or negative" + " " + string_of_bin, pos=(300, 40))
        self.msgTxt = wx.TextCtrl(self.bmap, value="", pos=(420, 70))

        submit_button = wx.Button(self.bmap, label="Submit", pos=(420, 110))
        submit_button.Bind(wx.EVT_BUTTON, self.onSubmit)

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    def onBack(self, event):
        from Title_Page import sign_modulus

        self.Destroy()

        frame = sign_modulus()
        frame.Show()

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

        # Checking usr answer to calculated answer
        if value == self.answer:
            wx.StaticText(self.bmap, label="Correct", pos=(420, 250))
            correct += 1  # Adding one to total correct answers for this test
            if questions_asked <= test_length:
                frame = sign_modulus_test_Frame()
                frame.Show(True)
                self.Destroy()
            else:
                frame = score_Frame()
                frame.Show()

        else:
            wx.StaticText(self.bmap, label="Incorrect", pos=(420, 250))
            wrong += 1
            if questions_asked <= test_length:
                frame = sign_modulus_test_Frame()
                frame.Show(True)
                self.Destroy()
            else:
                frame = score_Frame()
                frame.Show()


#1's complement

class learn_ones_and_twos_complement_Frame(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Learn 1's and 2's Complement", size=(1000, 700))

        jpg = wx.Image("images/complementpage1.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

        next_button = wx.Button(self.bmap, label="Next", pos=(900, 650))
        next_button.Bind(wx.EVT_BUTTON, self.onNext)

    def onNext(self, event):
        frame = learn_ones_and_twos_complement_Frame_2()
        frame.Show()

    def onBack(self, event):
        from Title_Page import ones_and_twos_complement

        self.Destroy()

        frame = ones_and_twos_complement()
        frame.Show()


class learn_ones_and_twos_complement_Frame_2(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Learn 1's and 2's Complement", size=(1000, 700))

        jpg = wx.Image("images/complementpage2.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    def onBack(self, event):

        self.Destroy()

        frame = learn_ones_and_twos_complement_Frame()
        frame.Show()


class ones_and_twos_complement_test_Frame(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "1's and 2's complement test", size=(1000, 700))

        jpg = wx.Image("images/complementstestbg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        # -----------------------------------------------

        import random

        decimal_value = 0
        bin_array =[]

        for x in range(1):
            decimal_value = (random.randint(1, 100))

        self.binary_number = (bin(decimal_value)[2:])
        print(self.binary_number)

        for e in self.binary_number:
            if e == '1':
                bin_array.append("0")
            else:
                bin_array.append("1")
        bin_array.reverse()
        bin_array[0] = '1'
        bin_array.reverse()

        print("".join(bin_array))
        self.twos_complement = "".join(bin_array)
        # -----------------------------------------------

        instructions = wx.StaticText(self.bmap, label="What is the twos complement of" + " " + self.binary_number + " " + "?", pos=(420, 40))
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

        # Retrieving usr answer from msgText variable
        value = self.msgTxt.GetValue()

        # Checking usr answer to calculated answer
        if value == self.twos_complement:
            wx.StaticText(self.bmap, label="Correct", pos=(420, 80))
            correct += 1  # Adding one to total correct answers for this test
            if questions_asked <= test_length:
                frame = ones_and_twos_complement_test_Frame()
                frame.Show(True)
                self.Destroy()
            else:
                frame = score_Frame()
                frame.Show()

        else:
            wx.StaticText(self.bmap, label="Incorrect", pos=(420, 80))
            wrong += 1
            if questions_asked <= test_length:
                frame = ones_and_twos_complement_test_Frame()
                frame.Show(True)
                self.Destroy()
            else:
                frame = score_Frame()
                frame.Show()

    def onBack(self, event):
        from Title_Page import ones_and_twos_complement

        frame = ones_and_twos_complement()
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

~Rolled 1's and 2's complement into one section 25/2/18

~Added comments to describe sections of code 28/2/28

~Fixed commenting errors 1/3/18

'''