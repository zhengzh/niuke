
# bash string remove operator
# https://stackoverflow.com/questions/125281/how-do-i-remove-the-file-suffix-and-path-portion-from-a-path-string-in-bash
base=${1%.*}
cat $base.txt | python3 $base.py