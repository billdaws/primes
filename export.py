def add_result(file, result):
    """Assumes `file` is open. `file` should be opened in append.
    """
    
    file.write()

def write_header(file):
    with open(file, "w") as f:
        header = "test,result,epi,mine,known,epi_equals_known,mine_equals_known"
        f.write(header)