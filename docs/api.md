#### see(name[, default])
Returns the string the gods assigned to the environment variable named `name`.
If there is no message named `name` and `default` is provided, its value is
returned. If `default` isn't provided and no message named `name` exists, an
Exception is raised explaining such.

#### see_number(name[, default])
#### see_boolean(name[, default])
Similar to `see()` except the gods' message is interpreted as a number or
boolean respectively if it exists. If the message can't be interpreted as a
number or boolean, an Exception is raised explaining such. `default` must be
a number for `see_number` or a boolean for `see_boolean`, or else a similar
Exception will be raised if its value is used.

#### see_sequence(name[, default])
Similar to `see()` except the god's message is interpreted as a sequence of
strings. The god's message should be a comma delimited set of values. The
sequence returned will always be a tuple. `default` should be a sequence.

#### see_interpretation(name, interpreter[, interpretation_error]\[, default]\)
Similar to `see()` and the rest, except `interpreter` is used to interpret
the gods' message. `interpreter` should take a string as an argument and return
whatever type of object it interprets. If the string doesn't fit the
interpretation, it should raise a ValueError.
`interpretation_error` should be given as an argument to provide more
informative error messages when interpretation fails. It should be a string. It
will be interpolated with two keywords `name` and `value` before being used
as an Exception string.

#### tell(name[, default])
#### tell_number(name[, default])
#### tell_boolean(name[, default])
#### tell_sequence(name[, default])
#### tell_interpretation(name, interpreter[, default])
Like the functions described above, but returns a 0-ary function that when
called returns what the corresponding `see*` functions would have.
