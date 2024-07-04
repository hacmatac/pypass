class Password:

    def __init__(self, password):
        self.password = password

    def length(self):
        return len(self.password)
 
    def pool(self):
        import re, string
        regexes = {
            string.digits: re.compile(r'\d'),
            string.ascii_lowercase: re.compile(r'[a-z]'),
            string.ascii_uppercase: re.compile(r'[A-Z]'),
            string.punctuation: re.compile(r'[!"#$%&\'()*+,-./:;<=>?@[\\\]^_`{|}~]'),
        }
        return ''.join([key for key, value in regexes.items() if value.search(self.password)])
      
    def search_space(self):
        search_space = 0
        for x in range(1, self.length() + 1):
            result = len(self.pool()) ** x
            search_space += result
        return search_space

    def entropy(self):
        import cmath
        single_char_entropy = abs(cmath.log(len(self.pool()), 2))
        return single_char_entropy * self.length()

    def cracking_average_years(self):
        attacks = [
            ['One Million ----------------->', 10 ** 6],
            ['One Billion ----------------->', 10 ** 9],
            ['One Trillion ---------------->', 10 ** 12],
            ['One Quadrillion ------------->', 10 ** 15],
            ['One Quintillion ------------->', 10 ** 18],
            ['One Sextillion -------------->', 10 ** 21],
            ['One Septillion -------------->', 10 ** 24],
            ['One Octillion --------------->', 10 ** 27],
            ['One Nonillion --------------->', 10 ** 30],
            ['One Decillion --------------->', 10 ** 33],
            ['One Undecillion ------------->', 10 ** 36],
            ['One Duodecillion ------------>', 10 ** 39],
            ['One Tredecillion ------------>', 10 ** 42],
            ['One Quattuordecillion ------->', 10 ** 45],
            ['One Quindecillion ----------->', 10 ** 48],
            ['One Sexdecillion ------------>', 10 ** 51],
            ['One Septendecillion --------->', 10 ** 54],
            ['One Octodecillion ----------->', 10 ** 57],
            ['One Novemdecillion ---------->', 10 ** 60],
            ['One Vigintillion ------------>', 10 ** 63],
        ]
        for i in attacks:
            average_cracking_seconds = 0.5 * self.search_space() / i[1]
            i[1] = int(average_cracking_seconds / 31557600)
            if i[1] == 0:
                i[1] = '< 1'
        return tuple(attacks)

    def analysis(self):
        """Password analysis"""
        data = f"""
Password Analysis:

Password: {self.password}
Bits of Entropy: {round(self.entropy(), 1)}
Pool Size: {len(self.pool())} ({self.pool()}) 
Length: {self.length()} characters
Search Space: {self.search_space()}\n\n"""

        brute_force = """Brute-force Attack Scenarios:
\nGuesses per second\t\tAverage cracking time (years)\n
        """
        attacks = ''.join([f'\n{i[0]}\t{i[1]}' for i in self.cracking_average_years()])
        return data + brute_force + attacks
