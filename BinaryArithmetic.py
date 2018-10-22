import wx
import random

# global variables and generating random test length

questions_asked = 0
correct = 0
wrong = 0

for x in range(1):
    random = (random.randint(15, 25))

test_length = random


# Addition
class learn_binary_addition_Frame(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Learn Binary Addition", size=(1000, 700))

        jpg = wx.Image("binaryaddition1.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    def onBack(self, event):
        from Title_Page import binary_addition

        frame = binary_addition()
        frame.Show()

        self.Destroy()


class binary_addition_test_Frame(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Binary Addition Test", size=(1000, 700))

        jpg = wx.Image("binarymathtestbg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (0, 0), (jpg.GetWidth(), jpg.GetHeight()))

        # -------------------------------------------

        import random

        decimal_value_1 = 0
        decimal_value_2 = 0

        # Generating random integers to be converted to binary
        for x in range(1):
            decimal_value_1 = random.randint(1, 100)
            decimal_value_2 = random.randint(1, 100)

        binary_value_1 = int(bin(decimal_value_1)[2:])
        binary_value_2 = int(bin(decimal_value_2)[2:])

        binary_value_1 = str(binary_value_1)  # Converting bin values to string so that they can be displayed on screen
        binary_value_2 = str(binary_value_2)

        binary_value = bin(int(binary_value_1, 2) + int(binary_value_2, 2))  # Calculating binary addition value

        print((binary_value[2:]))

        self.binary_value = (binary_value[2:])  # making variable callable outside function

        # -------------------------------------------

        instructions = wx.StaticText(self.bmap, label="What is" + " " + binary_value_1 + " " + "+" + binary_value_2 + " " + "in binary", pos=(420, 40))
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

        # Reterving usr answer from msgText variable
        value = self.msgTxt.GetValue()

        value = int(value)

        # Checking usr answer to calculated answer
        if value == self.binary_value:
            wx.StaticText(self.bmap, label="Correct", pos=(420, 80))
            correct += 1  # Adding one to total correct answers for this test
            if questions_asked <= test_length:  # Checking if the number of questions asked is less then the generated test length

                frame = binary_addition_test_Frame()   # Call to execute this frame again displaying new question
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

                frame = binary_addition_test_Frame()  # Call to execute this frame again displaying new question
                frame.Show(True)
                self.Destroy()

            else:
                frame = score_Frame()
                frame.Show()
                self.Destroy()

    def onBack(self, event):
        from Title_Page import binary_addition

        frame = binary_addition()
        frame.Show()

        self.Destroy()

# Subtraction (2's complment)


class learn_binary_subtraction_Frame(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Learn Binary Subtraction", size=(1000, 700))

        jpg = wx.Image("subtraction1.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    def onBack(self, event):
        from Title_Page import binary_subtraction

        frame = binary_subtraction()
        frame.Show()

        self.Destroy()


class binary_subtraction_test_Frame(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Binary Subtraction Test", size=(1000, 700))

        jpg = wx.Image("binarymathtestbg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (0, 0), (jpg.GetWidth(), jpg.GetHeight()))

        # -------------------------------------------

        import random

        decimal_value_1 = 0
        decimal_value_2 = 0

        for x in range(1):
            decimal_value_1 = random.randint(1, 100)
            decimal_value_2 = random.randint(1, 100)

        binary_value_1 = int(bin(decimal_value_1)[2:])
        binary_value_2 = int(bin(decimal_value_2)[2:])

        binary_value_1 = str(binary_value_1)
        binary_value_2 = str(binary_value_2)

        binary_value = bin(int(binary_value_1, 2) - int(binary_value_2, 2))

        self.binary_value = (binary_value[3:])  # making variable callable outside function

        # -------------------------------------------

        instructions = wx.StaticText(self.bmap, label="What is" + " " + binary_value_1 + " " + "-" + binary_value_2 + " " + "in binary?", pos=(420, 40))
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

        # Reterving usr answer from msgText variable
        value = self.msgTxt.GetValue()

        value = int(value)

        # Checking usr answer to calculated answer
        if value == self.binary_value:
            wx.StaticText(self.bmap, label="Correct", pos=(420, 80))
            correct += 1  # Adding one to total correct answers for this test
            if questions_asked <= test_length:  # Checking if the number of questions asked is less then the generated test length

                frame = binary_subtraction_test_Frame()  # Call to execute this frame again displaying new question
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

                frame = binary_subtraction_test_Frame()  # Call to execute this frame again displaying new question
                frame.Show(True)
                self.Destroy()

            else:
                frame = score_Frame()
                frame.Show()
                self.Destroy()

    def onBack(self, event):
        from Title_Page import binary_subtraction

        frame = binary_subtraction()
        frame.Show()

        self.Destroy()


# Multiplication

    # Teach

class learn_binary_multiplication(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Learn Binary Multiplication", size=(1000, 700))

        jpg = wx.Image("multiplication1.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    def onBack(self, event):
        from Title_Page import binary_multiplication

        frame = binary_multiplication()
        frame.Show()

        self.Destroy()

    # Test


class binary_multiplication_test_Frame(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Binary Multiplication Test", size=(1000, 700))

        jpg = wx.Image("binarymathtestbg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (0, 0), (jpg.GetWidth(), jpg.GetHeight()))

        # -------------------------------------------

        import random

        decimal_value_1 = 0
        decimal_value_2 = 0

        for x in range(1):
            decimal_value_1 = random.randint(1, 10)
            decimal_value_2 = random.randint(1, 10)

        binary_value_1 = int(bin(decimal_value_1)[2:])
        binary_value_2 = int(bin(decimal_value_2)[2:])

        binary_value_1 = str(binary_value_1)
        binary_value_2 = str(binary_value_2)

        binary_value = bin(int(binary_value_1, 2) * int(binary_value_2, 2))

        self.binary_value = (binary_value[2:])  # making variable callable outside function

        # -------------------------------------------

        instructions = wx.StaticText(self.bmap, label="What is" + " " + binary_value_1 + " " + "x" + binary_value_2 + " " + "in binary?", pos=(420, 40))
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
        if value == self.binary_value:
            wx.StaticText(self.bmap, label="Correct", pos=(420, 80))
            correct += 1  # Adding one to total correct answers for this test
            if questions_asked <= test_length:  # Checking if the number of questions asked is less then the generated test length

                frame = binary_multiplication_test_Frame()  # Call to execute this frame again displaying new question
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

                frame = binary_multiplication_test_Frame()  # Call to execute this frame again displaying new question
                frame.Show(True)
                self.Destroy()

            else:
                frame = score_Frame()
                frame.Show()
                self.Destroy()

    def onBack(self, event):
        from Title_Page import binary_multiplication

        frame = binary_multiplication()
        frame.Show()

        self.Destroy()
# Division

    # Teach


class learn_binary_division_Frame(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Learn Binary Division", size=(1000, 700))

        jpg = wx.Image("div1.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    def onBack(self, event):
        from Title_Page import binary_division

        frame = binary_division()
        frame.Show()

        self.Destroy()

    # Test


class binary_division_test_Frame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Binary Division Test", size=(1000, 700))

        jpg = wx.Image("binarymathtestbg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (0, 0), (jpg.GetWidth(), jpg.GetHeight()))

        # -------------------------------------------

        import random

        decimal_value_1 = 0
        decimal_value_2 = 0

        for x in range(1):
            decimal_value_1 = random.randint(1, 100)
            decimal_value_2 = random.randint(1, 100)

        binary_value_1 = int(bin(decimal_value_1)[2:])
        binary_value_2 = int(bin(decimal_value_2)[2:])

        binary_value_1 = str(binary_value_1)
        binary_value_2 = str(binary_value_2)

        binary_value = bin(int(binary_value_1, 2) % int(binary_value_2, 2))

        self.binary_value = (binary_value[2:])  # making variable callable outside function

        # -------------------------------------------

        instructions = wx.StaticText(self.bmap, label="What is" + " " + binary_value_1 + " " + "÷" + binary_value_2 + " " + "in binary?", pos=(420, 40))
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
        if value == self.binary_value:
            wx.StaticText(self.bmap, label="Correct", pos=(420, 80))
            correct += 1  # Adding one to total correct answers for this test
            if questions_asked <= test_length:  # Checking if the number of questions asked is less then the generated test length

                frame = binary_division_test_Frame()  # Call to execute this frame again displaying new question
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

                frame = binary_division_test_Frame()  # Call to execute this frame again displaying new question
                frame.Show(True)
                self.Destroy()

            else:
                frame = score_Frame()
                frame.Show()
                self.Destroy()

    def onBack(self, event):
        from Title_Page import binary_division

        frame = binary_division()
        frame.Show()

        self.Destroy()

# Defining Score frame to be displayed at the end of tests


class score_Frame(wx.Frame):

    def __init__(self):

        # Retrieving global variables
        global correct
        global wrong
        correct = str(correct)

        wx.Frame.__init__(self, None, wx.ID_ANY, "Test Score", size=(1000, 700))

        jpg = wx.Image("binarymathtestbg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        # Display to screen
        wx.StaticText(self.bmap, label="Correct:" + " " + str(correct), pos=(420, 240))
        wx.StaticText(self.bmap, label="With" + " " + str(wrong) + " " + "wrong answers", pos=(420, 280))


'''
Change Log:

~Added self.Destroy() to all open new frame functions to remove window build up 24/2/18

~Added question marks to test section displays 26/2/18

~Added comments to describe sections of code 28/2/28

~Removed double frame calls in test sections 28/2/18

~Added varied test length 28/2/18

~Fixed commenting errors 1/3/18

'''
