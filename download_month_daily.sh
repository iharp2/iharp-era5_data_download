source venv/bin/activate

# call python download_daily.py for each day
# $1 is the month
# $2 is the number of days in the month

for i in {1..$2}
do
    python download_daily.py -m $1 -d $i
done

deactivate
