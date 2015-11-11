hg clone https://bitbucket.org/logilab/pylint/
hg clone https://bitbucket.org/logilab/astroid
mkdir logilab && touch logilab/__init__.py
hg clone http://hg.logilab.org/logilab/common logilab/common
cd pylint && sudo python setup.py install
