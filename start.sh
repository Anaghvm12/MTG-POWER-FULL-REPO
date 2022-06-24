if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Anaghvm12/MTG-POWER-FULL-REPO.git /Anaghvm12
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Anaghvm12
fi
cd /EvaMaria
pip3 install -U -r requirements.txt
echo " Starting Alia....🔥"
python3 bot.py
