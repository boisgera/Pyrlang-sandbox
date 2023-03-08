
Do:

    $ iex --name oddball@192.168.1.85 --cookie banana
    Erlang/OTP 25 [erts-13.1.5] [source] [64-bit] [smp:8:8] [ds:8:8:10] [async-threads:1] [jit:ns]

    Interactive Elixir (1.15.0-dev) - press Ctrl+C to exit (type h() ENTER for help)
    iex(oddball@192.168.1.85)1> Process.register(self(), :target)
    true
    iex(oddball@192.168.1.85)2> Node.list()
    []

then

    $ python node.py
    ALIVE2 returned error 1
    ALIVE2 failed
    Send to unknown global_name_server ignored
    rex unhandled info msg: (<1678288018.54.0 @ oddball@192.168.1.85>, Atom('features_request'))
    ⏳
    
Then, back in iex

    iex(oddball@192.168.1.85)3> Node.list()
    [:"py@192.168.1.85"]
    iex(oddball@192.168.1.85)4> flush()
    :hello
    :ok

So basically, it works!

Errow/warning analysis:

    - No idea so far what `ALIVE2` is about.

    - `global_name_server` is an erlang stuff, not pyrlang.

    - I wouldn't be too worried about the undhandled info message.
      `features_request` seems to be an atom used by erlang rpc lib.

TODO: test remote stuff, visibility of the nodes, etc.