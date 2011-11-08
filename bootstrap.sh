# shell script for setting up environment
# assuming you're using virtualenv and pip, of course ;-)
# this is safe to run multiple times if you update requirements.txt
# (though if you want the env rebuilt, you'll need to remove it)

BASE=$(dirname $0)
ENV=$BASE/env

test ! -d $ENV && virtualenv --distribute --no-site-packages $ENV
pip install -E $ENV -r $BASE/requirements.txt

echo "== Bootstrap finished, use env/bin/activate to get started"
