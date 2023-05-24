### python3 Files
Paul Resnick, Univ of Michican


### ======= BASIC FILE OPS

# A read file into string

- 1 open file, read into string
- 2 print a slice of string
- 3 close file

# B read file into lines

- 1 read lines
- 2 print n lines
- 3 strip \n cf at end of line

# C print all lines simplified

# D get # of lines in file

# E get # of characters in file

//-------------------

### ======== FILE SEARCH

# F Finding a file in filesystem

Relative "../d/e/somefile.txt" vs Absolute "/a/b/myfile.txt"
generally absolute is not a good idea ~ containers

### ======== WRITING TO FILE

# G write

- 1 file.write( string )
- 2 add \n carriage return at end of each row

result:

```
1
4
9
16
2
--
```

### ======== WITH AS (CONTEXT MANAGER)

# H read/write w CM

- 1 with \_ as x:
- 2 can exec only 1 op
- 3 file close is automatic

### ======== WORKING W CSV FILES

# I read csv

- 1 query by parsing

# J write to csv

- 1 do reverse from read
