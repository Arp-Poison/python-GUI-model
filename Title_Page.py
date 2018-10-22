# Importing wx python module

import wx

# Defining title frame


class title_Frame(wx.Frame):
    # Defining Frame Constructor

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "Representation of data in a computer", size=(1000, 700))

        # Defining path to background image, image type, converting it to bitmap, defining its anchors
        jpg = wx.Image("homescreenbg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        # Creating and binding button widgets, as well as defining functions to call on click
        categories = wx.Button(self.bmap, label='Categories', pos=(460, 240), size=(100, 40))
        help = wx.Button(self.bmap, label='Help', pos=(460, 280), size=(100, 40))
        exit = wx.Button(self.bmap, label='Exit', pos=(460, 320), size=(100, 40))
        self.Bind(wx.EVT_BUTTON, self.help, help)
        self.Bind(wx.EVT_BUTTON, self.categories, categories)
        self.Bind(wx.EVT_BUTTON, self.exit, exit)

    def categories(self, event):
        frame = categories_Frame()
        frame.Show()

        self.Destroy()

    def help(self, event):
        frame = help_Frame()
        frame.Show()

        self.Bind(wx.EVT_CLOSE, self.exit)

    def exit(self, event):
        self.Destroy()


class categories_Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Categories", size=(1000, 698))

        # Defining path to background image, image type, converting it to bitmap, defining its anchors
        jpg = wx.Image("categoriesbg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        # Creating and binding button widgets, as well as defining functions to call on click
        character_representation = wx.Button(self.bmap, label='Character Representation', pos=(410, 210), size=(200, 40))
        different_number_systems = wx.Button(self.bmap, label='Alternate Number Systems', pos=(410, 250), size=(200, 40))
        integer_representation = wx.Button(self.bmap, label='Integer Representation', pos=(410, 290), size=(200, 40))
        floating_point = wx.Button(self.bmap, label="Floating Point Representation", pos=(410, 330), size=(200, 40))
        binary_arithmetic = wx.Button(self.bmap, label="Binary Arithmetic", pos=(410, 370), size=(200, 40))
        self.Bind(wx.EVT_BUTTON, self.character_represntation, character_representation)
        self.Bind(wx.EVT_BUTTON, self.diffrent_number_systems, different_number_systems)
        self.Bind(wx.EVT_BUTTON, self.integer_representation, integer_representation)
        self.Bind(wx.EVT_BUTTON, self.floating_point, floating_point)
        self.Bind(wx.EVT_BUTTON, self.binary_Arithmetic, binary_arithmetic)

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

# Functions to be called on button clicks
    def onBack(self, event):

        # Call to open frame
        frame = title_Frame(None, 1)
        frame.Show()

        self.Destroy()

    def character_represntation(self, event):

        # Call to open frame
        frame = character_rep_Frame()
        frame.Show()

        self.Destroy()

    def diffrent_number_systems(self, event):

        frame = diffrent_number_systems()
        frame.Show()

        self.Destroy()

    def integer_representation(self, event):

        frame = integer_representation()
        frame.Show()

        self.Destroy()

    def floating_point(self, event):

        frame = floating_point_representation()
        frame.Show()

        self.Destroy()

    def binary_Arithmetic(self, event):

        frame = binary_arithmetic()
        frame.Show()

        self.Destroy()


class help_Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Help", size=(1000, 700))

        # Defining path to background image, image type, converting it to bitmap, defining its anchors
        jpg = wx.Image("helpbg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    # Functions to be called on button clicks
    def onBack(self, event):
        frame = title_Frame(None, 1)
        frame.Show()

        self.Destroy()


class character_rep_Frame(wx.Frame):
    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Character Representation", size=(1000, 700))

        # Defining path to background image, image type, converting it to bitmap, defining its anchors
        jpg = wx.Image("charrepbg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        # Creating and binding button widgets, as well as defining functions to call on click
        ASCII = wx.Button(self.bmap, label='ASCII', pos=(460, 240), size=(100, 40))
        Unicode = wx.Button(self.bmap, label='Unicode', pos=(460, 280), size=(100, 40))
        self.Bind(wx.EVT_BUTTON, self.ASCII, ASCII)
        self.Bind(wx.EVT_BUTTON, self.Unicode, Unicode)

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    # Functions to be called on button clicks
    def onBack(self, event):
        frame = categories_Frame()
        frame.Show()

        self.Destroy()

    def ASCII(self, event):

        frame = ASCII_Frame()
        frame.Show()

        self.Destroy()

    def Unicode(self, event):

        frame = Unicode_Frame()
        frame.Show()

        self.Destroy()


class ASCII_Frame(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "ASCII", size=(1000, 700))

        # Defining path to background image, image type, converting it to bitmap, defining its anchors
        jpg = wx.Image("asciibg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        # Creating and binding button widgets, as well as defining functions to call on click
        learn = wx.Button(self.bmap, label='Learn', pos=(460, 240), size=(100, 40))
        test = wx.Button(self.bmap, label='Test', pos=(460, 280), size=(100, 40))
        self.Bind(wx.EVT_BUTTON, self.learn, learn)
        self.Bind(wx.EVT_BUTTON, self.test, test)

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    # Functions to be called on button clicks
    def onBack(self, event):
        frame = character_rep_Frame()
        frame.Show()

        self.Destroy()

    def learn(self, event):

        from CharacterRepresentation import learn_ASCII_Frame

        frame = learn_ASCII_Frame()
        frame.Show()

        self.Destroy()

    def test(self, event):

        from CharacterRepresentation import ASCII_test_Frame

        frame = ASCII_test_Frame()
        frame.Show()

        self.Destroy()


class Unicode_Frame(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Unicode", size=(1000, 700))

        # Defining path to background image, image type, converting it to bitmap, defining its anchors
        jpg = wx.Image("unicodebg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        # Creating and binding button widgets, as well as defining functions to call on click
        learn = wx.Button(self.bmap, label='Learn', pos=(460, 240), size=(100, 40))
        test = wx.Button(self.bmap, label='Test', pos=(460, 280), size=(100, 40))
        self.Bind(wx.EVT_BUTTON, self.learn, learn)
        self.Bind(wx.EVT_BUTTON, self.test, test)

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    # Functions to be called on button clicks
    def onBack(self, event):
        frame = character_rep_Frame()
        frame.Show()

        self.Destroy()

    def learn(self, event):

        from CharacterRepresentation import learn_unicode_Frame

        frame = learn_unicode_Frame()
        frame.Show()

        self.Destroy()

    def test(self, event):

        from CharacterRepresentation import unicode_test_Frame

        frame = unicode_test_Frame()
        frame.Show()

        self.Destroy()


class diffrent_number_systems(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Alternate Number Systems", size=(1000, 700))

        # Defining path to background image, image type, converting it to bitmap, defining its anchors
        jpg = wx.Image("altbg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        # Creating and binding button widgets, as well as defining functions to call on click
        binary = wx.Button(self.bmap, label='Binary', pos=(460, 240), size=(100, 40))
        hexadecimal = wx.Button(self.bmap, label='Hexadecimal', pos=(460, 280), size=(100, 40))
        decimal = wx.Button(self.bmap, label='Decimal', pos=(460, 320), size=(100, 40))
        self.Bind(wx.EVT_BUTTON, self.binary, binary)
        self.Bind(wx.EVT_BUTTON, self.hexadecimal, hexadecimal)
        self.Bind(wx.EVT_BUTTON, self.decimal, decimal)

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    # Functions to be called on button clicks
    def onBack(self, event):
        frame = categories_Frame()
        frame.Show()

        self.Destroy()

    def binary(self, event):

        frame = binary_Frame()
        frame.Show()

        self.Destroy()

    def hexadecimal(self, event):

        frame = hexadecimal_Frame()
        frame.Show()

        self.Destroy()

    def decimal(self, event):

        frame = decimal_Frame()
        frame.Show()

        self.Destroy()


class binary_Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Binary", size=(1000, 700))

        # Defining path to background image, image type, converting it to bitmap, defining its anchors
        jpg = wx.Image("binarybg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        # Creating and binding button widgets, as well as defining functions to call on click
        learn = wx.Button(self.bmap, label='Learn', pos=(460, 280), size=(100, 40))
        self.Bind(wx.EVT_BUTTON, self.learn, learn)
        test = wx.Button(self.bmap, label='Test', pos=(460, 320), size=(100, 40))
        self.Bind(wx.EVT_BUTTON, self.test, test)

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    # Functions to be called on button clicks
    def onBack(self, event):
        frame = diffrent_number_systems()
        frame.Show()

        self.Destroy()

    def learn(self, event):

        from AlternateNumberSystems import learn_binary_Frame

        frame = learn_binary_Frame()
        frame.Show()

        self.Destroy()

    def test(self, event):

        from AlternateNumberSystems import binary_test_Frame

        frame = binary_test_Frame()
        frame.Show()

        self.Destroy()


class hexadecimal_Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Hexadecimal", size=(1000, 700))

        # Defining path to background image, image type, converting it to bitmap, defining its anchors
        jpg = wx.Image("hexbg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        # Creating and binding button widgets, as well as defining functions to call on click
        learn = wx.Button(self.bmap, label='Learn', pos=(460, 300), size=(100, 40))
        self.Bind(wx.EVT_BUTTON, self.learn, learn)
        test = wx.Button(self.bmap, label='Test', pos=(460, 340), size=(100, 40))
        self.Bind(wx.EVT_BUTTON, self.test, test)

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    # Functions to be called on button clicks
    def onBack(self, event):
        frame = diffrent_number_systems()
        frame.Show()

        self.Destroy()

    def learn(self, event):

        from AlternateNumberSystems import learn_hexadecimal_Frame

        frame = learn_hexadecimal_Frame()
        frame.Show()

        self.Destroy()

    def test(self, event):

        from AlternateNumberSystems import hexadecimal_test_Frame

        frame = hexadecimal_test_Frame()
        frame.Show()

        self.Destroy()


class decimal_Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Decimal", size=(1000, 700))

        # Defining path to background image, image type, converting it to bitmap, defining its anchors
        jpg = wx.Image("binarybg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (10, 5), (jpg.GetWidth(), jpg.GetHeight()))

        # Creating and binding button widgets, as well as defining functions to call on click
        learn = wx.Button(self.bmap, label='Learn', pos=(460, 40), size=(100, 40))
        self.Bind(wx.EVT_BUTTON, self.learn, learn)
        test = wx.Button(self.bmap, label='Test', pos=(460, 70), size=(100, 40))
        self.Bind(wx.EVT_BUTTON, self.test, test)

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    # Functions to be called on button clicks
    def onBack(self, event):
        frame = diffrent_number_systems()
        frame.Show()

        self.Destroy()

    def learn(self, event):

        from AlternateNumberSystems import learn_decimal_Frame

        frame = learn_decimal_Frame()
        frame.Show()

        self.Destroy()

    def test(self, event):

        from AlternateNumberSystems import decimal_test_Frame

        frame = decimal_test_Frame()
        frame.Show()

        self.Destroy()


class integer_representation(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Integer Representation", size=(1000, 700))

        # Defining path to background image, image type, converting it to bitmap, defining its anchors
        jpg = wx.Image("integerrepbg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (-5, 0), (jpg.GetWidth(), jpg.GetHeight()))

        # Creating and binding button widgets, as well as defining functions to call on click
        sign_modulus_button = wx.Button(self.bmap, label='Sign and Modulus', pos=(430, 240), size=(130, 40))
        ones_complement_button = wx.Button(self.bmap, label='1s & 2s Complement', pos=(430, 280), size=(130, 40))
        self.Bind(wx.EVT_BUTTON, self.sign_modulus, sign_modulus_button)
        self.Bind(wx.EVT_BUTTON, self.ones_and_twos_complement, ones_complement_button)

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    # Functions to be called on button clicks
    def onBack(self, event):
        frame = categories_Frame()
        frame.Show()

        self.Destroy()

    def sign_modulus(self, event):

        frame = sign_modulus()
        frame.Show()

        self.Destroy()

    def ones_and_twos_complement(self, event):

        frame = ones_and_twos_complement()
        frame.Show()

        self.Destroy()


class sign_modulus(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Sign & Modulus", size=(1000, 700))

        # Defining path to background image, image type, converting it to bitmap, defining its anchors
        jpg = wx.Image("signmodbg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (-5, 0), (jpg.GetWidth(), jpg.GetHeight()))

        # Creating and binding button widgets, as well as defining functions to call on click
        learn = wx.Button(self.bmap, label='Learn', pos=(460, 240), size=(100, 40))
        self.Bind(wx.EVT_BUTTON, self.learn, learn)
        test = wx.Button(self.bmap, label='Test', pos=(460, 280), size=(100, 40))
        self.Bind(wx.EVT_BUTTON, self.test, test)

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    # Functions to be called on button clicks
    def onBack(self, event):
        frame = integer_representation()
        frame.Show()

        self.Destroy()

    def learn(self, event):
        from IntegerRepresentation import learn_sign_modulus_Frame

        frame = learn_sign_modulus_Frame()
        frame.Show()

        self.Destroy()

    def test(self, event):
        from IntegerRepresentation import sign_modulus_test_Frame

        frame = sign_modulus_test_Frame()
        frame.Show()

        self.Destroy()


class ones_and_twos_complement(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "1's & 2's Complement", size=(1000, 700))

        # Defining path to background image, image type, converting it to bitmap, defining its anchors
        jpg = wx.Image("complementsbg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (-5, 0), (jpg.GetWidth(), jpg.GetHeight()))

        # Creating and binding button widgets, as well as defining functions to call on click
        learn = wx.Button(self.bmap, label='Learn', pos=(460, 320), size=(100, 40))
        self.Bind(wx.EVT_BUTTON, self.learn, learn)
        test = wx.Button(self.bmap, label='Test', pos=(460, 360), size=(100, 40))
        self.Bind(wx.EVT_BUTTON, self.test, test)

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    # Functions to be called on button clicks
    def onBack(self, event):
        frame = integer_representation()
        frame.Show()

        self.Destroy()

    def learn(self, event):
        from IntegerRepresentation import learn_ones_and_twos_complement_Frame

        frame = learn_ones_and_twos_complement_Frame()
        frame.Show()

        self.Destroy()

    def test(self, event):
        from IntegerRepresentation import ones_and_twos_complement_test_Frame

        frame = ones_and_twos_complement_test_Frame()
        frame.Show()

        self.Destroy()


class floating_point_representation(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Floating Point Representation", size=(1000, 700))

        # Defining path to background image, image type, converting it to bitmap, defining its anchors
        jpg = wx.Image("floatingbg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (0, 0), (jpg.GetWidth(), jpg.GetHeight()))

        # Creating and binding button widgets, as well as defining functions to call on click
        real_numbers_button = wx.Button(self.bmap, label='Real Number Representation', pos=(380, 300), size=(250, 40))
        limitations_button = wx.Button(self.bmap, label="Limitations", pos=(380, 340), size=(250, 40))
        self.Bind(wx.EVT_BUTTON, self.real_number_representation, real_numbers_button)
        self.Bind(wx.EVT_BUTTON, self.limitations, limitations_button)

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    # Functions to be called on button clicks
    def onBack(self, event):
        frame = categories_Frame()
        frame.Show()

        self.Destroy()

    def real_number_representation(self, event):

        frame = real_number_representation_Frame()
        frame.Show()

        self.Destroy()

    def limitations(self, event):

        frame = limitations_Frame()
        frame.Show()

        self.Destroy()


class real_number_representation_Frame(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Real Number Representation", size=(1000, 700))

        # Defining path to background image, image type, converting it to bitmap, defining its anchors
        jpg = wx.Image("limitationsbg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (0, 0), (jpg.GetWidth(), jpg.GetHeight()))

        # Creating and binding button widgets, as well as defining functions to call on click
        learn = wx.Button(self.bmap, label='Learn', pos=(460, 240), size=(100, 40))
        self.Bind(wx.EVT_BUTTON, self.learn, learn)
        test = wx.Button(self.bmap, label='Test', pos=(460, 280), size=(100, 40))
        self.Bind(wx.EVT_BUTTON, self.test, test)

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    # Functions to be called on button clicks
    def onBack(self, event):
        frame = floating_point_representation()
        frame.Show()

        self.Destroy()

    def learn(self, event):
        from FloatingPointRepresentation import learn_real_number_representation_Frame

        frame = learn_real_number_representation_Frame()
        frame.Show()

        self.Destroy()

    def test(self, event):
        from FloatingPointRepresentation import real_number_representation_test_Frame

        frame = real_number_representation_test_Frame()
        frame.Show()

        self.Destroy()


class limitations_Frame(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Limitations", size=(1000, 700))

        # Defining path to background image, image type, converting it to bitmap, defining its anchors
        jpg = wx.Image("limitationsbg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (0, 0), (jpg.GetWidth(), jpg.GetHeight()))

        # Creating and binding button widgets, as well as defining functions to call on click
        learn = wx.Button(self.bmap, label='Learn', pos=(460, 240), size=(100, 40))
        self.Bind(wx.EVT_BUTTON, self.learn, learn)
        test = wx.Button(self.bmap, label='Test', pos=(460, 280), size=(100, 40))
        self.Bind(wx.EVT_BUTTON, self.test, test)

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    # Functions to be called on button clicks
    def onBack(self, event):
        frame = floating_point_representation()
        frame.Show()

        self.Destroy()

    def learn(self, event):
        from FloatingPointRepresentation import learn_limitations_Frame

        frame = learn_limitations_Frame()
        frame.Show()

        self.Destroy()

    def test(self, event):
        from FloatingPointRepresentation import limitations_test_Frame

        frame = limitations_test_Frame()
        frame.Show()

        self.Destroy()


class binary_arithmetic(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Binary Arithmetic", size=(1000, 700))

        # Defining path to background image, image type, converting it to bitmap, defining its anchors
        jpg = wx.Image("binarymathbg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (0, 0), (jpg.GetWidth(), jpg.GetHeight()))

        # Creating and binding button widgets, as well as defining functions to call on click
        binary_addition_button = wx.Button(self.bmap, label='Binary Addition', pos=(423, 240), size=(138, 40))
        binary_subtraction_button = wx.Button(self.bmap, label='Binary Subtraction', pos=(423, 280), size=(138, 40))
        binary_multiplication_button = wx.Button(self.bmap, label='Binary Multiplication', pos=(423, 320), size=(138, 40))
        binary_division_button= wx.Button(self.bmap, label="Binary Division", pos=(423, 360), size=(138, 40))
        self.Bind(wx.EVT_BUTTON, self.binary_addition, binary_addition_button)
        self.Bind(wx.EVT_BUTTON, self.binary_subtraction, binary_subtraction_button)
        self.Bind(wx.EVT_BUTTON, self.binary_multiplication, binary_multiplication_button)
        self.Bind(wx.EVT_BUTTON, self.binary_division, binary_division_button)

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    # Functions to be called on button clicks
    def onBack(self, event):
        frame = categories_Frame()
        frame.Show()

        self.Destroy()

    def binary_addition(self, event):

        frame = binary_addition()
        frame.Show()

        self.Destroy()

    def binary_subtraction(self, event):

        frame = binary_subtraction()
        frame.Show()

        self.Destroy()

    def binary_multiplication(self, event):

        frame = binary_multiplication()
        frame.Show()

        self.Destroy()

    def binary_division(self, event):

        frame = binary_division()
        frame.Show()

        self.Destroy()


class binary_addition(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Binary Addition", size=(1000, 700))

        # Defining path to background image, image type, converting it to bitmap, defining its anchors
        jpg = wx.Image("binaryaddbg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (0, 0), (jpg.GetWidth(), jpg.GetHeight()))

        # Creating and binding button widgets, as well as defining functions to call on click
        learn = wx.Button(self.bmap, label='Learn', pos=(460, 240), size=(100, 40))
        self.Bind(wx.EVT_BUTTON, self.learn, learn)
        test = wx.Button(self.bmap, label='Test', pos=(460, 280), size=(100, 40))
        self.Bind(wx.EVT_BUTTON, self.test, test)

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    # Functions to be called on button clicks
    def onBack(self, event):
        frame = binary_arithmetic()
        frame.Show()

        self.Destroy()

    def learn(self, event):
        from BinaryArithmetic import learn_binary_addition_Frame

        frame = learn_binary_addition_Frame()
        frame.Show()

        self.Destroy()

    def test(self, event):
        from BinaryArithmetic import binary_addition_test_Frame

        frame = binary_addition_test_Frame()
        frame.Show()

        self.Destroy()


class binary_subtraction(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Binary Subtraction", size=(1000, 700))

        # Defining path to background image, image type, converting it to bitmap, defining its anchors
        jpg = wx.Image("binarysubbg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (0, 0), (jpg.GetWidth(), jpg.GetHeight()))

        # Creating and binding button widgets, as well as defining functions to call on click
        learn = wx.Button(self.bmap, label='Learn', pos=(460, 240), size=(100, 40))
        self.Bind(wx.EVT_BUTTON, self.learn, learn)
        test = wx.Button(self.bmap, label='Test', pos=(460, 280), size=(100, 40))
        self.Bind(wx.EVT_BUTTON, self.test, test)

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    # Functions to be called on button clicks
    def onBack(self, event):
        frame = binary_arithmetic()
        frame.Show()

        self.Destroy()

    def learn(self, event):
        from BinaryArithmetic import learn_binary_subtraction_Frame

        frame = learn_binary_subtraction_Frame()
        frame.Show()

        self.Destroy()

    def test(self, event):
        from BinaryArithmetic import binary_subtraction_test_Frame

        frame = binary_subtraction_test_Frame()
        frame.Show()

        self.Destroy()


class binary_multiplication(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Binary Multiplication", size=(1000, 700))

        # Defining path to background image, image type, converting it to bitmap, defining its anchors
        jpg = wx.Image("binarymultbg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (0, 0), (jpg.GetWidth(), jpg.GetHeight()))

        # Creating and binding button widgets, as well as defining functions to call on click
        learn = wx.Button(self.bmap, label='Learn', pos=(460, 240), size=(100, 40))
        self.Bind(wx.EVT_BUTTON, self.learn, learn)
        test = wx.Button(self.bmap, label='Test', pos=(460, 280), size=(100, 40))
        self.Bind(wx.EVT_BUTTON, self.test, test)

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    # Functions to be called on button clicks
    def onBack(self, event):
        frame = binary_arithmetic()
        frame.Show()

        self.Destroy()

    def learn(self, event):
        from BinaryArithmetic import learn_binary_multiplication

        frame = learn_binary_multiplication()
        frame.Show()

        self.Destroy()

    def test(self, event):
        from BinaryArithmetic import binary_multiplication_test_Frame

        frame = binary_multiplication_test_Frame()
        frame.Show()

        self.Destroy()


class binary_division(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Binary Division", size=(1000, 700))

        # Defining path to background image, image type, converting it to bitmap, defining its anchors
        jpg = wx.Image("binarydivbg.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmap = wx.StaticBitmap(self, -1, jpg, (0, 0), (jpg.GetWidth(), jpg.GetHeight()))

        # Creating and binding button widgets, as well as defining functions to call on click
        learn = wx.Button(self.bmap, label='Learn', pos=(460, 240), size=(100, 40))
        self.Bind(wx.EVT_BUTTON, self.learn, learn)
        test = wx.Button(self.bmap, label='Test', pos=(460, 280), size=(100, 40))
        self.Bind(wx.EVT_BUTTON, self.test, test)

        back_button = wx.Button(self.bmap, label="Back", pos=(10, 650))
        back_button.Bind(wx.EVT_BUTTON, self.onBack)

    # Functions to be called on button clicks
    def onBack(self, event):
        frame = binary_arithmetic()
        frame.Show()

        self.Destroy()

    def learn(self, event):
        from BinaryArithmetic import learn_binary_division_Frame

        frame = learn_binary_division_Frame()
        frame.Show()

        self.Destroy()

    def test(self, event):
        from BinaryArithmetic import binary_division_test_Frame

        frame = binary_division_test_Frame()
        frame.Show()

        self.Destroy()

#App constructor


if __name__ == '__main__':
    app = wx.App()
    frame = title_Frame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()

# --------------------------------------------------#

'''
Change Log:

~Imported other scripts and linked frames for teach and lean sections 2/2/18

~Centered buttons to middle of frames 18/2/183

~Created backgrounds for home screen and categories screen 20/2/18

~Fixed length of button elements to fit text 23/2/18

~Added self.Destroy() to all open new frame functions to remove window build up 24/2/18

~Moved self.Destroy() to after new frame has opened iscase of failure to open new window 24/2/18

~Removed redundant buttons and frames 25/2/18

~Added backgrounds for every sub directory from categories frame 28/2/18

~Added back buttons to every frame in this scope 28/2/18

~Added comments to explain the function of sections of code 28/2/18

~Changed app class to app = wx.App() instead of app = wx.SimpleApp() which was out dated 29/2/18

~Fixed commenting errors 1/3/18

'''


