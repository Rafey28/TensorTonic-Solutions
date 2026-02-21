def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # Write code here
    step = chunk_size - overlap
    token_new = []
    for i in range(0,len(tokens),step):
        if (i + chunk_size >= len(tokens)):
            token_new.append(tokens[i:])
            break
        else:
            token_new.append(tokens[i:i+chunk_size])

    
    return token_new
    
        
        
        
        