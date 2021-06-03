revstring = 'ocip{FTC0l_I4_t5m_ll0m_y_y3n58a025e3ÿ'
n = 4

revlist = [revstring[i:i+n] for i in range(0, len(revstring), n)]
chunks = [chunk[::-1] for chunk in revlist]
print(''.join(chunks))
