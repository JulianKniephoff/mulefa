`mulefa`
========

Just a small Python script,
displaying a transparent full screen window.
The purpose of this for me
is to capture mouse wheel inputs
while using the enhanced desktop zoom feature
of hte Compiz window manager,
to keep them away from other windows
like browsers
which might interpret them
as an intent to scroll.

Usage
-----

Just bind this program
to a global keyboard shortcut
that includes the Windows key.
I have it set to `Windows + Z`
The idea is that you press that combination,
release everything **but** the Windows key,
adjust your zoom level using the mouse wheel,
and then release the Windows key as well.
The last step will automatically close the window opened by this program.

Requirements
------------

This program is not Compiz specific at all.
I don't know how other window managers
handle the situation described above,
but if yours has this problem as well,
you should still be able to use this workaround.

You **do** hovever need Python and PyQt, specifically.
