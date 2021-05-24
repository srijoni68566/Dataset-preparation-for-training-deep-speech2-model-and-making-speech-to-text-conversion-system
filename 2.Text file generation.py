# converting text transcripts to text file scanning row by row
i = 0 
for index, row in data.iterrows( ) :
f = open (str (df.text_column[ i ] ) + ‘ .txt’ , ‘w’ , encoding = ‘utf-8’ )
f.write ( row[0] )
f.close( )
i += 1
