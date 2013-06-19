Build slides:

    $ python build_slides.py presentation.md
    
`presentation.html` will be in the directory. To make the logo:

    $ wget http://3.bp.blogspot.com/_8yDjtDOx9ws/TSxxlk__32I/AAAAAAAAFlE/0D3BmlKmvbI/s1600/NIST_logo.jpg
    $ convert NIST_logo.jpg NIST_logo.png
    $ convert -fuzz 10% -transparent white NIST_logo.png NIST_logo_transparent.png
