# Step 1: Merge 2 files into merged.txt
Suppose your two files are named file1.txt and file2.txt. Use the cat command:
cat file1.txt file2.txt > merged.txt
This command combines the contents of file1.txt and file2.txt into merged.txt.

#Count lines, words, and characters in merged.txt

Use the wc (word count) command:

wc merged.txt


This outputs something like:

  100  200 1500 merged.txt


Where:

100 → number of lines
200 → number of words
1500 → number of characters