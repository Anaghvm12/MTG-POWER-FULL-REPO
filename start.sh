if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Aadhi000/Ajax.git /Ajax /EvaMaria
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Ajax
fi
cd /EvaMaria
pip3 install -U -r requirements.txt
echo " Starting Mtg....🔥"
python3 bot.py
