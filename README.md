Jojen of House Reed is gifted with greensight. The old gods see fit to provide
him with information through the ENVIRONMENT. He'll share that information with
you as is if you ask:

    $ FOO=bar python
    >>> import jojen
    >>> jojen.see("FOO")
    'bar'
    >>>

Jojen has had his gift for most of his life. He's had time to ponder on them
and draw usual interpretations. You can ask him to share them:

    $ FOO=1 BAR=True BAZ=a,b,c python
    >>> import jojen; jojen.see_number("FOO")
    1
    >>> jojen.see_boolean("BAR")
    True
    >>> jojen.see_sequence("BAZ")
    ('a', 'b', 'c')
    >>>

Jojen's honest. Sometimes the information the gods send doesn't quite fit his
interpretations, but he'll own up to it. He'll clearly epxlain to you exactly
how it doesn't fit too:

    $ FOO=bar python
    >>> import jojen; jojen.see_number("FOO")
    Traceback (most recent call last):
        <...>
    Exception: The gods' message 'FOO' was not a number. Its value was 'bar'.
    >>>

If you think your interpretation of the gods' messages would fit better than
Jojen's, by all means, explain them to him and he'll use them when he sees:

    $ FOO=(1 3 5)
    >>> import jojen; from sexprs import read_sexpr_str
    >>> jojen.see_interpretation("FOO", read_sexpr_str)
    (1 3 5)
    >>>

If you get sick of asking Jojen these things, you can just remember how he told
them. (Re)call that telling and you'll get the latest value for it.

    $ FOO=bar BAZ=1 python
    >>> import jojen
    >>> foo = jojen.tell("FOO")
    >>> foo()
    'bar'
    >>> baz = jojen.tell_number("BAZ")
    >>> baz()
    1
    >>>

This is useful in a situation where the gods are fickle and the information
they give can change. Perhaps when some thread influences them?

Just in case I missed anything in this introduction, a full listing of what
Jojen can do is available in [docs/api.md](docs/api.md).
