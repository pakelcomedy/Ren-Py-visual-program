label start:
    scene bg blck
    if not name:
        $ name = renpy.input("What's your name (max. 14 characters)","PakelComedy","abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ","{}",14)
    $ renpy.show_screen("history", _layer="master")
    python:
        ncolor = c.who_args["color"]
        prompt = renpy.input("{color=[ncolor]}[name]{/color}")
        outval = dogpt(gptmodel, gpttemp, prompt)
        outval = outval[2:] if outval[:2] == "\n\n" else outval
        e.add_history(kind=nvl, who="GPT-Chan", what=outval)
        c.add_history(kind=nvl, who=name, what=prompt)
    jump start