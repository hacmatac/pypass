import click
import string
from password import Password
from random import SystemRandom
rand = SystemRandom()

@click.group()
def cli():
    pass

@cli.command()
@click.argument('password')
def analyze(password):
    """Provide analysis on the input password, assuming it was randomly generated"""
    P = Password(password=password)
    return print(P.analysis())

@cli.command()
@click.option(
    '--entropy',
    '-e',
    default=100,
    help="""
Generated password will have at least INTEGER bits of entropy (this is the default, set to 100 bits)
"""
)
@click.option(
    '--length',
    '-l',
    default=0,
    help="""
Generated password will have length of INTEGER characters (entropy option will be ignored)"""
)
@click.option(
    '--full',
    '-f', 
    is_flag=True,
    default=False,
    help="""
Password will be drawn from a full pool of 94 (non-whitespace) printable ascii characters: 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ Same as "--digits --lower --upper --special" or "--plain --special"
    """
)
@click.option(
    '--plain',
    '-p',
    is_flag=True,
    default=False,
    help="""
Password will be drawn from a pool of all 62 alphanumeric characters: 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ Same as "--digits --lower --upper" 
    """
)
@click.option(
    '--digits',
    '-d',
    is_flag=True,
    default=False,
    help="""
Password will be drawn from a pool of 10 digits: 0123456789
    """
)
@click.option(
    '--lower',
    '-a',
    is_flag=True,
    default=False,
    help="""
Password will be drawn from a pool of 26 lowercase alpha characters: abcdefghijklmnopqrstuvwxyz
    """
)
@click.option(
    '--upper',
    '-A',
    is_flag=True,
    default=False,
    help="""
Password will be drawn from a pool of 26 uppercase alpha characters: ABCDEFGHIJKLMNOPQRSTUVWXYZ
    """
)
@click.option(
    '--special',
    '-s',
    is_flag=True,
    default=False,
    help="""
Password will be drawn from a pool of 32 special characters/punctuation: !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
    """
)
@click.option(
    '--raw',
    '-r',
    is_flag=True,
    default=False,
    help="""
Print the raw password with no analysis
    """
)
def gen(entropy, length, full, plain, digits, lower, upper, special, raw):
    """Generate a random password with analysis"""
    def gen_pool(full, plain, digits, lower, upper, special):
        if full:
            return string.printable[:-6]
        elif plain:
            if special:
                return string.printable[:-6]
            else:
                return string.ascii_lowercase + string.ascii_uppercase + string.digits
        pool = []
        if digits:
            pool.append(string.digits)
        if lower:
            pool.append(string.ascii_lowercase)
        if upper:
            pool.append(string.ascii_uppercase)
        if special:
            pool.append(string.punctuation)
        if not pool:
            pool = string.printable[:-6]
        return ''.join(pool)
    pool = gen_pool(full, plain, digits, lower, upper, special)
    def get_password_length(length, pool, entropy):
        if length:
            True
        else:
            import math, cmath
            single_char_entropy = abs(cmath.log(len(pool), 2))
            length = math.ceil(entropy / single_char_entropy)
        return length
    length = get_password_length(length, pool, entropy)
    if length < 4:
        return print('Entropy too low. Increase entropy bits or password length')
    def gen_password(pool, length):
        password = ''.join([rand.choice(pool) for x in range(length)])
        P = Password(password=password)
        if len(P.pool()) != len(pool):
            return gen_password(pool, length)
        return P
    P = gen_password(pool, length)
    if raw:
        return print(P.password)
    return print(P.analysis())
